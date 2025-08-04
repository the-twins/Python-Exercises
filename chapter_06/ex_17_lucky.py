PERCENT = 0.08
WITHDRAW = 100000
score = 1000000
years = 0
while (score > 0):
    score += score * PERCENT
    score -= WITHDRAW
    years += 1
print("Money will run out in" , years, "years.")
