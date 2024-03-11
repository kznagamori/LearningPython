# メッセージキュー

Pythonの `queue.Queue` を使用して、複数のスレッド間でメッセージキューを介したデータ共有を行うサンプルプログラムを作成します。このプログラムでは、メインスレッドがキューにデータを送信し、3つの子スレッドがキューからデータを受信します。キューは最大3つのアイテムを保持でき、子スレッドは1秒ごとにデータを受信しようと試み、10秒間データを受信しなければ終了します。

## サンプルプログラム
```python
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
```

このサンプルプログラムでは、`sender` 関数がメインスレッドで実行され、合計10個のデータをキューに送信します。`receiver` 関数は子スレッドで実行され、キューからデータを受信します。各子スレッドは1秒に1回データを受信しようと試み、10秒間データを受信しなければ自動的に終了します。

メインスレッドは、`sender` 関数を別のスレッドで実行し、同時に3つの子スレッドを起動します。これらのスレッドは、キューが空になるまでデータを受信し続け、10秒間データがない場合に終了します。プログラムは、すべての子スレッドと送信スレッドが終了した後に完了します。
