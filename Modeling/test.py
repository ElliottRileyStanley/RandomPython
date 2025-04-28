import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image


ax = plt.figure().add_subplot(projection='3d')

data = np.random.randint(0, 2, size=(25, 25, 25))
print("data generated")


ax.voxels(data, facecolors=[0, 0, 0])
print("voxels drawn")

ax.axis('off')

ax.set_aspect('equal')
ax.view_init(elev=45, azim=45)
print("axis off, aspect set")


buf = io.BytesIO()
plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
print("saving figure to buf")


buf.seek(0)
img = Image.open(buf)
img = img.convert('1')
img.save(r'Modeling/test.png')
