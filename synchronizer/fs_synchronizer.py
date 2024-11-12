from filelock import FileLock
import glob
import os
import time
from tempfile import NamedTemporaryFile
from .synchronizer import Synchronizer


class FileSystemSynchronizer(Synchronizer):
    def __init__(
            self,
            shared_dir: str,
            rank: int=None,
            world_size: int=None):
        super().__init__(rank, world_size)
        self.shared_dir = shared_dir
        if self.rank == 0:
            NamedTemporaryFile(
                dir=self.shared_dir,
                suffix='.lock',
                delete=False).close()
        self.lock_file = self._get_lock_file()
        self.file = self.lock_file.replace('.lock', '')
        
    def _get_lock_file(self):
        lock_files = glob.glob(os.path.join(self.shared_dir, '*.lock'))
        while len(lock_files) == 0:
            time.sleep(2)
            lock_files = glob.glob(os.path.join(self.shared_dir, '*.lock'))
        
        assert len(lock_files) == 1, (
            f"Expecting only one lock file in the shared directory, "
            f"but got {len(lock_files)}. Make sure the shared directory "
            f"({self.shared_dir}) is clean."
        )
        return lock_files[0]

    def barrier(self):
        with FileLock(self.lock_file):
            data = None
            if not os.path.exists(self.file):
                open(self.file, 'w').close()
            with open(self.file, 'r') as f:
                data = f.readline()
                if data == '':
                    data = '1'
                else:
                    data = str(int(data) + 1)
            with open(self.file, 'w') as f:
                f.write(data)
        
        while True:
            with FileLock(self.lock_file):
                with open(self.file, 'r') as f:
                    data = f.readline()
            if int(data) == self.world_size:
                break
            time.sleep(2)
