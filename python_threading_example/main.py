import threading
import time

def thread_function(name):
    """スレッドで実行される関数"""
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")

def main():
    threads = []
    for i in range(3):
        # スレッドを生成し、リストに追加
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    # すべてのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

    print("All threads have finished.")

if __name__ == "__main__":
    main()
