import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2)

axes[0].plot([1, 2, 3], [10, 20, 30])
axes[0].set_title("Sales")

axes[1].bar(["A", "B", "C"], [20, 35, 25])
axes[1].set_title("Products")

plt.tight_layout()
plt.show()