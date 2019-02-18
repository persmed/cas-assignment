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

print('Your environment is ready...')
