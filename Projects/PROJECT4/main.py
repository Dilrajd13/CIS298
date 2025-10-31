import csv
import matplotlib.pyplot as plt
count=0
max=50
sale_totals = {}
town = []
with open('Real_Estate_Sales_2001-2022_GL.csv') as bdata:
    reader = csv.DictReader(bdata)

    for row in reader:
        if count >= max:
            break
        town = row['Town']
        sale_amount = float(row['Sale Amount'])
        sale_totals[town] = sale_totals.get(town, 0) + sale_amount
        count+=1
    towns = list(sale_totals.keys())
    total_sales = list(sale_totals.values())

    plt.figure(figsize=(7, 7))
    plt.bar(towns, total_sales, color='skyblue')
    plt.xlabel('Town')
    plt.ylabel('Total Sale Amount')
    plt.title('Total Sale Amount by Town')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(7, 8))
    plt.pie(total_sales, labels=towns, autopct='%1.1f%%', startangle=140)
    plt.title(' Sale Amount by Town ')
    plt.axis('equal')
    plt.show()

    x_values = range(len(towns))

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, total_sales, color='blue', s=100)  # s controls the marker size
    plt.xlabel('Town')
    plt.ylabel('Total Sale Amount')
    plt.title('Sale Amount by Town ')
    plt.xticks(x_values, towns, rotation=45)  # Replace x-tick labels with town names
    plt.tight_layout()
    plt.show()