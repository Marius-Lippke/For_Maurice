# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:02:12 2020

@author: mariu
"""

import vtk

reader = vtk.vtkDICOMImageReader() 
reader.SetDirectoryName('Marching_Man')
reader.Update()


# threshold = vtk.vtkImageThreshold ()
# threshold.SetInputConnection(reader.GetOutputPort())
# threshold.ThresholdByLower(1000)  # remove all soft tissue
# threshold.ReplaceInOn()
# threshold.SetInValue(0)  # set all values below 400 to 0
# threshold.ReplaceOutOn()
# threshold.SetOutValue(1)  # set all values above 400 to 1
# threshold.Update()

#----------------------Filter------------------------------------------#
extractor = vtk.vtkMarchingCubes()
extractor.SetInputConnection(reader.GetOutputPort()) 
extractor.SetValue(10 , 500)
extractor.ComputeNormalsOff()
extractor.Update()

#----------------------Plane&Cutter------------------------------------#

plane = vtk.vtkPlane()
plane.SetOrigin(120,0,0)
plane.SetNormal(1,0,0)

cutter = vtk.vtkCutter()
cutter.SetCutFunction(plane)
cutter.SetInputConnection(reader.GetOutputPort())
cutter.Update()


#----------------------Mapper------------------------------------------#
cuttermapper = vtk.vtkPolyDataMapper()
cuttermapper.SetInputConnection(cutter.GetOutputPort())

extractormapper = vtk.vtkPolyDataMapper()
extractormapper.SetInputConnection(extractor.GetOutputPort())
extractormapper.ScalarVisibilityOff()



#----------------------Actor------------------------------------------#
extract_actor = vtk.vtkActor()
extract_actor.SetMapper(extractormapper)

cutter_actor = vtk.vtkActor()
cutter_actor.SetMapper(cuttermapper)
cutter_actor.GetProperty().SetLineWidth(2)

#----------------------Renderer---------------------------------------#
renderer = vtk.vtkRenderer()
renderer.AddActor(extract_actor)
renderer.AddActor(cutter_actor)
renderer.SetBackground(0.0, 0.0, 0.0)

#----------------------RenWindow--------------------------------------#
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

#----------------------Interactor-------------------------------------#

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)


window.SetSize(500,500)
interactor.Initialize()

window.Render() 
interactor.Start()