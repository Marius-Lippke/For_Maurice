# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:43:27 2020

@author: mariu
"""

import vtk

def dicom_reader(reader):
    xMin, xMax, yMin, yMax, zMin, zMax = reader.GetDataExtent()
    xSpacing, ySpacing, zSpacing = reader.GetOutput().GetSpacing()
    print(xSpacing, ySpacing, zSpacing)
    x0, y0, z0 = reader.GetOutput().GetOrigin()
    center = [x0 + xSpacing * 0.5 * (xMin + xMax),
              y0 + ySpacing * 0.5 * (yMin + yMax),
              z0 + zSpacing * 0.5 * (zMin + zMax)]
    
    axial = vtk.vtkMatrix4x4()
    axial.DeepCopy((1, 0, 0, center[0],
                    0, 1, 0, center[1],
                    0, 0, 1, center[2],
                    0, 0, 0, 1))
    reslice = vtk.vtkImageReslice()
    reslice.SetInputConnection(reader.GetOutputPort())
    reslice.SetOutputDimensionality(2)
    reslice.SetResliceAxes(axial)
    reslice.SetInterpolationModeToCubic()

    glob_level = 0.
    glob_window = 2048.
    table = vtk.vtkLookupTable()
    table.SetRange(glob_level-glob_window/2, glob_level+glob_window/2) # Level-Window -> intensity range
    table.SetValueRange(0.0, 1.0) # von schwarz nach weiß
    table.SetSaturationRange(0.0, 0.0) # keine Farbsättigung
    table.SetRampToLinear() # Linearer Verlauf
    table.Build()
    
    color = vtk.vtkImageMapToColors()
    color.SetLookupTable(table)
    color.SetInputConnection(reslice.GetOutputPort())
    
    actor = vtk.vtkImageActor()
    actor.GetMapper().SetInputConnection(color.GetOutputPort())
    
    return reslice, actor