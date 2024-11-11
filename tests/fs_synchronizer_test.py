from synchronizer import FileSystemSynchronizer
from multiprocessing import Process


def worker(rank, num_processes):
    fs_sync = FileSystemSynchronizer('test', rank, num_processes)
    fs_sync.barrier()
    print(f"Rank {rank} passed the barrier.")


def main(num_processes):
    processes = []
    for i in range(num_processes):
        p = Process(target=worker, args=(i, num_processes,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    main(num_processes=64)
