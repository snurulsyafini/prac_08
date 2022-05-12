from unreliable_car import UnreliableCar


def main():
    """Start of program"""
    trusty_car = UnreliableCar("Dependable", 100, 70)
    dodgy_car = UnreliableCar("Unreliable", 100, 7)

    # run cars 10 times to see differences and display distance driven
    count = 0
    for i in range(1, 11):
        count += 1
        print(f"Driving session {count}: {i}km")
        print(f"{trusty_car.name} has driven {trusty_car.drive(i)}km")
        print(f"{dodgy_car.name} has driven {dodgy_car.drive(i)}km")
    print()

    print(f"Final results: {trusty_car}\n{dodgy_car}")


if __name__ == '__main__':
    main()
