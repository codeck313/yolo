import os
import sys
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from xml_generator import write_xml

img = None
tl_list = []  # tl mouse click
br_list = []  # br mouse click
object_list = []

image_folder = '/home/pyrop/Documents/YOLO/IMAGES_JPEG'
savedir = 'anotations_jpeg'
obj = 'fidget_spinner'
extension = 'jpeg'


def lines_select_callback(clk, rls):
    global tl_list
    global br_list
    global img
    print("Recording the Co-ordinates - File Name", img.name)
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def onKeyPress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        if tl_list != [] and br_list != []:
            print("Saving")
            write_xml(image_folder, img, object_list,
                      tl_list, br_list, savedir, extension)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()
    if event.key == 'e':
        raise SystemExit()


def toggle_selector(event):

    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        try:
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
        except KeyboardInterrupt or SystemExit:
            sys.exit()

        except:
            print("Error Occured in image", img.name)
            tl_list = []
            br_list = []
            object_list = []
            img = None
            pass
