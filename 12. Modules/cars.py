# Parent Class
class Car:
    """A representation of a car"""
    
    def __init__(self, make, model, year):
        """Initialize the attributes of a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Shows the value on the odometer."""
        reading = f"The car has {self.odometer:,} kms on it." #! Thousand separator!
        return reading
    
    def update_odometer(self, mileage):
        """Updates the odometer with the given mileage"""
        if mileage >= self.odometer:
            self.odometer = mileage
            return "Mileage updated."
        else:
            return "You cannot roll back an odometer!"
        
    def increment_odometer(self, kms):
        """Increments the odometer by the given number of kms."""
        if kms > 0:
            self.odometer += kms
        else:
            return "You cannot roll back an odometer!"
        
    def fill_gas_tank(self):
        """Fills the gas tank by the given amount of liters"""
        return "Tank filled"
        

def function_outside_class():
    return "function_outside_class"

def another_function():
    return "another_function"