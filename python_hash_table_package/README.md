# ハッシュテーブル

Pythonでハッシュテーブルを使用する際、最も一般的な方法は辞書型( `dict` )を利用することです。`dict` は内部的にハッシュテーブルを使用しており、キーと値のペアを効率的に格納・検索することができます。ここでは、`dict` を使ってハッシュテーブルの基本的な操作を行うサンプルプログラムを提供します。このプログラムでは、要素の追加、要素の検索、要素の削除、およびハッシュテーブルの内容の表示を行います。

##　サンプルプログラム
```python
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
```

このプログラムは、Pythonの `dict` を使用して基本的なハッシュテーブルの操作を実行します。`create_hash_table` 関数で新しいハッシュテーブル（辞書）を作成し、`add_item` でアイテムを追加します。`find_item` 関数は、指定されたキーが存在する場合はその値を、存在しない場合はデフォルトのメッセージを返します。`remove_item` 関数は、指定されたキーのアイテムを削除し、`display_hash_table` 関数はハッシュテーブルのすべてのアイテムを表示します。


