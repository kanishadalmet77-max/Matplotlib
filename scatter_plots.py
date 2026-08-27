import matplotlib.pyplot as plt

hours=[1,2,3,4,5]
scores=[45,50,60,70,85]

plt.scatter(hours,scores)

plt.title("Study hours VS Scores")
plt.xlabel("Study hours")
plt.ylabel("Scores")

plt.show()