import os
from packs.classes import Vehicle, Car, Motorcycle, Truck


from exercises.activity_002.packs.menu import cls_term, title
from packs.classes import Vehicle, Car, Motorcycle, Truck


def menu():
    while True:
        cls_term()
        title()
        print('=' * 80)
        print('Menu:'.center(80))
        print('=' * 80)
        print('1. Register vehicle.')
        print('2. Modify register.')
        print('3. Delete register.')
        print('4. Show registers.')
        print('5. Exit.')
        print('-' * 80)

        option = input('Choose option (1-5): ')

        if option.isdigit():
            option = int(option)

            if option in [1, 2, 3, 4]:
                cls_term()
                print('=' * 80)
                print()
                especify_menu()
            elif option == 5:
                print('=' * 80)
                print()
                print('=' * 80)
                print('Shutting down system.')
                print('=' * 80)
                print()
                break
            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def especify_menu():
    while True:
        print('=' * 80)
        print('Especify Menu:'.center(80))
        print('=' * 80)
        print('1. Car.')
        print('2. Motorcycle.')
        print('3. Truck.')
        print('4. Back.')
        print('-' * 80)

        option = input('Choose option (1-4): ').strip()

        if option.isdigit():
            option = int(option)

            if option == 1:
                print('=' * 80)
                print()
                print('=' * 80)
                register_car()
                print()
                print('=' * 80)
                while True:
                    try_again = input(
                        'Continue register (y/n): '
                    ).strip().lower()

                    if try_again == 'n':
                        return
                    elif try_again == 'y':
                        cls_term()
                        title()
                        continue
                    else:
                        print('-' * 80)
                        input('Invalid option. Press enter to try again: ')
                        print('-' * 80)

            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                return
            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def register_car():
    car_dict = get_car_dict()
    car = Car(
        car_dict['brand'],
        car_dict['model'],
        car_dict['year'],
        car_dict['color'],
        car_dict['fuel_type']
    )

    print('=' * 80)
    print('Car registered successfully.')

    show_car_dict(car_dict)
    return car


def get_vehicle_data():
    """Iterate Method - Get vehicle commom data
    """
    vehicle_dict = {}
    vehicle = Vehicle()
    while True:
        try:
            brand = input('Enter brand: ')
            vehicle_dict[vehicle.brand] = brand
            break

        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            model = input('Enter model: ')
            vehicle_dict[vehicle.model] = model
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            year = int(
                input('Enter year manufacture (Format: YYYY): '))
            vehicle_dict[vehicle.year] = year
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            color = input('Enter color: ')
            vehicle_dict[vehicle.color] = color
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    return vehicle_dict


def get_car_dict():
    car_dict = get_vehicle_data()
    car = Car()
    print('-' * 80)
    while True:
        try:
            car_dict[car.fuel_type] = input('Enter fuel type: ')
            print('=' * 80)
            print()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    return car_dict


def show_car_dict(car_dict):
    print('=' * 80)
    print(f'Brand: {car_dict["brand"]}')
    print(f'Model: {car_dict["model"]}')
    print(f'Year: {car_dict["year"]}')
    print(f'Color: {car_dict["color"]}')
    print(f'Fuel Type: {car_dict["fuel_type"]}')
    print('=' * 80)


def get_vehicle_data():
    """Iterate Method - Get vehicle commom data
    """
    vehicle = Vehicle()
    while True:
        try:
            brand = input('Enter brand: ')
            vehicle.brand = brand
            break

        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            model = input('Enter model: ')
            vehicle.model = model
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            year = int(
                input('Enter year manufacture (Format: YYYY): '))
            vehicle.year = year
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            color = input('Enter color: ')
            vehicle.color = color
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    return {
        'brand': brand,
        'model': model,
        'year': year,
        'color': color
    }


def show_car_data(vehicle_dict):
    print('=' * 80)
    print(f'Brand: {vehicle_dict["brand"]}')
    print(f'Model: {vehicle_dict["model"]}')
    print(f'Year: {vehicle_dict["year"]}')
    print(f'Color: {vehicle_dict["color"]}')

def get_car_data():
    get_vehicle_data()
    car = Car()
    print('-' * 80)
    while True:
        try:
            fuel_type = input('Enter fuel type: ')
            car.fuel_type = fuel_type
            print('=' * 80)
            print()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)


def show_car_data(car_dict):
    show_car_data()
    print(f'Fuel Type: {car_dict["fuel_type"]}')
    print('=' * 80)




def get_car_data():
    """Iterate Method - Get vehicle commom data
    """
    car = Car()
    while True:
        try:
            brand = input('Enter brand: ')
            car.brand = brand
            break

        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            model = input('Enter model: ')
            car.model = model
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            year = int(
                input('Enter year manufacture (Format: YYYY): '))
            car.year = year
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            color = input('Enter color: ')
            car.color = color
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('-' * 80)
    while True:
        try:
            fuel_type = input('Enter fuel type: ')
            car.fuel_type = fuel_type
            print('=' * 80)
            print()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    return {
        'brand': brand,
        'model': model,
        'year': year,
        'color': color,
        'fuel_type': fuel_type
    }


def show_car_data(car_dict):
    print('=' * 80)
    print(f'Brand: {car_dict["brand"]}')
    print(f'Model: {car_dict["model"]}')
    print(f'Year: {car_dict["year"]}')
    print(f'Color: {car_dict["color"]}')
    print(f'Fuel Type: {car_dict["fuel_type"]}')
    print('=' * 80)