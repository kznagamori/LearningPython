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
