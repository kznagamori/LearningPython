import threading
import queue
import time

# キューの最大サイズを3に設定
message_queue = queue.Queue(maxsize=3)

def sender():
    """メインスレッドからデータをキューに送信する関数"""
    for item in range(10):
        while True:
            try:
                message_queue.put(item, timeout=1)
                print(f'Main thread sent: {item}')
                time.sleep(1)  # キューが開くのを少し待つ
                break
            except queue.Full:
                print('Queue is full, waiting...')
                time.sleep(1)  # キューが満杯の場合、少し待ってから再試行

def receiver(name):
    """キューからデータを受信する子スレッド関数"""
    while True:
        try:
            # キューからデータを受信、1秒のタイムアウトを設定
            item = message_queue.get(timeout=10)
            print(f'{name} received: {item}')
        except queue.Empty:
            print(f'{name} did not receive any data for 10 seconds, exiting.')
            break

def main():
    # 3つの子スレッドを生成し、それぞれ異なる受信関数を割り当てる
    receivers = []
    for i in range(3):
        thread = threading.Thread(target=receiver, args=(f'Receiver {i+1}',))
        receivers.append(thread)
        thread.start()

    # データ送信を開始
    sender_thread = threading.Thread(target=sender)
    sender_thread.start()

    # すべての子スレッドの終了を待ち合わせる
    for thread in receivers:
        thread.join()

    # 送信スレッドの終了を待ち合わせる
    sender_thread.join()
    print("All threads have finished.")

if __name__ == "__main__":
    main()
