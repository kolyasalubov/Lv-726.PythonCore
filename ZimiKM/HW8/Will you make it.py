def zero_fueel(distance_to_pump, mpg, fuel_left) -> bool:
    '''
    Calculation of the distance traveled by the car
     on the remaining fuel

    Parameters: 
    distance_to_pump - user input distance to pump
    mpg - average fuel consumption
    fuel_left - remainig fuel in tank

    Result:
    return bool value True if if the car reaches 
    the gas station on the remaining fuel
     or Falce in otherwise
     '''

    return (mpg * fuel_left) >= distance_to_pump

print(zero_fueel(50, 20, 10))
