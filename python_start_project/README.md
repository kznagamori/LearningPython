# プロジェクト作成からビルドまでの手順

Pythonでコマンドラインプログラムを作成し、ビルドするための基本的な手順は以下の通りです。

## 1. プロジェクトのセットアップ

### 1.1. プロジェクトディレクトリの作成:
プロジェクト用の新しいディレクトリを作成します。

```bash
mkdir python_start_project
cd python_start_project
```
### 1.2. 仮想環境のセットアップ（オプション）: 
Pythonの仮想環境を作成し、アクティベートします。

#### Windows
```powershell
python -m venv venv --without-pip
venv\Scripts\Activate
python -m ensurepip --upgrade --default-pip
python -m pip install --upgrade pip
```

#### Linux
```bash
python -m venv venv --without-pip
source venv/bin/activate
python -m ensurepip --upgrade --default-pip
python -m pip install --upgrade pip
```
以後、プロジェクトを使用する場合は仮想環境の `Activate` を行う必要があります。

### 1.3. 必要なライブラリのインストール: 
必要な場合、ライブラリをインストールします。例えば、`requests` や `numpy` など。

```bash
pip install requests
```

## 2. プログラムの作成
### 2.1. プログラムファイルの作成: 
例えば、`main.py` という名前のファイルを作成します。

### 2.2. プログラムの記述: 
コマンドライン引数を処理するために `argparse` などを使用することができます。

## 3. プログラムの実行
### 3.1. コマンドラインからプログラムの実行:

```bash
python main.py
```

## サンプルプログラム
以下は単純なコマンドラインプログラムの例です。このプログラムはコマンドライン引数を受け取り、それを出力します。

### `main.py:`

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Python CLI Program")
    parser.add_argument('name', help='Your name')
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
```
このプログラムを実行するには、コマンドラインで以下のように入力します。

```bash
python main.py [Your Name]
```

例えば、`python main.py Alice`と入力すると、`Hello, Alice!`と出力されます。
