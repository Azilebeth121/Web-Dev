from Models import Vehicle, Car, Motorcycle


def main():
    vehicle1 = Vehicle("Generic", "Truck", 2015)
    car1 = Car("Toyota", "Camry", 2022, 4)
    bike1 = Motorcycle("Yamaha", "R1", 2021, 1000)

    vehicles = [vehicle1, car1, bike1]

    for v in vehicles:
        print(v)
        print(v.start_engine())
        print(v.move())  
        print(v.stop_engine())
        print("-" * 40)

    print(car1.honk())
    print(bike1.wheelie())


if __name__ == "__main__":
    main()