# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:22:09 2020

@author: mariu
"""

import vtk
from CubesClass import CubesClass
from dicom_visualizer import dicom_reader

reader = vtk.vtkDICOMImageReader() 
reader.SetDirectoryName('Marching_Man')
reader.Update()


extrac_filter = CubesClass(reader)
extrac_filter.setExtractor(0, 500)
extrac_filter.setNormal(1,0,0)
extrac_filter.setPlane(120,0,0)

renderer = vtk.vtkRenderer()
renderer.AddActor(extrac_filter.getExtractorActor())
renderer.AddActor(extrac_filter.getCutterActor())
renderer.SetBackground(0.0, 0.0, 0.0)

renderer_2D = vtk.vtkRenderer()

reslice, actor = dicom_reader(reader)
renderer_2D.AddActor(actor)

window_3D = vtk.vtkRenderWindow()
window_2D = vtk.vtkRenderWindow()
window_3D.AddRenderer(renderer)
window_2D.AddRenderer(renderer_2D)

interactor_3D = vtk.vtkRenderWindowInteractor()
interactor_3D.SetRenderWindow(window_3D)

window_3D.SetSize(500,500)
interactor_3D.Initialize()

window_3D.Render() 
#------------------------------------------------------------------
interactorStyle_2D = vtk.vtkInteractorStyleImage()
interactor_2D = vtk.vtkRenderWindowInteractor()
interactor_2D.SetInteractorStyle(interactorStyle_2D)
window_2D.SetInteractor(interactor_2D)
window_2D.Render()

actions = {}
actions["Slicing"] = 0

def ButtonCallback(obj, event):
    if event == "LeftButtonPressEvent":
        actions["Slicing"] = 1
    else:
        actions["Slicing"] = 0

def MouseMoveCallback(obj, event):

    (lastX, lastY) = interactor_2D.GetLastEventPosition()
    (mouseX, mouseY) = interactor_2D.GetEventPosition()
    if actions["Slicing"] == 1:
        deltaY = mouseY - lastY
        reslice.Update()
        sliceSpacing = reslice.GetOutput().GetSpacing()[2]
        matrix = reslice.GetResliceAxes()
# move the center point that we are slicing through
        center = matrix.MultiplyPoint((0, 0, sliceSpacing*deltaY, 1))
        matrix.SetElement(0, 3, center[0])
        matrix.SetElement(1, 3, center[1])
        matrix.SetElement(2, 3, center[2])
        window_2D.Render()
    else:
        interactorStyle_2D.OnMouseMove()

interactorStyle_2D.AddObserver("MouseMoveEvent", MouseMoveCallback)
interactorStyle_2D.AddObserver("LeftButtonPressEvent", ButtonCallback)
interactorStyle_2D.AddObserver("LeftButtonReleaseEvent", ButtonCallback)
#------------------------------------------------------------------
interactor_2D.Start()
interactor_3D.Start()


