import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr","May"]
sales=[120,180,150,200,190]

plt.plot(months,sales,label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.legend()
plt.show()