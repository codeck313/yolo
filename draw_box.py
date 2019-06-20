import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import writexml

img = None
tl_list = []  # tl mouse click
br_list = []  # br mouse click
object_list = []

image_folder = '/home/pyrop/Documents/YOLO/IMAGES'
savedir = 'anotations'
obj = 'fidget_spinner'
extenstion = 'jpg'


def lines_select_callback(clk, rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def onKeyPress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        writexml(image_folder, img, object_list,
                 tl_list, br_list, savedir, extension)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):

    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        # mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry = (250, 120, 1280, 1024)
        image = cv2.imread(img.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, lines_select_callback, drawtype='box',
            useblit=True, button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onKeyPress)
        plt.show()
