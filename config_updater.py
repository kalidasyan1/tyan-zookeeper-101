from kazoo.client import KazooClient
import sys, time

if __name__ == "__main__":
    zk = KazooClient(hosts="127.0.0.1:2181")
    zk.start()
    zk.ensure_path("/configs")
    zk.ensure_path("/configs/demo")

    print("Type new config values (or Ctrl-C to quit):")
    while True:
        try:
            new_value = input("Enter config: ")
            zk.set("/configs/demo", new_value.encode())
            print("Updated config to:", new_value)
        except KeyboardInterrupt:
            break

    zk.stop()