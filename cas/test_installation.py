import sys
print(f'Python version:\t\t\t{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')

import numpy as np
print(f'Numpy version:\t\t\t{np.__version__}')

import vtk
print(f'VTK version:\t\t\t{vtk.VTK_MAJOR_VERSION}.{vtk.VTK_MINOR_VERSION}')

import SimpleITK as sitk
print(f'SimpleITK version:\t\t{sitk.SITK_ITK_VERSION_MAJOR}.{sitk.SITK_ITK_VERSION_MINOR}')

import matplotlib
print(f'Matplotlib version:\t\t{matplotlib.__version__}')

import transformations
print(f'Transformations version:\t{transformations.__version__}')

import scipy
print(f'SciPy version:\t\t\t{scipy.__version__}')


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

print("Testing matplotlib...", end='', flush=True)
image = sitk.ReadImage("data/planning/pelvis_ct.nii.gz")
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
print("\rTesting matplotlib... [OK]", flush=True)

print('Your environment is ready.')
