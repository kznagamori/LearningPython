# ファイル内グローバル変数と関数、ファイル外グローバル変数と関数

Pythonでファイル内外のグローバル変数と関数を使用する例を示します。この例では、2つのPythonファイルを用意し、それぞれのファイルでグローバル変数と関数を定義します。一方のファイルでは他方のファイルのグローバル変数と関数にアクセスします。

## プロジェクト構造
### `module_a.py`:
グローバル変数と関数を定義するファイルです。

### `module_b.py`:
`module_a` のグローバル変数と関数にアクセスするファイルです。

## `module_a.py`
このファイルでは、グローバル変数と関数を定義します。

```python
# module_a.py

# ファイル内グローバル変数
global_variable_a = "Hello from module_a"

# ファイル内関数
def print_message():
    print("This is a function inside module_a.")
```

## `module_b.py`
このファイルでは、`module_a` のグローバル変数と関数にアクセスし、別のグローバル変数を変更します。

```python
# module_b.py

import module_a

# ファイル外グローバル変数への読み書き
module_a.global_variable_a = "Modified in module_b"

def access_module_a():
    # module_aの関数と変数にアクセス
    module_a.print_message()
    print(module_a.global_variable_a)

    # 以下の行はエラーを引き起こします（コメントアウト）
    # print(global_variable_a)
    # このファイルでは、module_aのファイル内グローバル変数に直接アクセスできません。

def main():
    access_module_a()

if __name__ == "__main__":
    main()
```

## 実行方法
上記のコードで `module_a.py` と `module_b.py` を同じディレクトリに作成します。
`module_b.py` を実行すると、`module_a` の関数とグローバル変数にアクセスし、グローバル変数の値を変更します。
```bash
python module_b.py
```
このプログラムでは、`module_b` から `module_a` のグローバル変数と関数にアクセスしています。一方で、`module_a` のファイル内グローバル変数にはmodule_bから直接アクセスできません。これは、Pythonが名前空間を管理する方法によるものです。


