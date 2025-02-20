class Vehicle:
    def __init__(self, brand='', model='', year=0, color=''):
        """Initialize commom attributes

        Args:
            brand (string): Vehicle brand
            model (string): Vehicle model
            year (int): Vehicle year of manufacture
            color (string): Vehicle color
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError('Brand cannot be empty.')
        self._brand = value.strip()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError('Model cannot be empty.')
        self._model = value.strip()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Year must be a positive value.')
        self._year = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not value.strip():
            raise ValueError('Color cannot be empty.')
        self._color = value.strip()

    def get_data(self):
        self.brand = input('Enter brand: ')
        print('-' * 80)
        self.model = input('Enter model: ')
        print('-' * 80)
        self.year = int(input('Enter year manufacture (Format: YYYY): '))
        print('-' * 80)
        self.color = input('Enter color: ')
        print('-' * 80)

    def show_data(self):
        print('=' * 80)
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Color: {self.color}')

    def vehicle_dict(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color
        }
        


class Car(Vehicle):
    def __init__(self, brand='', model='', year=0, color='', fuel_type=''):
        super().__init__(brand, model, year, color)
        self._fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        if not value.strip():
            raise ValueError('Fuel type cannot be empty.')
        self._fuel_type = value.strip()

    def get_data(self):
        super().get_data()
        self.fuel_type = input('Enter fuel type: ')
        print('=' * 80)
        print()

    def show_data(self):
        super().show_data()
        print(f'Fuel type: {self.fuel_type}')
        print('=' * 80)
        print()

    def car_dict(self):
        car_dict = super().vehicle_dict()
        car_dict['fuel_type'] = self.fuel_type
        return car_dict


class Motorcycle(Vehicle):
    def __init__(self, brand='', model='', year=0, color='', motorcycle_type=''):
        super().__init__(brand, model, year, color)
        self._motorcycle_type = motorcycle_type

    @property
    def motorcycle_type(self):
        return self._motorcycle_type

    @motorcycle_type.setter
    def motorcycle_type(self, value):
        if not value.strip():
            raise ValueError('Motorcycle type cannot be empty.')
        self._motorcycle_type = value.strip()

    def get_data(self):
        print('=' * 80)
        while True:
            try:
                self._motorcycle_type = input('Enter motorcycle type: ')
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    def show_data(self):
        print('=' * 80)
        super().show_data()
        print(f'Motorcycle type: {self._motorcycle_type}')
        print('=' * 80)
        print()


class Truck(Vehicle):
    def __init__(self, brand='', model='', year=0, color='', load_capacity=0):
        super().__init__(brand, model, year, color)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError('Load capacity must be a positive value.')
        self._load_capacity = value

    def get_data(self):
        super().get_data()

        print('=' * 80)
        while True:
            try:
                self._load_capacity = float(input('Enter load capacity: '))
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    def show_data(self):
        print('=' * 80)
        super().show_data()
        print(f'Load capacity: {self._load_capacity:.2f} kg')
        print('=' * 80)
        print()