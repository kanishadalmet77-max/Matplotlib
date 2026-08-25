import matplotlib.pyplot as plt

Categories=["Clothing","Books","Electronics","Food"]
sales=[30,10,20,40]

plt.pie(sales,labels=Categories,autopct="%1.1f%%")

plt.title("Sales Distribution")

plt.show()