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

