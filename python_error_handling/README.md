# 一般的なエラー処理

エラー処理はプログラムで予期しない問題が発生したときに対処するために重要です。Pythonでは `try`、`except` ブロックを使用してエラーを捕捉し、適切に処理します。以下のサンプルでは、関数内でエラーを発生させ、呼び出し側でそのエラーを捕捉して処理する方法を示します。

## サンプルプログラム
この例では、割り算を行う簡単な関数divideを定義し、0による割り算（ `ZeroDivisionError` ）や型不一致（ `TypeError` ）など、可能性のあるエラーを捕捉します。さらに、呼び出し側で関数からエラーが返された場合の処理も示します。

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Only numerical values are allowed."
    else:
        return result

def main():
    # 正常な呼び出し
    print(divide(10, 2))  # 5.0

    # 0による割り算を試みる
    print(divide(10, 0))  # Error: Division by zero is not allowed.

    # 型不一致を試みる
    print(divide("10", "2"))  # Error: Only numerical values are allowed.

    # try-exceptブロックを使用して呼び出し側でエラーを捕捉
    try:
        result = divide(10, 0)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

## 解説
`divide` 関数では、`try` ブロック内で割り算を試みます。
`except` ブロックで特定のエラー（ `ZeroDivisionError` 、`TypeError` ）を捕捉し、発生したエラーに応じたメッセージを返します。
`else` ブロックは、エラーが発生しなかった場合に割り算の結果を返します。
`main` 関数では、`divide` 関数を異なるパラメータで呼び出し、さまざまな状況での振る舞いを示します。また、エラーを呼び出し側で捕捉しようとする例は、このケースでは実際には `divide` 関数が文字列型のエラーメッセージを返しているため、`except` ブロックには到達しませんが、一般的なエラー処理の方法を示しています。
このサンプルプログラムは、Pythonでの一般的なエラー処理の方法と、関数内でのエラー処理と呼び出し側でのエラー捕捉の方法を示しています。
