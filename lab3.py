# Customer's monthly salary
monthly_salary = float(input("Enter monthly salary:"))
# Loan amount requested
loan_amount = float(input("Enter the requested loan amount:"))

# Check if customer is eligible for loan
if monthly_salary >= 30000.00 and loan_amount <= monthly_salary * 10:
    print("Customer is eligible for loan!")
    # Get the number of months to pay
    months_to_pay = int(input("Enter the number of months the customer wish to pay:"))
    # Calculate the monthly payment with 10% interest increase 
    interest_rate = 0.10
    total_amount = loan_amount + (loan_amount * interest_rate)
    monthly_payment = total_amount / months_to_pay
    print("Total amount of payment:" + str(total_amount))
    print("Total payment over " + str(months_to_pay) + " months:" + str(monthly_payment))
else:
    print("Customer is not eligible for loan.")
    if monthly_salary < 30000.00:
        print("Monthly salary is too low.")
    if loan_amount > monthly_salary * 10:
        print("Requested loan amount is too high.")