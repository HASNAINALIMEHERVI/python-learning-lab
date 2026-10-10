"""Inheritance and super(), with fictional sample objects."""
from dataclasses import dataclass


@dataclass
class Device:
    name: str

    def describe(self):
        return f'Device: {self.name}'


class Sensor(Device):
    def __init__(self, name, unit):
        super().__init__(name)
        self.unit = unit

    def describe(self):
        return f'{super().describe()}; unit: {self.unit}'


if __name__ == '__main__':
    print(Sensor('Demo temperature sensor', 'Celsius').describe())
