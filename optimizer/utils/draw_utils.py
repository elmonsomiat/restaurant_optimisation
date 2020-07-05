import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def create_diagram(rectangles, security, room_size, filename):

    fig,ax = plt.subplots(1, figsize=(10,10))
    room = plt.Rectangle((0, 0), room_size[0], room_size[1], linewidth=1, edgecolor='g', facecolor='none')
    ax.add_patch(room)

    for box in rectangles:
        width = box.width
        height = box.height
        x = box.x
        y = box.y
        x_table = x + security/2
        w_table = width - security
        y_table = y + security/2
        h_table = height - security 
        
        if x == 0:
            x += security/2
            width -= security/2
        elif x==room_size[0]-width+security:
            width -= security/2
        if y == 0:
            y += security/2
            height -= security/2
        elif y==room_size[1]-height+security:
            height -= security/2
        
        x -= security/2
        y -= security/2
        x_table -= security/2
        y_table -= security/2

        rect = plt.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)


        rect = plt.Rectangle((x_table, y_table), w_table, h_table ,linewidth=2, edgecolor='b', facecolor='none')
        ax.add_patch(rect)

        plt.text(x + width/3, y + height/2, str(width-security) +','+ str(height-security))

    ax.scatter([1], [1],color="w")
    plt.savefig(str(filename)+'.png')

