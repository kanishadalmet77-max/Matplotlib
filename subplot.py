import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr","May"]
sales=[120,180,150,200,190]
expenses=[80,100,50,150,100]

plt.subplot(2,1,1)
plt.plot(months,sales)
plt.title("Sales")

plt.subplot(2,1,2)
plt.plot(months,expenses)
plt.title("Expenses")

plt.tight_layout()
plt.show()