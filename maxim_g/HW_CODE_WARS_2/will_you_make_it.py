def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (mpg * fuel_left) >= distance_to_pump


result = zero_fuel(distance_to_pump=50, mpg=25, fuel_left=2)
print(result)