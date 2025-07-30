def result(first_numb: float, second_numb: float) -> float:
    """Return the value of the calculation"""
    return (first_numb - second_numb) / (first_numb * second_numb)
    

print("Enter a first float: ")
try:
    first_numb = float(input())
except ValueError:
    first_numb = None
while first_numb is not None:
    print("Enter a second float: ")
    second_numb = float(input())
    print(result(first_numb, second_numb))
    print("Enter a first float or q to quit: ")
    try:
        first_numb = float(input())
    except ValueError:
        first_numb = None
