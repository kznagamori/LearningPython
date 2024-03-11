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
