#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

rangebar = range(3)
apples = plt.bar(rangebar, fruit[0, :], color='red', width=0.5)
bananas = plt.bar(rangebar, fruit[1, :],
                  bottom=fruit[0, :], color='yellow', width=0.5)
oranges = plt.bar(rangebar, fruit[2, :],
                  bottom=fruit[0, :] + fruit[1, :],
                  color='#ff8000', width=0.5)
peaches = plt.bar(rangebar, fruit[3, :],
                  bottom=fruit[0, :] + fruit[1, :] + fruit[2, :],
                  color='#ffe5b4', width=0.5)

plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.xticks(rangebar, ('Farrah', 'Fred', 'Felicia'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((apples[0], bananas[0], oranges[0], peaches[0]),
           ('Apples', 'Bananas', 'Oranges', 'Peaches'))
plt.show()
