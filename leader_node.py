from kazoo.client import KazooClient
from kazoo.recipe.election import Election
import sys, time, os

def leader_task(worker_id):
    print(f"[Node {worker_id}] I am now the leader! (PID={os.getpid()})")
    # Do leader work; stay leader until process killed
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"[Node {worker_id}] Stepping down.")

def main(worker_id):
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    election = Election(zk, "/demo-election")

    print(f"[Node {worker_id}] Starting, waiting for leadership...")
    election.run(lambda: leader_task(worker_id))
    zk.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python leader_node.py <node_id>")
        sys.exit(1)
    main(sys.argv[1])