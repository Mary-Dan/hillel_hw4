loan = float(input("Enter the loan amount: "))
interest_two_years = 0.02
interest_after_two_years = 0.04
loan_term = int(input("Enter the loan term in years: "))
total = loan_term * 12
monthly = 0
print("\n{:<8}{:<15}{:<15}".format("Month", "Payment", "Remaining Balance"))
for month in range(1, total + 1):
    if month <= 24:
        monthly_interest = loan * interest_two_years
    else:
        monthly_interest = loan * interest_after_two_years
    monthly_payment = (loan + monthly_interest) / total
    loan -= monthly_payment
    print("{:<8}{:<15}{:<15}".format(month, round(monthly_payment, 2), round(loan, 2)))
print("\nTotal amount paid:", round(total * monthly, 2))