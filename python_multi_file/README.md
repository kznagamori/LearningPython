# 複数ファイルを使用する

Pythonで複数のファイルを使用してプログラムを構成する場合、プログラムをモジュールに分割し、これらのモジュールをインポートして使用することが一般的です。以下に簡単な例を示します。

## プロジェクト構造
この例では、次のようなファイル構造を持つプロジェクトを考えます。

```css
python_multi_file/
│
├── main.py
└── utils/
    └── helper.py
```

## 各ファイルの内容
### `helper.py:`
このファイルは `utils` ディレクトリ内にあり、単純なヘルパー関数を含んでいます。

```python
# utils/helper.py

def greet(name):
    return f"Hello, {name}!"
```
### `main.py:`
 このファイルはプログラムのエントリーポイントです。`helper.py` から`greet` 関数をインポートして使用します。

```python
# main.py

from utils.helper import greet

def main():
    print(greet("Alice"))

if __name__ == "__main__":
    main()
```

## プログラムの実行
このプログラムを実行するには、`main.py` があるディレクトリで以下のコマンドを実行します。

```bash
python main.py
```
このコマンドを実行すると、`main.py` が `utils/helper.py` から `greet` 関数をインポートし、"Hello, Alice!"と出力します。

**注意点**
モジュールのインポートは、Pythonのパッケージ構造に従います。この例では、`utils` ディレクトリはパッケージとして扱われ、`helper.py` はそのサブモジュールです。
複雑なプロジェクトでは、各モジュールが特定の機能やロジックを担当し、これによってコードの保守性と再利用性が向上します。




