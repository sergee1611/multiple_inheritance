class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self, hor_pow):
        print(f'Мощность: {hor_pow} л.с')


class Nissan(Car, Vehicle):
    price = 1100000
    vehicle_type = 'SUV'

    def horse_powers(self, hor_pow):
        super().horse_powers(hor_pow=hor_pow)


nissan = Nissan()
print(nissan.__class__.__name__, nissan.vehicle_type, nissan.price)
nissan.horse_powers(150)
