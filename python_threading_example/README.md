# スレッド

Pythonでスレッドを使用する際、`threading` モジュールがよく利用されます。以下のサンプルプログラムは、複数のスレッドを起動し、それらが終了するまでメインスレッドが待機する方法を示しています。各スレッドで実行される作業は、あらかじめ定義された関数によって行われます。

## サンプルプログラム
```python
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

```

このプログラムでは、`thread_function` はスレッドで実行される関数です。この関数は単にスレッドの開始と終了を表示し、`time.sleep(2)` を使って模擬的な作業を2秒間行います。`main` 関数では、3つのスレッドを生成し、それぞれに `thread_function` を実行させます。各スレッドは `threading.Thread` オブジェクトの生成時に指定された関数を実行します。

`thread.start()` メソッドを呼び出してスレッドを開始した後、メインスレッドは生成した全スレッドの終了を待つために `thread.join()` を呼び出します。`join()` メソッドを使うことで、メインスレッドはすべてのスレッドが完了するまで待機します。

最後に、すべてのスレッドが終了したことを確認したら、"All threads have finished." が出力されます。これにより、メインスレッドが複数のワーカースレッドを管理し、その完了を同期的に待つ基本的な方法を示すことができます。
