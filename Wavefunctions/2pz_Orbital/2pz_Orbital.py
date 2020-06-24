import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent


        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

    

        # Draw surface.
        points = adsk.core.ObjectCollection.create()

        x = 0.2
        y = 0
        z = 0.38  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.4
        y = 0
        z = 0.46  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.5
        y = 0
        z = 0.55  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.55
        y = 0
        z = 0.67  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.55
        y = 0
        z = 0.74  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.5
        y = 0
        z = 0.89  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.4
        y = 0
        z = 0.99  
        points.add(adsk.core.Point3D.create(x,y,z))

        x = 0.2
        y = 0
        z = 1.09  
        points.add(adsk.core.Point3D.create(x,y,z))

        #axis
        axis = adsk.core.ObjectCollection.create()

        axis.add(adsk.core.Point3D.create(0.01,0,0.36))
        axis.add(adsk.core.Point3D.create(0.01,0,1.13))

        # Draw surface.
        points2 = adsk.core.ObjectCollection.create()

        x = 0.2
        y = 0
        z = -0.38  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.4
        y = 0
        z = -0.46  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.5
        y = 0
        z = -0.55  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.55
        y = 0
        z = -0.67  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.55
        y = 0
        z = -0.74  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.5
        y = 0
        z = -0.89  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.4
        y = 0
        z = -0.99  
        points2.add(adsk.core.Point3D.create(x,y,z))

        x = 0.2
        y = 0
        z = -1.09  
        points2.add(adsk.core.Point3D.create(x,y,z))

        #axis
        axis2 = adsk.core.ObjectCollection.create()

        axis2.add(adsk.core.Point3D.create(0.01,0,-0.36))
        axis2.add(adsk.core.Point3D.create(0.01,0,-1.13))

        #Draw splines
        sketch.sketchCurves.sketchFittedSplines.add(points)
        sketch.sketchCurves.sketchFittedSplines.add(axis)

        sketch.sketchCurves.sketchFittedSplines.add(points2)
        sketch.sketchCurves.sketchFittedSplines.add(axis2)
        
    




    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))