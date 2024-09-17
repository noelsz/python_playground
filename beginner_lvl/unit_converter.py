class UnitConverter:
    def __init__(self):
        self.length_units = {
            'mm': 0.001,    # millimeters
            'cm': 0.01,     # centimeters
            'm': 1,         # meters
            'km': 1000,     # kilometres
            'in': 0.0254,   # inches
            'ft': 0.3048,   # feet
            'yd': 0.9144    # yards
        }
        self.weight_units = {
            'mg': 0.001,    # milligrams
            'g': 1,         # grams
            'kg': 1000,     # kilograms
            'oz': 28.3495,  # ounces
            'lb': 453.592   # pounds
        }
        self.temperature_units = {
            'C': lambda x: x,               # Celsius
            'F': lambda x: x * 9 / 5 + 32,  # Fahrenheit
            'K': lambda x: x + 273.15       # Kelvin
        }
        self.volume_units = {
            'ml': 0.001,
            'l': 1,
            'm3': 1000,
            'cm3': 0.001,
            'gallon': 3.785,
        }

    def convert_length(self, value, from_unit, to_unit):
        if from_unit not in self.length_units:
            raise ValueError(f"The unit you want to convert from is not available. ({from_unit})")
        if to_unit not in self.length_units:
            raise ValueError(f"The unit you want to convert to is not available. ({to_unit})")
        return str(value * self.length_units[from_unit] / self.length_units[to_unit]) + " " + to_unit

    def convert_weight(self, value, from_unit, to_unit):
        if from_unit not in self.weight_units:
            raise ValueError(f"The unit you want to convert from is not available. ({from_unit})")
        if to_unit not in self.weight_units:
            raise ValueError(f"The unit you want to convert to is not available. ({to_unit})")
        return str(value * self.weight_units[from_unit] / self.weight_units[to_unit]) + " " + to_unit

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit not in self.temperature_units:
            raise ValueError(f"The unit you want to convert from is not available. ({from_unit})")
        if to_unit not in self.temperature_units:
            raise ValueError(f"The unit you want to convert to is not available. ({to_unit})")
        return str(self.temperature_units[to_unit](self.temperature_units[from_unit](value))) + " " + to_unit

    def convert_volume(self, value, from_unit, to_unit):
        if from_unit not in self.volume_units:
            raise ValueError(f"The unit you want to convert from is not available. ({from_unit})")
        if to_unit not in self.volume_units:
            raise ValueError(f"The unit you want to convert to is not available. ({to_unit})")
        return str(value * self.volume_units[from_unit] / self.volume_units[to_unit]) + " " + to_unit

# Usage:
converter = UnitConverter()

# Available units:
# Length: mm, cm, m, km, ft, yd, in
# Weight: mg, g, kg, oz, lb
# Temperature: C, F, K
# Volume: ml, l, m3, cm3, gallon

print(converter.convert_length(100, 'm', 'mm'))
print(converter.convert_weight(10, 'kg', 'lb'))
print(converter.convert_temperature(40, 'C', 'F'))
print(converter.convert_volume(50, 'l', 'gallon'))