from matplotlib import pyplot as plt
import numpy as np

sum = 0;
size = 0;

data = open('data.txt','r')
data_size = len(data.readlines())

x,y = np.loadtxt('data.txt',
                 unpack = True,
                 delimiter= ':')

y = out_num = np.reciprocal(y)

for i in range(0,data_size):
    size = 0.5 * y[i]
    sum += size

data.close()

print("Impulse: " + str(size))

plt.plot(x,y);
plt.bar(x,y, width=0.05, color = '#ADD8E6')
plt.title('Time to Force')
plt.ylabel('Force')
plt.xlabel('Time')
plt.show()