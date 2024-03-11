# パッケージをインストールして使用する

PythonでGitHub上に公開し、`pip install` でインストール可能なパッケージを作成するためのサンプルプログラムと手順を以下に示します。この例ではパッケージ名を `hello_mypackage` とし、指定可能なバージョンを `1.0`、`1.1`、および `latest` とします。バージョンを指定しない場合、`latest` がインストールされるようにします。

## ステップ 1: パッケージの構造を作成
まずは、パッケージの基本的なディレクトリ構造を作成します。以下のような構造です。
```
hello_mypackage/
├── hello_mypackage/
│   ├── __init__.py
│   └── version.py
├── setup.py
└── README.md
```

- `hello_mypackage/`: 最上位のディレクトリで、この中にパッケージのコードが入ります。
  - `__init__.py`: パッケージを初期化するためのファイル。空でも構いませんが、ここにバージョン情報を出力する関数を記述します。
  - `version.py`: バージョン情報を定義するファイル。
- `setup.py`: パッケージのインストールや配布に必要な設定を記述します。
- `README.md`: パッケージの説明を記述するマークダウンファイル。

## ステップ 2: コードの記述
**hello_mypackage/hello_mypackage/init.py**
```python
from .version import version

def print_version():
    print(f"hello_mypackage version: {version}")

```

**hello_mypackage/hello_mypackage/version.py**

- バージョン1.0の場合：
```python
version = "1.0"
```

**setup.py**
```python
from setuptools import setup, find_packages

setup(
    name='hello_mypackage',
    version='1.0',  # パッケージのバージョン
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hello_mypackage = hello_mypackage:print_version',
        ],
    },
)
```

## ステップ 3: GitHubにプッシュ
1. GitHubにリポジトリを作成します（例: `hello_mypackage`）。
2. 作成したディレクトリ構造をリポジトリにプッシュします。


## ステップ 4: バージョンタグの付け方
GitHubでリリースを作成するときに、バージョンタグを付けます。ターミナルから以下のコマンドを実行します：

```bash
git tag -a v1.0 -m "version 1.0"
git push origin v1.0
```

この操作を各バージョンに対して繰り返します。


## ステップ 5: pipでのインストール
ユーザーは以下のコマンドを使用してパッケージをインストールできます。

**バージョンを指定してインストール：**
```bash
pip install git+https://github.com/<ユーザー名>/hello_mypackage.git@v1.0
```

**`latest`（最新バージョン）をインストール：**
```bash
pip install git+https://github.com/<ユーザー名>/hello_mypackage.git
```

GitHubで最新のタグを `latest` として管理することで、バージョンを指定しない場合に最新をインストールできるようにします。

