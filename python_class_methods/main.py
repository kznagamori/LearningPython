class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def describe_car(self):
        print(f"This car is a {self.color} {self.model}.")

    def drive(self):
        print(f"The {self.model} is now driving.")

def main():
    # Carクラスのインスタンスを作成
    my_car = Car("Toyota Corolla", "blue")

    # 車に関する情報を出力
    my_car.describe_car()

    # 車を「走行」させる
    my_car.drive()

if __name__ == "__main__":
    main()

