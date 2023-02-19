import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5]

# list of y-axis values
y_list = [
    [2, 4, 6, 8, 10],
    [100, 300, 500, 700, 900],
    [1200, 1400, 1600, 1800, 2100],
    [3, 4, 5, 6, 7]
]

# plot the unique y-axis values
for y in set(map(tuple, y_list)):
    if y_list.count(list(y)) == 1:
        plt.plot(x, list(y))

# add axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple lines with unique y-axis values')

# show the plot
plt.show()
