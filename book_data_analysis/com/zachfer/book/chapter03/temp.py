import matplotlib.pyplot as plt
import matplotlib.image as mi
import pylab

img = mi.imread('./flags/flag (1).png')

# fig = plt.figure()
# fig.add_subplot(1, 2, 1)
# plt.imshow(img1)
# fig.add_subplot(1, 2, 2)
# plt.imshow(img2)
#


plt.imshow(img)

fig = plt.figure()

# for i in range(2):
#     for j in range(2):
#         print(i, j)
#         fig.add_subplot(i + 1, 2, j + 1)
#         plt.imshow(img)


fig.add_subplot(2, 2, 1)
plt.imshow(img)
fig.add_subplot(2, 2, 2)
plt.imshow(img)
fig.add_subplot(2, 2, 3)
plt.imshow(img)
fig.add_subplot(2, 2, 4)
plt.imshow(img)


pylab.show()



#
#
# import matplotlib.pyplot as plt
# import matplotlib.image as mi
# import pylab
#
# # img1 = mi.imread('./flags/af.png')
# # img2 = mi.imread('./flags/ag.png')
# #
# # fig = plt.figure()
# # fig.add_subplot(1, 2, 1)
# # plt.imshow(img1)
# # fig.add_subplot(1, 2, 2)
# # plt.imshow(img2)
# #
# #
# # pylab.show()
#
# flag_arr = []
# for i in range(9):
#     flag_arr.append("flag (" + str(i + 1) + ")")
#
# # print(flag_arr)
#
# flag_img = []
#
# for i in range(9):
#     print(i, flag_arr[i])
#     flag_img.append(mi.imread('./flags/' + flag_arr[i] + '.png'))
#
# fig = plt.figure()
#
# for i in range(9):
#     fig.add_subplot(3, 3, i + 1)
#     plt.imshow(flag_img[i])
#
# pylab.show()
#
#
#
#
