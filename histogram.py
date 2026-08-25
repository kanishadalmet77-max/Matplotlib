import matplotlib.pyplot as plt

scores=[45,50,52,55,60,62,65,68,70,72,75,80,85,90]

plt.hist(scores, bins=[40,50,60,70,80,90],edgecolor="black")

plt.title("score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()