from taxi import Taxi


def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40km
    taxi.drive(40)

    # Print the taxi details and current fare
    print(taxi)  # calling taxi.__str__()
    print(f"Current fare: ${taxi.get_fare():.2f}")
    print()

    # Restart the meter (start a new fare) and then drive the car 100km
    taxi.start_fare()  # reset the current distance fare to 0
    print(f"Current fare: ${taxi.get_fare():.2f} before moving any new distance")
    distance_driven = taxi.drive(100)

    # Print the details and the current fare
    print(f"After attempting to drive another 100km. Actual distance travelled was {distance_driven}km")
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
