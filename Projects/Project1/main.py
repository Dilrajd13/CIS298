#DIlraj Dhillon CIS 298

while True:
    income= int(input("Please Enter your income: "))

    choice= input("Is the income CORRECT? Y/N: ")
    if choice.lower() == 'y':
        break;

while True:
    deduction= int(input("Please Enter you total deductions: "))

    choice = input("Is the income CORRECT? Y/N: ")
    if choice.lower() == 'y':
        break;

AGI= income-deduction


standard_deduction = 14600
if deduction < standard_deduction:
    deduction = standard_deduction

print(f'Your AGI ( Adjusted Gross Income) is {AGI}')

# Caluclate Taxes

taxowed10 = 0
taxowed12 = 0
taxowed22 = 0
taxowed24 = 0
taxowed32 = 0
taxowed35 = 0
taxowed37 = 0

if AGI > 609350:
    taxowed37 = (AGI - 609350) * 0.37
    AGI = 609350
if AGI > 243725:
    taxowed35 = (AGI - 243725) * 0.35
    AGI = 243725
if AGI > 191950:
    taxowed32 = (AGI - 191950) * 0.32
    AGI = 191950
if AGI > 100525:
    taxowed24 = (AGI - 100525) * 0.24
    AGI = 100525
if AGI > 47150:
    taxowed22 = (AGI - 47150) * 0.22
    AGI = 47150
if AGI > 11600:
    taxowed12 = (AGI - 11600) * 0.12
    AGI = 11600
taxowed10 = AGI * 0.10

total_taxes = ( taxowed10 + taxowed12 + taxowed22 + taxowed24 + taxowed32 + taxowed35 + taxowed37)

print(f'Taxes Owed at 10% bracket: ${taxowed10}')
print(f'Taxes Owed at 12% bracket: ${taxowed12}')
print(f'Taxes Owed at 22% bracket: ${taxowed22} ')
print(f'Taxes Owed at 24% bracket: ${taxowed24}')
print(f'Taxes Owed at 32% bracket: ${taxowed32}')
print(f'Taxes Owed at 35% bracket: ${taxowed35}')
print(f'Taxes Owed at 37% bracket: ${taxowed37}')
print(f'Total Taxes Owed: ${total_taxes }')
print(f'Taxes Owed as Percentage of Gross Income: {100 * total_taxes / income}%')
print(f'Taxes Owed as Percentage of Adjusted Gross Income: {100 * total_taxes / (income - deduction)}%')