# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:49:59 2020

@author: mariu
"""
import vtk

class CubesClass:
    planeNormal_x = 1
    planeNormal_y = 0
    planeNormal_z = 0
    
    planeOrigin_x = 0
    planeOrigin_y = 0
    planeOrigin_z = 0
    
    def __init__(self, reader):
        self.reader = reader
        self.extractor = vtk.vtkMarchingCubes()
        self.plane = vtk.vtkPlane()
        self.cutter = vtk.vtkCutter()
        self.cuttermapper = vtk.vtkPolyDataMapper()
        self.extractormapper = vtk.vtkPolyDataMapper()
        self.extract_actor = vtk.vtkActor()
        self.cutter_actor = vtk.vtkActor()
        
    def setExtractor(self,lower, upper):

        self.extractor.SetInputConnection(self.reader.GetOutputPort()) 
        self.extractor.SetValue(lower , upper)
        self.extractor.ComputeNormalsOff()
        self.extractor.Update()
        self.extractormapper.SetInputConnection(self.extractor.GetOutputPort())
        self.extractormapper.ScalarVisibilityOff()
        self.extract_actor.SetMapper(self.extractormapper)
        
    def setPlane(self,x, y, z):
        self.planeOrigin_x = x
        self.planeOrigin_y = y
        self.planeOrigin_z = z
        self.plane.SetOrigin(self.planeOrigin_x,self.planeOrigin_x,self.planeOrigin_x)
        self.setNormal(self.planeNormal_x,self.planeNormal_y,self.planeNormal_z)
        self.cutter.SetCutFunction(self.plane)
        self.cutter.SetInputConnection(self.reader.GetOutputPort())
        self.cutter.Update()
        self.cuttermapper = vtk.vtkPolyDataMapper()
        self.cuttermapper.SetInputConnection(self.cutter.GetOutputPort())
        self.cutter_actor.SetMapper(self.cuttermapper)
        self.cutter_actor.GetProperty().SetLineWidth(2)
        
    def setNormal(self, x,y,z):
        self.planeNormal_x = x
        self.planeNormal_y = y
        self.planeNormal_z = z
        self.plane.SetNormal(x,y,z)

        
    def getExtractorActor(self):
        return self.extract_actor
    
    def getCutterActor(self):
        self.cutter.Update()
        return self.cutter_actor
    
    
        
        