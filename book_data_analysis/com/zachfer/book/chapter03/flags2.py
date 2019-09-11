import matplotlib.pyplot as plt
import matplotlib.image as mi
import pylab


def flag_num(num):
    flag_arr_temp = []
    for index in range(num):
        flag_arr_temp.append("flag (" + str(index + 1) + ")")
    return flag_arr_temp


def build_flag(flag_arr_args, rows_args, columns_args):
    flag_img_temp = []
    for index in range(rows_args * columns_args):
        flag_img_temp.append(mi.imread('./flags-big/' + flag_arr_args[index] + '.png'))
    return flag_img_temp


def draw_flags(flag_img_args, rows_args, columns_args, fig_args):
    for index in range(rows_args * columns_args):
        fig_args.add_subplot(rows, columns, index + 1)
        plt.imshow(flag_img_args[index])


while True:
    rows = int(input("请输入以几行展示："))
    columns = int(input("请输入以几列展示："))
    if rows * columns > 120:
        print("对不起，没有这么多张图片！！！")
        print()
        print("------请重新输入---------")
    else:
        flag_arr = flag_num(rows * columns)
        flag_img = build_flag(flag_arr, rows, columns)
        fig = plt.figure()
        draw_flags(flag_img, rows, columns, fig)
        pylab.show()
        break

