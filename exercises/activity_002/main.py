# STUDENT: BRUNO C. RODGERS
# DATE: 18/02/2025

# Vehicle Register System

# º Vehicles Super Class:
# - Car;
# - Motorcycle;
# - Truck.

# º Commom Attributes:
# + Brand;
# + Model;
# + Year;
# + Color.

# º Commom Method:
# - show_data()

# º Subclasses:
# - Car:
# + Fuel type.
# - Motorcycle:
# + Motorcycle type.
# - Truck:
# + Load capacity.

from packs.print import cls_term, title
from packs.iterate import menu


def main():
    cls_term()
    title()
    menu()


if __name__ == '__main__':
    main()