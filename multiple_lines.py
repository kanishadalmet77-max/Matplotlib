import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr","May"]
sales_a=[120,180,150,200,190]
sales_b=[100,160,140,210,180]


plt.plot(months,sales_a,label="ProductA")
plt.plot(months,sales_b,label="ProductB")


plt.title("Monthly Sales Comparision")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.legend()
plt.show()