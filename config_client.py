from kazoo.client import KazooClient
import time

def watch_config(event):
    data, _ = zk.get("/configs/demo", watch=watch_config)
    print(f"[Worker] Config changed! New value: {data.decode()}")

if __name__ == "__main__":
    zk = KazooClient(hosts="127.0.0.1:2181")
    zk.start()
    zk.ensure_path("/configs/demo")

    # Set initial watch
    data, _ = zk.get("/configs/demo", watch=watch_config)
    print(f"[Worker] Initial config value: {data.decode()}")
    
    print("[Worker] Watching for config updates (Ctrl-C to quit)...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    zk.stop()