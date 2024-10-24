# 3200, 5000, 1790, 8900 and 2300 

monthly_cost = 100
amount_of_months = int(input("Enter the number of months the server will run: "))

purchase_cost = [3200, 5000, 1790, 8900, 2300]
i = 0

for hej in purchase_cost:
    print("The server costing " + str(purchase_cost[i]) + " costs on average " + str(purchase_cost[i] / amount_of_months + monthly_cost) + " each month.")
    i += 1

print("Total cost: " + str(sum(purchase_cost) + (monthly_cost * 5 * amount_of_months)))
