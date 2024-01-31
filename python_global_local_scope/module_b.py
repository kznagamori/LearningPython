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
