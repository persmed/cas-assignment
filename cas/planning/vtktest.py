# An example from scipy cookbook demonstrating the use of numpy arrys in vtk

import vtk
import numpy as np
from numpy import *

# We begin by creating the data we want to render.
# For this tutorial, we create a 3D-image containing three overlaping cubes.
# This data can of course easily be replaced by data from a medical CT-scan or anything else three dimensional.
# The only limit is that the data must be reduced to unsigned 8 bit or 16 bit integers.
data_matrix = np.load('segmentation.npy') * 30
data_matrix = data_matrix.astype(np.uint8)
print(np.min(np.min(data_matrix)))
print(np.max(np.max(data_matrix)))

dataImporter = vtk.vtkImageImport()
data_string = data_matrix.tostring()
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
dataImporter.SetDataScalarTypeToUnsignedChar()
dataImporter.SetNumberOfScalarComponents(1)
[h,w,z] = data_matrix.shape
dataImporter.SetDataExtent(0,z-1, 0, w-1, 0,h-1)
dataImporter.SetWholeExtent(0,z-1, 0,w-1, 0,h-1)
dataImporter.SetDataSpacing(1.0, 0.5, 0.5)

contour = vtk.vtkContourFilter()
#contour = vtk.vtkMarchingCubes()
contour = vtk.vtkDiscreteMarchingCubes()
contour.SetInputConnection(dataImporter.GetOutputPort())
contour.ComputeNormalsOn()
contour.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contour.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 1.0, 0.0)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0, 0, 0)

renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtk.vtkRenderWindowInteractor()
style = vtk.vtkInteractorStyleTrackballActor()
#renderInteractor.SetInteractorStyle(style)
renderInteractor.SetRenderWindow(renderWin)

renderWin.SetSize(400, 400)

#Launching the renderer
renderInteractor.Initialize()
renderWin.Render()
renderInteractor.Start()