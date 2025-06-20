cup_in_pint = 2.0
ounc_in_cup = 8.0
tablespoons_in_ounc = 2.0
teaspoons_in_tablespoon = 3.0
print('Enter volume in cups: ')
volume = float(input())
print('In pints =', volume / cup_in_pint)
print('In ounces =', volume * ounc_in_cup)
print('In tablespoons =', volume * ounc_in_cup * tablespoons_in_ounc)
print('In tablespoons =', volume * ounc_in_cup * tablespoons_in_ounc * teaspoons_in_tablespoon)
