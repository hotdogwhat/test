import matplotlib.pyplot as plt
import matplotlib.image as mi
import pylab

flag_arr = []
for i in range(9):
    flag_arr.append("flag (" + str(i + 1) + ")")

flag_img = []
for i in range(9):
    flag_img.append(mi.imread('./flags/' + flag_arr[i] + '.png'))

fig = plt.figure()

for i in range(9):
    fig.add_subplot(3, 3, i + 1)
    plt.imshow(flag_img[i])

pylab.show()


