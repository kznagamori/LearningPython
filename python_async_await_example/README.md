# Async/Await

Pythonでは、`asyncio` ライブラリを使用して非同期プログラミングを実装できます。`async` 宣言された関数（コルーチン）と `await` キーワードを使って、非同期に実行されるタスクを簡単に管理できます。以下のサンプルプログラムは、非同期関数の実装と使用方法を示しています。この例では、非同期に実行される2つの関数を作成し、それらが完了するのを待っています。

## サンプルプログラム
```python
import asyncio

async def async_task(name, delay):
    """非同期タスクを模倣する関数"""
    print(f"Task {name}: starting with delay {delay}")
    await asyncio.sleep(delay)
    print(f"Task {name}: completed after {delay} seconds")
    return f"Task {name} result"

async def main():
    # 非同期タスクを同時に実行
    task1 = asyncio.create_task(async_task("One", 2))
    task2 = asyncio.create_task(async_task("Two", 3))

    # 各タスクの結果を待つ
    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)

    # さらに非同期処理をここに追加できる

# Python 3.7以上では、asyncio.run() を使用してメイン関数を実行
if __name__ == "__main__":
    asyncio.run(main())

```

このプログラムでは、`async_task` という非同期関数を定義しています。この関数は、指定された秒数 `delay` だけ処理を一時停止します（非ブロッキングの `await asyncio.sleep(delay)` を使用）。`main` 関数内では、`asyncio.create_task()` を使用してこの関数の2つのインスタンスを非同期に実行し、`await` を使用して各タスクの結果を待ちます。この方法により、複数の非同期タスクが並行して実行され、完了次第その結果を取得できます。

`asyncio.run(main())` は、`main` コルーチンを実行し、プログラムのエントリーポイントとして機能します。これにより、非同期プログラミングのパワーを簡単に活用し、Pythonで効率的な非同期IO操作を実現できます。

