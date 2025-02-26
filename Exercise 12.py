# Calculate Income Tax

'''
Calculate Income Tax for the given income by adhering to the below rules

Taxable Income	Rate (%)
First $10,000	0
Next $10,000	10
The remaining	20

Expected Output:
For example, suppose that the taxable income is $45000 the income tax payable is $10000*0% + $10000*10% + $25000*20% = $6000.

'''
income = int(input("Enter your income: "))
tax = 0

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax for first 10000 and 10% for next 10000
    tax_payable = (income - 10000) * 0.1
else:
    # first 10000 no tax, next 10000 10% and remaining 20%
    tax_payable = 10000 * 0 + 10000 * 0.1 + (income - 20000) * 0.2

print(f'The income tax payable is: {tax_payable}')