import sys
from pathlib import Path

print(
    "Python version:\t\t\t"
    f"{sys.version_info.major}."
    f"{sys.version_info.minor}."
    f"{sys.version_info.micro}"
)

import numpy as np

print(f"Numpy version:\t\t\t{np.__version__}")

import vtk

print(f"VTK version:\t\t\t{vtk.VTK_MAJOR_VERSION}.{vtk.VTK_MINOR_VERSION}")

import SimpleITK as sitk

print(
    "SimpleITK version:\t\t"
    f"{sitk.SITK_ITK_VERSION_MAJOR}.{sitk.SITK_ITK_VERSION_MINOR}"
)

import matplotlib

print(f"Matplotlib version:\t\t{matplotlib.__version__}")

import transformations

print(f"Transformations version:\t{transformations.__version__}")

import scipy

print(f"SciPy version:\t\t\t{scipy.__version__}")


repo_root = Path(__file__).resolve().parents[1]
image_path = repo_root / "data" / "planning" / "pelvis_ct.nii.gz"

if not image_path.exists():
    print("\nERROR: Required file not found:")
    print(f"  {image_path}")
    print("\nFix:")
    print("  Download pelvis_ct.nii.gz from ILIAS and copy it to:")
    print("  data/planning/pelvis_ct.nii.gz (relative to the repository root)")
    print("\nDebug info:")
    print(f"  Repository root: {repo_root}")
    print(f"  Current working directory: {Path.cwd()}")
    sys.exit(1)


matplotlib.use("TkAgg", force=True)
import matplotlib.pyplot as plt

print("Testing matplotlib...", end="", flush=True)

try:
    image = sitk.ReadImage(str(image_path))
except Exception as e:
    print("\rTesting matplotlib... [FAILED]", flush=True)
    print("\nERROR: Could not read the test image:")
    print(f"  {image_path}")
    print(f"\nException: {e}")
    sys.exit(1)

size = image.GetSize()
spacing = image.GetSpacing()
reference_image = sitk.Image(
    int(size[0] / 2),
    int(size[1] / 2),
    int(size[2] / 2),
    sitk.sitkUInt32,
)

resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(reference_image)
resampler.SetOutputOrigin(image.GetOrigin())
resampler.SetOutputSpacing([spacing[0] * 2, spacing[1] * 2, spacing[2] * 2])
resampler.SetInterpolator(sitk.sitkNearestNeighbor)
resampled = resampler.Execute(image)
image = resampled

nda = sitk.GetArrayFromImage(image)
image_slice = nda[120, :, :]
plt.imshow(image_slice, cmap="gray", interpolation=None)
plt.pause(1)
plt.close()
print("\rTesting matplotlib... [OK]", flush=True)

print("Your environment is ready.")