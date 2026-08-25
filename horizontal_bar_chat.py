import matplotlib.pyplot as plt

Products=["Mobile","Tablet","Laptop","Earpods","Charger"]
sales=[120,180,110,200,190]

plt.barh(Products,sales)

plt.title("Products Sales")
plt.xlabel("Sales")
plt.ylabel("Products")

plt.show()