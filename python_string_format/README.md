# 各型のstring formatの組み合わせ

Pythonの `str.format()` メソッドやフォーマット済み文字列リテラル（ `f-strings` ）を使用することで、様々なデータ型を文字列にフォーマットすることができます。以下にいくつかの一般的な例と、進数、浮動小数点数、科学技術記法などの表示形式を組み合わせたフォーマット方法を紹介します。

## 基本的な型の組み合わせ
```python
name = "Alice"
age = 30
height = 1.75

# 基本的な組み合わせ
print(f"Name: {name}, Age: {age}, Height: {height}")
```

## 各型の表示形式の組み合わせ
- 整数の進数表示: 10進数、2進数、16進数
- 浮動小数点数: 小数点以下の桁数制限、科学技術記法
- 文字列: 文字数制限

```python
number = 255

# 整数の進数表示
print(f"Decimal: {number}, Binary: {number:b}, Hexadecimal: {number:x}")

# 浮動小数点数の表示
value = 12345.6789
print(f"Fixed point: {value:.2f}, Scientific: {value:.2e}")

# 文字列の文字数制限
string = "Hello, World!"
print(f"Limited characters: {string:.5}")
```

## 0パディング、桁数制限、文字数制限、右詰め/左詰め
```python
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
```

これらの例は、Pythonで提供されているフォーマット指定子を使用して、さまざまなデータ型の値を文字列に組み込む方法を示しています。`str.format()` メソッドや `f-strings` を使うことで、出力のフォーマットを柔軟に制御することが可能です。


