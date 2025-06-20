The program requests a volume in cups and that displays the equivalent
// volumes in pints, ounces, tablespoons, and teaspoons. A pint is 2 cups, a
// cup is 8 ounces, an ounce is 2 tablespoons, and a tablespoon is 3 teaspoons
cup_in_pint = 2.0
ounc_in_cup = 8.0
tablespoons_in_ounc = 2.0
teaspoons_in_tablespoon = 3.0
print('Enter volune in cups: ')
volume = float(input())
print('In pints =', volume / cup_in_pint)
print('In ounces =', volume * ounc_in_cup)
print('In tablespoons =', volume * ounc_in_cup * tablespoons_in_ounc)
print('In tablespoons =', volume * ounc_in_cup * tablespoons_in_ounc * teaspoons_in_tablespoon)
