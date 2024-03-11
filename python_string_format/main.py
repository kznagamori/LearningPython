def main():
    name = "Alice"
    age = 30
    height = 1.75

    # 基本的な組み合わせ
    print(f"Name: {name}, Age: {age}, Height: {height}")

    number = 255

    # 整数の進数表示
    print(f"Decimal: {number}, Binary: {number:b}, Hexadecimal: {number:x}")

    # 浮動小数点数の表示
    value = 12345.6789
    print(f"Fixed point: {value:.2f}, Scientific: {value:.2e}")

    # 文字列の文字数制限
    string = "Hello, World!"
    print(f"Limited characters: {string:.5}")

    # 0パディングあり
    print(f"Zero padding: {number:08d}")

    # 桁数制限
    print(f"Digits limited: {value:.3f}")

    # 文字数制限と右詰め/左詰め
    # 左詰め
    print(f"Left aligned: {string:<20}")
    # 右詰め
    print(f"Right aligned: {string:>20}")
    # 中央揃え
    print(f"Center aligned: {string:^20}")

    # 0パディングと整数の桁数制限
    print(f"Zero padded number: {number:010d}")

    # 浮動小数点数で0パディング
    print(f"Floating point zero padded: {value:010.2f}")

if __name__ == "__main__":
    main()
