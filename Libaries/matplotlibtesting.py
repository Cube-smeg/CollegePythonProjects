from matplotlib import pyplot as plt

data = [4, 3, 1, 4, 2]

animals = ["Cat", "Dog", "Fish", "Rabbit", "piggy"]

plt.bar(animals, data, colors=["Red","Green","Yellow","Blue"])
plt.title("-Animal Ratings-")
plt.xlabel(animals)
plt.ylabel(data)
plt.show()


dataset1 = [12, 49, 31, 542, 29, 3, 59, 64, 88, 24]
dataset2 = [543, 453, 23, 765, 43, 876, 34, 23, 90]

plt.scatter(dataset1, dataset2)
plt.show()