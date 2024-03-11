# LearningPython
Python学習用レポジトリ

## Pythonとは
Pythonは、そのシンプルさと読みやすさから非常に人気のある高水準のプログラミング言語です。Guido van Rossumによって1989年に開発が始まり、1991年に公開されました。Pythonは、コードの簡潔さと表現力の豊かさを重視し、初心者からプロフェッショナルまで幅広い開発者に支持されています。以下にPython言語の主要な特徴を挙げます：

### Pythonとは の特徴

1. 簡潔で読みやすい構文：Pythonの構文は、他の多くのプログラミング言語よりもはるかに読みやすく、学習しやすいです。これにより、プログラミングの初心者がコードを理解しやすくなります。

2. 高い汎用性：Pythonは、ウェブ開発、データ分析、機械学習、人工知能、科学計算、データベースアクセス、デスクトップGUI、ネットワークプログラミングなど、幅広いアプリケーションに使用されます。

3. 豊富なライブラリとフレームワーク：Pythonには、特定のタスクを簡単に実行するための広範な標準ライブラリとサードパーティ製ライブラリがあります。DjangoやFlaskなどのウェブフレームワーク、PandasやNumPy、SciPy、Matplotlibなどのデータサイエンスと機械学習ライブラリが特に有名です。

4. インタプリタ型言語：Pythonはインタプリタ型言語であり、コードを書いてすぐに実行できるため、開発プロセスが迅速に進みます。この特性は、プロトタイピングや迅速なアプリケーション開発に特に有利です。

5. 動的型付け：Pythonは動的型付け言語であり、変数の型を宣言せずに使用できます。これにより、コードがより柔軟になりますが、型関連のエラーを引き起こす可能性もあります。

6. 拡張性：PythonはCやC++など他の言語で書かれたコードを統合することができ、パフォーマンスが重要な部分の高速化や、既存のライブラリやシステムとの連携が可能です。

7. ポータブル性：Pythonは多くのオペレーティングシステムで動作し、クロスプラットフォームのアプリケーション開発をサポートしています。

Pythonは、その多用途性、簡潔な構文、強力なライブラリのエコシステムにより、科学研究、ウェブ開発、データ分析、教育、スタートアップ企業など多岐にわたる分野で使用されています。また、機械学習とデータサイエンスの分野での主要言語としての地位を確立しています。


### 推しポイント
- 学習コストが低い。
- 使用可能なパッケージが多く存在するので、ツールを作成しやすい。
- ネットや本での参考文献が多い
- ChatGPTで質問すると、かなり正解に近いコードを取得できる。

### いまいち、ダメなポイント
- スクリプト言語なので配布が難しい
- スクリプト言語なので実行して処理されるまで正しく動作するのかが分からない
- ブロックがインデントで定義するので、ブロックの開始・終端の判別が難しい
- エコシステムのパッケージのインストールでgithubなどのレポジトリが使用できない。
- GUIアプリは作れるけど微妙

## 基礎
- [プロジェクト作成からビルドまでの手順](./python_start_project/README.md)
- [外部パッケージを使用したプログラムを作成する手順](./python_use_package/README.md)
- [複数ファイルを使用する](./python_multi_file/README.md)
- [複数ファイルを機能ごとにパッケージを分けて使用する](./python_multi_pack_file/README.md)
- [ファイル内グローバル変数と関数、ファイル外グローバル変数と関数](./python_global_local_scope/README.md)
- [クラスを使う](./python_class_methods/README.md)
- [パブリックなクラスのメンバ、メソッドを定義とプライベートなクラスのメンバ、メソッドを定義する](./python_public_private/README.md)
- [クラスの継承を実現する](./python_inherit_class/README.md)
- [クラスのインタフェースを使用したポリモーフィズムの実現](./python_poly_class/README.md)
- [クラスのプロパティを定義、使用](./python_class_property/README.md)
- [一般的なエラー処理](./python_error_handling/README.md)
- [各型のstring formatの組み合わせ](./python_string_format/README.md)
- [ジェネリック機能](./python_generics_example/README.md)
- [ラムダ式](./python_lambda_example/README.md)
- [LINQ機能](./python_linq_example/README.md)

## アルゴリズムとデータ構造
- [リンクドリスト構造](./python_linked_list/README.md)
- [リングバッファ構造](./python_ring_buffer/README.md)
- [キュー構造](./python_data_queue/README.md)
- [スタック構造](./python_data_stack/README.md)
- [二分木構造](./python_binary_tree/README.md)
- [平衡二分木構造](./python_balanced_tree/README.md)
- [ハッシュテーブル](./python_hash_table/README.md)
- [クイックソート](./python_quick_sort/README.md)
- [再帰を使用しないシェルソート](./python_non_recursive_shell_sort/README.md)

## 応用
- [リングバッファ](./python_ring_buffer_package/README.md)
- [キュー](./python_queue_package/README.md)
- [ハッシュテーブル](./python_hash_table_package/README.md)
- [ソート](./python_sort_package/README.md)
- [スレッド](./python_threading_example/README.md)
- [Async/Await](./python_async_await_example/README.md)
- [排他処理](./python_mutex_example/README.md)
- [メッセージボックス](./python_message_box_example/README.md)
- [メッセージキュー](./python_message_queue_example/README.md)

## エコシステム
- [パッケージをインストールして使用する](./python_install_package/README.md)

## 言語特性

