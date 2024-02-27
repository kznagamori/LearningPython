# クラスの継承を実現する

Pythonでクラスの継承を扱う際、基本クラス（親クラス）の属性やメソッドを派生クラス（子クラス）が引き継ぐことができます。継承を使用することで、コードの再利用性を高め、より効率的なプログラムの開発が可能になります。

以下のサンプルプログラムでは、`Vehicle` クラスを基本クラスとして定義し、`Car` クラスがこれを継承します。継承した `Car` クラスには、独自のメソッドを追加しています。

## サンプルプログラム
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle_info(self):
        print(f"Vehicle Info: {self.brand} {self.model}")

class Car(Vehicle):  # Vehicleクラスを継承
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)  # 親クラスのコンストラクタを呼び出す
        self.horsepower = horsepower

    def display_car_info(self):
        print(f"Car Info: {self.brand} {self.model}, Horsepower: {self.horsepower}")

def main():
    # Vehicleのインスタンスを作成
    my_vehicle = Vehicle("Toyota", "Corolla")
    my_vehicle.display_vehicle_info()

    # Carのインスタンスを作成
    my_car = Car("Nissan", "Skyline", 320)
    my_car.display_vehicle_info()  # 継承したメソッドを使用
    my_car.display_car_info()  # Carクラス固有のメソッドを使用

if __name__ == "__main__":
    main()
```

このプログラムでは、`Vehicle` クラスはブランド名とモデル名を属性として持ち、これらの情報を表示するメソッドを持っています。`Car` クラスは `Vehicle` からこれらの属性とメソッドを継承し、追加で馬力（ `horsepower` ）の属性と、その情報を表示する独自のメソッドを持っています。

`main` 関数内で、まず `Vehicle` クラスのインスタンスを作成し、その情報を表示します。次に、Carクラスのインスタンスを作成し、継承したメソッドと、`Car` クラス固有のメソッドを使用して情報を表示します。これにより、Pythonのクラス継承の基本的な使い方を示しています。

