# 複数ファイルを機能ごとにパッケージを分けて使用する

Pythonで機能ごとにパッケージを分けて使用する際には、複数のプロジェクトやディレクトリを作成して、一方をライブラリとして、もう一方でそのライブラリを呼び出す形をとります。以下にその手順とサンプルプログラムを示します。

## プロジェクト構造
### ライブラリプロジェクト（mylibrary）: 
これは再利用可能なコードを含むパッケージです。

```
python_multi_pack_file/
│
└──mylibrary/
    │
    ├── mylibrary/
    │   ├── __init__.py
    │   └── operations.py
    └── setup.py
```

### メインプロジェクト（myapplication）:
このプロジェクトではmylibraryを使用します。

```
python_multi_pack_file/
│
└myapplication
     │
     └── main.py
```


## ライブラリプロジェクトの作成
### `operations.py` の作成:
`mylibrary/mylibrary/operations.py` に簡単な関数を作成します。

```python
# mylibrary/mylibrary/operations.py

def add(a, b):
    return a + b
```

### `__init__.py`の作成:
このファイルはディレクトリをPythonパッケージとして扱うために必要です。

```python
# mylibrary/mylibrary/__init__.py

from .operations import add
```

### `setup.py`の作成:
このファイルはパッケージのセットアップと配布を管理します。

```python
# mylibrary/setup.py

from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages()
)
```

### ライブラリのビルドとインストール:
`mylibrary`ディレクトリで以下のコマンドを実行します。

```bash
python setup.py develop
```

これにより、ライブラリが開発モードでインストールされ、変更をリアルタイムで反映できるようになります。

## メインプロジェクトの作成
### `main.py`の作成:
`myapplication/main.py` で `mylibrary` を使用します。

```python
# myapplication/main.py

from mylibrary import add

def main():
    result = add(5, 3)
    print(f"The result is {result}")

if __name__ == "__main__":
    main()
```

## プログラムの実行
`myapplication` ディレクトリで以下のコマンドを実行します。

```bash
python main.py
```

この構造では、`mylibrary` は独立したプロジェクトとして機能し、他のプロジェクトで再利用できるコードを含んでいます。`myapplication` はこのライブラリを使用し、特定の操作（この場合は加算）を実行します。この方法は、コードの再利用性と整理を向上させるのに役立ちます。
