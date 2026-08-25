import matplotlib.pyplot as plt

Products=["Mobile","Tablet","Laptop","Earpods","Charger"]
sales=[120,180,110,200,190]

plt.bar(Products,sales)

plt.title("Products Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()