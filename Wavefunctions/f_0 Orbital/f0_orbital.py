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
        
        x = 0.01
        y = 0
        z = 0.65
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.57
        z = 1.0
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.98
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.30
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.52
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.62
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.55
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.25
        z = z + 0.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.94
        z = 4.25
        points.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.01
        z = 4.5
        points.add(adsk.core.Point3D.create(x,y,z))
        
        
        
        
        # Draw surface.
        points2 = adsk.core.ObjectCollection.create()
        
        x = 0.01
        y = 0
        z = -0.65
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.57
        z = -1.0
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.98
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.30
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.52
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.62
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.55
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 1.25
        z = z - 0.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.94
        z = -4.25
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        x = 0.01
        z = -4.5
        points2.add(adsk.core.Point3D.create(x,y,z))
        
        
        
        #Draw splines
        sketch.sketchCurves.sketchFittedSplines.add(points)
        sketch.sketchCurves.sketchFittedSplines.add(points2)
    
    
    
    
    
    
    
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

