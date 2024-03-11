import threading
import queue
import time

class MessageBox:
    def __init__(self):
        self.queue = queue.Queue()

    def send(self, message):
        """メッセージを送信するメソッド"""
        self.queue.put(message)

    def receive(self, timeout):
        """メッセージを受信するメソッド。タイムアウト機能付き"""
        try:
            message = self.queue.get(timeout=timeout)
            return True, message  # メッセージ受信
        except queue.Empty:
            return False, None  # タイムアウト

def thread_task(name, message_box):
    """スレッドが実行するタスク"""
    print(f"Thread {name}: Waiting for message...")
    received, message = message_box.receive(10)  # 10秒のタイムアウト
    if received:
        print(f"Thread {name}: Received message '{message}'")
    else:
        print(f"Thread {name}: No message received (timeout)")

def main():
    # メッセージボックスのインスタンスを各スレッドに渡す
    message_boxes = {i: MessageBox() for i in range(3)}
    threads = []

    # 3つの子スレッドを起動
    for i in range(3):
        thread = threading.Thread(target=thread_task, args=(i, message_boxes[i]))
        threads.append(thread)
        thread.start()

    # メインスレッドから各子スレッドにメッセージを送信
    time.sleep(2)  # 子スレッドが起動して受信準備ができるまで少し待つ
    for i in range(3):
        message_boxes[i].send(f"Message for thread {i}")

    # すべての子スレッドの終了を待つ
    for thread in threads:
        thread.join()

    print("All threads have finished.")

if __name__ == "__main__":
    main()
