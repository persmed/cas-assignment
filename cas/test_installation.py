import numpy as np
print('Numpy version:\t\t\t', np.__version__)

import vtk
print('VTK version:\t\t\t', '{0}.{1}'.format(vtk.VTK_MAJOR_VERSION, vtk.VTK_MINOR_VERSION))

import SimpleITK as sitk
print('SimpleITK version:\t\t', '{0}.{1}'.format(sitk.SITK_ITK_VERSION_MAJOR, sitk.SITK_ITK_VERSION_MINOR))

import matplotlib
print('Matplotlib version:\t\t', matplotlib.__version__)

import transformations
print('Transformations version:\t', transformations.__version__)

import pydicom
print('PyDICOM version:\t\t', pydicom.__version__)

import scipy
print('SciPy version:\t\t\t', scipy.__version__)

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

print("Testing matplotlib...")
image = sitk.ReadImage("data/planning/Pelvis_CT.nii")
size = image.GetSize()
spacing = image.GetSpacing()
reference_image = sitk.Image(int(size[0] / 2), int(size[1] / 2), int(size[2] / 2), sitk.sitkUInt32)

resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(reference_image)
resampler.SetOutputOrigin(image.GetOrigin())
resampler.SetOutputSpacing([spacing[0] * 2, spacing[1] * 2, spacing[2] * 2])
resampler.SetInterpolator(sitk.sitkNearestNeighbor)
resampled = resampler.Execute(image)
image = resampled

nda = sitk.GetArrayFromImage(image)
image_slice = nda[120, :, :]
plt.imshow(image_slice, cmap='gray', interpolation=None)
plt.pause(1)
print("Testing matplotlib... [OK]")

print('Your environment is ready...')
