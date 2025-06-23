CUP_IN_PINT = 2.0
OUNC_IN_CUP = 8.0
TABLESPOON_IN_OUNC = 2.0
TEASPOON_IN_TABLESPOON = 3.0
print('Enter volume in cups: ')
volume = float(input())
print('In pints =', volume / CUP_IN_PINT)
print('In ounces =', volume * OUNC_IN_CUP)
print('In tablespoons =', volume * OUNC_IN_CUP * TABLESPOON_IN_OUNC)
print('In tablespoons =', volume * OUNC_IN_CUP * TABLESPOON_IN_OUNC * TEASPOON_IN_TABLESPOON)
