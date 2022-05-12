from silver_service_taxi import SilverServiceTaxi


def main():
    """Start of program to test class SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Luxury Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"Final fare of SilverServiceTaxi: ${taxi.get_fare()}")


if __name__ == '__main__':
    main()
