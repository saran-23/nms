import matplotlib.pyplot as plt
import matplotlib.patches as patches

image = plt.imread('index.jpg')

# draw emtpy figure
fig = plt.figure()

# define axis
ax = fig.add_axes([0, 0, 1, 1])

# plot image
plt.imshow(image)
      
# create rectangular patch
rect_1 = patches.Rectangle((300, 420), 150, 210, edgecolor='green', facecolor='none', linewidth=2)
rect_4 = patches.Rectangle((490, 45), 200, 500, edgecolor='green', facecolor='none', linewidth=2)
    
# add patch
ax.add_patch(rect_1)
ax.text(328, 416, 'Box1:98%', color='green')

ax.add_patch(rect_4)
ax.text(492, 33, 'Box4:98%', color='green')


# show figure
plt.show()
