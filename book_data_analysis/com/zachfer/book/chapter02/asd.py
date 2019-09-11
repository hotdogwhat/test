# import numpy as np
#
# print(np.array([1, 2, 3, 4]))

import numpy as np

import matplotlib.pyplot as pt

x = np.arange(0, 360)

y = np.sin(x * np.pi / 180)

pt.plot(x, y)

pt.xlim(0, 360)

pt.ylim(-1.2, 1.2)

pt.title("SIN function")

pt.show()
