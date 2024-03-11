def create_hash_table():
    """新しいハッシュテーブルの作成"""
    return {}

def add_item(hash_table, key, value):
    """ハッシュテーブルにアイテムを追加"""
    hash_table[key] = value

def find_item(hash_table, key):
    """キーを使用してハッシュテーブルからアイテムを検索"""
    return hash_table.get(key, "Not found")

def remove_item(hash_table, key):
    """ハッシュテーブルからアイテムを削除"""
    if key in hash_table:
        del hash_table[key]
        return True
    else:
        return False

def display_hash_table(hash_table):
    """ハッシュテーブルの内容を表示"""
    for key, value in hash_table.items():
        print(f"{key}: {value}")

def main():
    # ハッシュテーブルの作成
    my_hash_table = create_hash_table()

    # アイテムの追加
    add_item(my_hash_table, "key1", "value1")
    add_item(my_hash_table, "key2", "value2")
    add_item(my_hash_table, "key3", "value3")

    # ハッシュテーブルの表示
    print("Hash table contents:")
    display_hash_table(my_hash_table)

    # アイテムの検索
    print("\nSearching for 'key2':", find_item(my_hash_table, "key2"))
    print("Searching for 'key4':", find_item(my_hash_table, "key4"))

    # アイテムの削除
    if remove_item(my_hash_table, "key2"):
        print("\n'key2' removed successfully.")
    else:
        print("\n'key2' not found.")

    # 削除後のハッシュテーブルの表示
    print("Hash table after deletion:")
    display_hash_table(my_hash_table)

if __name__ == "__main__":
    main()
