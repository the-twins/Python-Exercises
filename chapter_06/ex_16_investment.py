DEPOSIT = 100
DAPHNE_PERCENT = 0.1
DEIRDRE_PERCENT = 0.05
sum_daphne = 100
sum_deirdre = 100
years = 0
while(sum_deirdre <= sum_daphne):
    sum_daphne += DEPOSIT * DAPHNE_PERCENT
    sum_deirdre += sum_deirdre * DEIRDRE_PERCENT
    years += 1
print("Deirdre's balance will be", sum_deirdre, "and Daphne's balance will be", sum_daphne, "after"
      , years, "years.")
