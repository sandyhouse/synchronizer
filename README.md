# Synchronizer

This is a synchronization library used to synchronize multiple processes in distributed systems.

## Install

You can install this package with pip using the following command:

```shell
pip install py-synchronizer
```

## Usage

```python
from py-synchronizer import FileSystemSynchronizer
from multiprocessing import Process


def main(num_processes):
    fs_sync = FileSystemSynchronizer('test', rank, world_size)
    fs_sync.barrier()

if __name__ == "__main__":
    main()
```

## FileSystemSynchronizer

```python
FileSystemSynchronizer(shared_dir, rank, world_size)
```

Parameters:
- shared_dir: A directory on a shared file system that can be accessed by all processes; **this directory must be empty**.
- rank: Rank id of the current process
- world_size: Total number of processes.
