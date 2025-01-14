#Author-Vaishnav Rao
#Description-Atomic orbital

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
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

        # Create an object collection for the points.
        points = adsk.core.ObjectCollection.create()

        # Define the points the spline with fit through.
        points.add(adsk.core.Point3D.create(0, 0, 0.809))
        points.add(adsk.core.Point3D.create(0.1, 0, 0.7))
        points.add(adsk.core.Point3D.create(0.5,0, 0.0.62))
        points.add(adsk.core.Point3D.create(0, 0, 0))
        points.add(adsk.core.Point3D.create(0.4, 0, 0.3))
        points.add(adsk.core.Point3D.create(0, 0, 0.89))

        # Create the spline.
        sketch.sketchCurves.sketchFittedSplines.add(points)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))