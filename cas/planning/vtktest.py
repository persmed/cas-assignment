# An example from scipy cookbook demonstrating the use of numpy arrys in vtk

import vtk
import numpy as np
from numpy import *

# We begin by creating the data we want to render.
# For this tutorial, we create a 3D-image containing three overlaping cubes.
# This data can of course easily be replaced by data from a medical CT-scan or anything else three dimensional.
# The only limit is that the data must be reduced to unsigned 8 bit or 16 bit integers.
data_matrix = np.load('segmentation.npy')
data_matrix = data_matrix.astype(np.uint8)
print(np.min(np.min(data_matrix)))
print(np.max(np.max(data_matrix)))

dataImporter = vtk.vtkImageImport()
data_string = data_matrix.tostring()
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
dataImporter.SetDataScalarTypeToUnsignedChar()
dataImporter.SetNumberOfScalarComponents(1)
[h, w, z] = data_matrix.shape
dataImporter.SetDataExtent(0, z - 1, 0, w - 1, 0, h - 1)
dataImporter.SetWholeExtent(0, z - 1, 0, w - 1, 0, h - 1)
dataImporter.SetDataSpacing(1.0, 0.5, 0.5)

# contour = vtk.vtkContourFilter()
# #contour = vtk.vtkMarchingCubes()
# contour = vtk.vtkDiscreteMarchingCubes()
# contour.SetInputConnection(dataImporter.GetOutputPort())
# contour.ComputeNormalsOn()
# # contour.GenerateValues(4, 1, 4)
# # contour.Update()
#
# # n = 4
# # lut = vtk.vtkLookupTable()
# # lut.SetNumberOfColors(n)
# # lut.SetTableRange(0, n - 1)
# # lut.SetScaleToLinear()
# # lut.Build()
# # lut.SetTableValue(1, 0, 0, 0, 1)
# # lut.SetTableValue(2, 1, 1, 0, 1)
# # lut.SetTableValue(3, 1, 0, 1, 1)
# # lut.SetTableValue(4, 1, 0, 0, 1)
#
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(contour.GetOutputPort())
# # mapper.SetLookupTable(lut)
# # mapper.SetScalarRange(0, lut.GetNumberOfColors())
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
# # actor.GetProperty().SetColor(0.0, 1.0, 0.0)

colors = vtk.vtkNamedColors()
colors.SetColor("Pelvis", [255, 255, 255, 255])
colors.SetColor("L4", [0, 255, 0, 255])
colors.SetColor("L5", [0, 128, 128, 255])
colors.SetColor("Discs", [0, 0, 255, 255])


def extract(color, isovalue):
    skinExtractor = vtk.vtkDiscreteMarchingCubes()
    skinExtractor.SetInputConnection(dataImporter.GetOutputPort())
    skinExtractor.SetValue(isovalue, isovalue)

    skinStripper = vtk.vtkStripper()
    skinStripper.SetInputConnection(skinExtractor.GetOutputPort())

    skinMapper = vtk.vtkOpenGLPolyDataMapper()
    skinMapper.SetInputConnection(skinStripper.GetOutputPort())
    skinMapper.ScalarVisibilityOff()

    skin = vtk.vtkOpenGLActor()
    skin.SetMapper(skinMapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d(color))
    skin.GetProperty().SetSpecular(.3)
    skin.GetProperty().SetSpecularPower(20)
    return skin


renderer = vtk.vtkOpenGLRenderer()
renderer.AddActor(extract("L4", 1))
renderer.AddActor(extract("L5", 2))
renderer.AddActor(extract("Pelvis", 3))
renderer.AddActor(extract("Discs", 4))
# renderer.AddActor(actor)
renderer.SetBackground(0, 0, 0)

renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtk.vtkRenderWindowInteractor()
style = vtk.vtkInteractorStyleTrackballActor()
# renderInteractor.SetInteractorStyle(style)
renderInteractor.SetRenderWindow(renderWin)

renderWin.SetSize(400, 400)

# Launching the renderer
renderInteractor.Initialize()
renderWin.Render()
renderInteractor.Start()
