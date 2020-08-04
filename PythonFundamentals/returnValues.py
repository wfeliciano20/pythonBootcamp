
def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    return mpg


def car_name(car_to_calculate):
    name = f'{car_to_calculate["make"]} {car_to_calculate["model"]}'
    return name


def car_info(car):
    mpg = calculate_mpg(car)
    name = car_name(car)
    return (f"{name} does {mpg} miles per gallon.")


car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
}

print(car_info(car))
