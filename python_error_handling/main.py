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
