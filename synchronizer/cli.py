import argparse
import os
from synchronizer import FileSystemSynchronizer


def get_args():
    parser = argparse.ArgumentParser(
        description="Multi-process synchronized based on shared file system."
    )

    parser.add_argument(
        '--shared_dir', '-d',
        type=str,
        required=True,
        default=None,
        help="An empty directory on the shared file system, "
             "used to synchronize multiple processes."
    )
    parser.add_argument(
        '--num_processes', '-np',
        type=int,
        required=True,
        default=1,
        help="Number of processes to synchronize."
    )
    parser.add_argument(
        '--rank', '-r',
        type=int,
        required=True,
        default=0,
        help="Rank of the current process."
    )

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    sd = args.shared_dir
    assert sd, "A empty directory must be specified."
    assert len(os.listdir(sd)) == 0, f"{sd} must be empty."
    np = args.num_processes
    assert np > 0
    r = args.rank
    fs_sync = FileSystemSynchronizer(sd, r, np)
    fs_sync.barrier()

if __name__ == "__main__":
    main()
