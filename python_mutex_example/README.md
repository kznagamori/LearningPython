# 排他処理

Pythonで複数のスレッド間で排他制御（ `mutual exclusion` ）を行うには、`threading` モジュールの `Lock` クラスを使用します。`Lock` オブジェクトを使用して、同時に1つのスレッドのみが特定のセクションのコードを実行できるように制限します。これにより、共有リソースへの同時アクセスを防ぎ、データの整合性を保ちます。

以下のサンプルプログラムは、`Lock` を使用して、複数のスレッドが共有リソースへ安全にアクセスする方法を示しています。

## サンプルプログラム
```python
import threading

# 共有リソース
shared_resource = 0
# ミューテックス（排他制御のためのロック）
lock = threading.Lock()

def thread_task():
    """スレッドが実行するタスク"""
    global shared_resource
    for _ in range(100000):
        lock.acquire()  # ロックを取得（排他制御開始）
        try:
            # ここで共有リソースに対する操作を行う
            shared_resource += 1
        finally:
            lock.release()  # ロックを解放（排他制御終了）

def main():
    threads = []

    # 2つのスレッドを生成して実行
    for _ in range(2):
        thread = threading.Thread(target=thread_task)
        threads.append(thread)
        thread.start()

    # すべてのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

    # 共有リソースの最終状態を表示
    print("Shared resource value:", shared_resource)

if __name__ == "__main__":
    main()

```

このプログラムでは、`shared_resource` が共有リソースとして機能します。複数のスレッド（この例では2つ）が `thread_task` 関数を実行します。この関数内で、各スレッドは100,000回、共有リソースの値を1ずつ増やそうと試みます。`lock.acquire()` を呼び出すことで、各スレッドは共有リソースへのアクセス前にロックを取得します。これにより、同時に1つのスレッドのみがリソースを変更できます。操作が完了したら、`lock.release()` を使ってロックを解放し、他のスレッドがアクセスできるようにします。

`main` 関数では、すべてのスレッドが終了するのを待ってから、共有リソースの最終状態を表示します。このプログラムを実行すると、`shared_resource` の値が正確に200,000になることを期待できます。これは、ミューテックスを使用して共有リソースへのアクセスを正しく制御した結果です。
