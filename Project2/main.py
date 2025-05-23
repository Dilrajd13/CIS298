# Dilraj Dhillon

import csv
import numpy as np
import matplotlib.pyplot as plt

print("Welcome to Retirement Planning Calculator\nWe need some information before we begin  ")

Year= 2025
userAge= int(input("Enter your age "))

userRetireAge= int(input("Enter you retirement age "))

mUnderMattress = float(input("Please enter money stored under you mattress "))

mBankSav= float(input("Enter Money in your bank savings "))

mBonds= float(input("Enter money in bonds "))

mStocks= float(input("Enter money in stocks "))


def calculateStockMean():
    total = 0
    count = 0
    with open("BondsAndStocksAnnualReturn.csv") as Annualret:
        next(Annualret)
        for row in Annualret:
            count += 1
            total += float(((row.split(sep=',')[1])[:-1]))
        return 1+((total/count)/100)

def calulateBondMean():
    total = 0
    count = 0
    with open("BondsAndStocksAnnualReturn.csv") as Annualret:
        next(Annualret)
        for row in Annualret:
            count += 1
            total += float(((row.split(sep=',')[2].strip())[:-1]))
        return 1+((total/count)/100)

def addbal():
    up = float(input("Enter a amount "))
    print(f'You added {up} dollars! ')
    return up

def printBal(a,b,c,d,Y):
    print("||||BALANCE||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(f'YEAR OF: {Year}')
    print(f'Under Mattress Balance: {mUnderMattress} ')
    print(f'Bank Savings Balance: {mBankSav} ')
    print(f'Bonds Balance: {mBonds} ')
    print(f'Stocks Balance: {mStocks} ')
    balance = mUnderMattress + mBankSav + mBonds + mStocks
    print(f'Total Balance is: {balance}')
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

def writeCSV(data):
    with open('RetirementRecord.csv', 'w', newline='') as csvfile:
        # https://www.geeksforgeeks.org/writing-csv-files-in-python/# used for reference to write a csv file
        fieldnames = ['Year', 'MattressAccount', 'BankSavingsAccount', 'BondsAccount', 'StocksAccount', 'Total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

bondrate=calulateBondMean()
stockrate=calculateStockMean()
out=[]

for x in range (userAge,userRetireAge):
    printBal(mUnderMattress, mBankSav, mBonds, mStocks,Year)

    data = {}
    data["Year"]= Year
    data["MattressAccount"]= mUnderMattress
    data["BankSavingsAccount"]=mBankSav
    data["BondsAccount"]=mBonds
    data["StocksAccount"]=mStocks
    balance = mUnderMattress+mBankSav+mBonds+mStocks
    data["Total"] = balance
    out.append(data)


    Year += 1

    choice = int(input("""
    
    Would you like to add any money to a account?
    1. Add to mattress money
    2. Add to bank savings
    3. Add to bond money
    4. Add to stocks money
    5. I dont want to add money
    """
     ))

    if (choice) == 1:
        mUnderMattress += addbal()
    elif (choice) == 2:
        mBankSav += addbal()
    elif (choice) == 3:
        mBonds += addbal()
    elif (choice) == 4:
        mStocks += addbal()
    else:
        print("No money added! ")

    mBankSav= (mBankSav*1.02)
    mBonds=(mBonds*bondrate)
    mStocks=(mStocks*stockrate)


data={}
data["Year"]= Year
data["MattressAccount"]= mUnderMattress
data["BankSavingsAccount"]=mBankSav
data["BondsAccount"]=mBonds
data["StocksAccount"]=mStocks
balance=mUnderMattress+mBankSav + mBonds + mStocks
data["Total"]=balance
out.append(data)

writeCSV(out)

print("Congratulations You HAVE ReAChEd ReTiReMeNt!!!!!!!")
printBal(mUnderMattress,mBankSav,mBonds,mStocks,Year)
print(f'Total Retirements Savings: {balance}')
#Adjusted for inflation

YearsThatHavePassed= userRetireAge-userAge
inflated=balance/pow(1.02,YearsThatHavePassed)
print(f'Adjusted For Inflation Balance: {inflated}')
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


years = []
totals = []

with open("RetirementRecord.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        years.append(int(row["Year"]))
        totals.append(float(row["Total"]))

plt.figure(figsize=(10, 6))
plt.plot(years, totals, marker='o', linestyle='-', label="Total Savings")
plt.title("Retirement Savings Over Time")
plt.xlabel("Year")
plt.ylabel("Total Savings")
plt.grid(True)
plt.legend()
plt.show()