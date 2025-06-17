# ZooKeeper Mini-Projects: Distributed Lock & Leader Election (Python, MacOS, Kazoo)

This repo contains two Python-based mini-projects to demonstrate distributed coordination with ZooKeeper:

- **Project 1:** Distributed Lock Simulation (`lock_worker.py`)
- **Project 2:** Leader Election Simulation (`leader_node.py`)

Both can be run on MacOS with local ZooKeeper and simulate three nodes/workers.

---

## Prerequisites

1. **Install ZooKeeper locally**
   - With Homebrew:
     ```bash
     brew install zookeeper
     ```
   - Or [download from official site](https://zookeeper.apache.org/releases.html).

2. **Start ZooKeeper server (standalone mode)**
   ```bash
   zkServer start
   # Or if installed with Homebrew:
   zookeeper-server-start
   ```

3. **Install Python, create a virtual environment, and install dependencies**
   ```bash
   mkdir zookeeper-demo
   cd zookeeper-demo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   code .
   ```
   - Open the folder in VS Code and select the Python interpreter from the `venv` you just created.

4. **Clone/download the Python scripts**
   - Save the provided code into two files:
     - `lock_worker.py`
     - `leader_node.py`

---

## Project 1: Distributed Lock (`lock_worker.py`)

Simulates three workers competing for a distributed lock. Only one worker enters the critical section at any time.

**How to run:**
1. Open three terminal tabs, activate the Python venv in each:
   ```bash
   source venv/bin/activate
   ```
2. Run each worker with a unique ID (e.g., 1, 2, 3):
   ```bash
   python lock_worker.py 1
   # In another terminal:
   python lock_worker.py 2
   # In another terminal:
   python lock_worker.py 3
   ```
3. You’ll observe workers acquiring and releasing the lock in turn.

---

## Project 2: Leader Election (`leader_node.py`)

Simulates three nodes competing for cluster leadership. Only one node is leader at any time; when the leader stops, another is automatically elected.

**How to run:**
1. In three terminals, activate your venv:
   ```bash
   source venv/bin/activate
   ```
2. Run each node with a unique ID:
   ```bash
   python leader_node.py 1
   # In another terminal:
   python leader_node.py 2
   # In another terminal:
   python leader_node.py 3
   ```
3. The leader node prints leadership status; if you kill it, one of the remaining nodes becomes the leader.

---

## ZooKeeper CLI: Inspecting Lock/Election Status

You can use the ZooKeeper CLI to observe the znodes and coordination:

1. Start the CLI:
   ```bash
   zkCli
   ```
2. Check lock/election participants:
   ```bash
   ls /demo-lock
   ls /demo-election
   ```
3. Get details of a node (will be empty for lock nodes):
   ```bash
   get /demo-lock/<lock-node-name>
   get /demo-election/<leader-node-name>
   ```
4. Watch for changes:
   ```bash
   ls /demo-lock true
   ls /demo-election true
   ```

- The lock/election node with the lowest sequence number is the holder/leader.

---

## Troubleshooting

- Make sure ZooKeeper is running before starting Python scripts.
- If `kazoo` can't connect, check that ZooKeeper listens on `localhost:2181`.
- If you see empty output for `get` on a znode, that's normal for ephemeral sequential nodes used by the lock/leader recipes.

---

## References

- [ZooKeeper Official Docs](https://zookeeper.apache.org/doc/current/)
- [Kazoo Python Library](https://kazoo.readthedocs.io/)
- [ZooKeeper CLI Reference](https://zookeeper.apache.org/doc/current/zookeeperStarted.html#sc_zkCommands)
