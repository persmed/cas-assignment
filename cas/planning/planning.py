import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt
import scipy.ndimage

from assignments.planning import segmentation


class ImageViewer:
    def __init__(self):
        self.image = None
        self.segmentation = None
        self.slice = 0
        self.image_spacing = None
        self.image_ysize = None
        self.image_xsize = None
        self.image_zsize = None
        self.image_slice = None
        self.segmentation_slice = None
        self.image_slice_number = 0
        self.segmenter = None
        self.t = None
        self.t2 = None
        self.overlay_alpha = 0

    def set_segmenter(self, segmenter):
        self.segmenter = segmenter

    def set_image(self, image):
        self.image = sitk.GetArrayFromImage(image)

        self.segmentation = np.zeros(self.image.shape)
        self.image_spacing = image.GetSpacing()
        self.image_ysize = self.image.shape[0]
        self.image_xsize = self.image.shape[1]
        self.image_zsize = self.image.shape[2]
        self.image_slice_number = self.image.shape[0] // 2
        self.image_slice = self.image[self.image_slice_number, :, :]
        self.segmentation_slice = self.segmentation[self.image_slice_number, :, :]
        self.segmentation_slice[0, 0] = 4.0

    def onscroll(self, event):
        if event.button == 'up' and self.image_slice_number < self.image_zsize - 1:
            # print('up')
            self.image_slice_number += 1
        elif event.button == 'down' and self.image_slice_number > 0:
            # print('down')
            self.image_slice_number -= 1

        # print(self.image_slice_number)
        self.image_slice = self.image[self.image_slice_number, :, :]
        self.segmentation = self.segmenter.get_segmentation_mask()
        self.segmentation_slice = self.segmentation[self.image_slice_number, :, :]
        # print('nonzero: ', np.count_nonzero(self.segmentation_slice))
        self.__update()

    def onclick(self, event):
        print(event)
        if event.button == 1:
            x = int(round(event.xdata, 0))
            y = int(round(event.ydata, 0))
            self.segmenter.segment(x, y, self.image_slice_number)
            self.segmentation = self.segmenter.get_segmentation_mask()
            self.__update()

    def keypress(self, event):
        try:
            if event.key == ' ':
                self.toggle_overlay()
            elif event.key == 'x':
                print('Histogram')
                segmentation_hist = scipy.ndimage.histogram(self.segmentation, 0, 4, 5)
                print(segmentation_hist)
            elif event.key == 's':
                print('Saving')
                np.save('segmentation.npy', self.segmentation)
            else:
                key_pressed = int(event.key)
                self.segmenter.activate_label(key_pressed)
        except TypeError:
            print('was not a number between 0 and 4')
        print('current active label is ', self.segmenter.get_active_label_name())
        self.__update()

    def __update(self):
        self.t.set_data(self.image_slice)
        self.t.set_cmap("gray")
        self.t.set_alpha(1)
        self.t2.set_data(self.segmentation_slice)
        self.t2.set_alpha(self.overlay_alpha)
        self.t2.set_cmap('jet')
        plt.draw()

    def show(self):
        margin = 0.05
        dpi = 80
        figsize = (1 + margin) * self.image_ysize / dpi, (1 + margin) * self.image_xsize / dpi
        fig = plt.figure(figsize=figsize, dpi=dpi)
        cid = fig.canvas.mpl_connect('scroll_event', self.onscroll)
        cid2 = fig.canvas.mpl_connect('button_press_event', self.onclick)
        cid3 = fig.canvas.mpl_connect('key_press_event', self.keypress)
        ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
        # extent = (0, self.image_xsize * self.image_spacing[1], self.image_ysize * self.image_spacing[0], 0)
        # plt.subplot(121)
        self.t = plt.imshow(self.image_slice, cmap='gray', interpolation=None)
        # plt.subplot(122)
        self.t2 = plt.imshow(self.segmentation_slice, cmap='jet', alpha=self.overlay_alpha, interpolation=None)
        plt.title("Image")
        plt.show()

    def toggle_overlay(self):
        if self.overlay_alpha < 0.5:
            self.overlay_alpha = 0.75
        else:
            self.overlay_alpha = 0


class Segmenter:
    def __init__(self):
        self.labels = {
            0: 'None',
            1: 'Spinal Cord',
            2: 'Vertebraes',
            3: 'Pelvis',
            4: 'Discs'
        }
        self.__active_label = 0
        self.data = None
        self.segmentation_mask = None

    def set_data(self, data):
        self.data = data
        self.segmentation_mask = np.zeros(self.data.shape)

    def segment(self, x, y, z):
        print('segmenting')
        print('data at ({0}, {1}, {2}) is {3}'.format(x, y, z, self.data[z, y, x]))
        print(self.segmentation_mask.shape)
        print(self.data.shape)
        current_mask = segmentation.region_grow(self.data, (z, y, x))
        self.segmentation_mask[current_mask] = self.__active_label
        self.segmentation_mask = self.segmentation_mask.astype(np.uint8)

    def activate_label(self, label):
        if 0 <= label <= 4:
            self.__active_label = label

    def get_active_label_name(self):
        return self.labels[self.__active_label]

    def get_segmentation_mask(self):
        return self.segmentation_mask


image = sitk.ReadImage("data\planning\Pelvis_CT.nii")

size = image.GetSize()
spacing = image.GetSpacing()
reference_image = sitk.Image(int(size[0] / 2), int(size[1] / 2), int(size[2] / 2), sitk.sitkUInt32)

resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(reference_image)
resampler.SetOutputOrigin(image.GetOrigin())
resampler.SetOutputSpacing([spacing[0] * 2, spacing[1] * 2, spacing[2] * 2])
resampler.SetInterpolator(sitk.sitkNearestNeighbor)
resampled = resampler.Execute(image)
print(resampled.GetSpacing())
print(resampled.GetSize())
image = resampled

nda = sitk.GetArrayFromImage(image)

segmenter = Segmenter()
segmenter.set_data(nda)

viewer = ImageViewer()
viewer.set_segmenter(segmenter)
viewer.set_image(image)
viewer.show()
