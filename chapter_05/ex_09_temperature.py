def temperatures(temper_fahr: float):
    """Calculate the Celsius equivalent and the Kelvin equivalent 
    and display all three temperatures (with a Fahrenheit temperature)"""
    CELS = 32.0
    KELV = 273.16
    print('Fahrenheit is', temper_fahr, 'Celsius is', round((5.0 / 9.0) * (temper_fahr - CELS), 2),
          'Kelvin is', round((5.0 / 9.0) * (temper_fahr - CELS) + KELV, 2))
    
    
def get_input() -> float | None:
    print('Enter a Fahrenheit temperature (q to quit): ')
    try:
        return float(input())
    except ValueError:
        return None
    
    
temp_fahr = get_input()
while temp_fahr is not None:
    temperatures(temp_fahr)
    temp_fahr = get_input()
    
    
    
