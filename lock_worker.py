from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock
import time, sys, random, os

def main(worker_id):
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    lock = Lock(zk, '/demo-lock')

    while True:
        print(f"Worker {worker_id} trying to acquire lock...")
        with lock:
            print(f"[Worker {worker_id}] Acquired lock! Doing critical section...")
            time.sleep(30 + random.random())  # simulate work
            print(f"[Worker {worker_id}] Released lock!")
        time.sleep(1 + random.random())      # simulate non-critical work

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lock_worker.py <worker_id>")
        sys.exit(1)
    main(sys.argv[1])