#Author-Vaishnav
#Description-Orbital

import adsk.core, adsk.fusion, adsk.cam, traceback

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
        points2 = adsk.core.ObjectCollection.create()
        points3 = adsk.core.ObjectCollection.create()
        points4 = adsk.core.ObjectCollection.create()


        # Define the points the spline with fit through.
        points.add(adsk.core.Point3D.create(0, 13.6,0))
        points.add(adsk.core.Point3D.create(1, 13.5,0))
        points.add(adsk.core.Point3D.create(4, 11.5,0))
        points.add(adsk.core.Point3D.create(6.6, 9.25,0))
        points.add(adsk.core.Point3D.create(4, 6.35,0))
        points.add(adsk.core.Point3D.create(1, 2.4,0))
        points.add(adsk.core.Point3D.create(0,1.95,0))

        points2.add(adsk.core.Point3D.create(0, -13.6,0))
        points2.add(adsk.core.Point3D.create(1, -13.5,0))
        points2.add(adsk.core.Point3D.create(4, -11.5,0))
        points2.add(adsk.core.Point3D.create(6.6, -9.25,0))
        points2.add(adsk.core.Point3D.create(4, -6.35,0))
        points2.add(adsk.core.Point3D.create(1, -2.4,0))
        points2.add(adsk.core.Point3D.create(0, -1.95,0))

        points3.add(adsk.core.Point3D.create(-13.6,0,0))
        points3.add(adsk.core.Point3D.create(-13.5,1,0))
        points3.add(adsk.core.Point3D.create(-11.5,4,0))
        points3.add(adsk.core.Point3D.create(-9.25,6.6,0))
        points3.add(adsk.core.Point3D.create(-6.35,4,0))
        points3.add(adsk.core.Point3D.create(-2.4,1,0))
        points3.add(adsk.core.Point3D.create(-1.95,0,0))

        points4.add(adsk.core.Point3D.create(13.6,0,0))
        points4.add(adsk.core.Point3D.create(13.5,1,0))
        points4.add(adsk.core.Point3D.create(11.5,4,0))
        points4.add(adsk.core.Point3D.create(9.25,6.6,0))
        points4.add(adsk.core.Point3D.create(6.35,4,0))
        points4.add(adsk.core.Point3D.create(2.4,1,0))
        points4.add(adsk.core.Point3D.create(1.95,0,0))



        lines = sketch.sketchCurves.sketchLines;
        line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 13.6, 0), adsk.core.Point3D.create(0, 1.95, 0))
        line2 = lines.addByTwoPoints(adsk.core.Point3D.create(0, -13.6, 0), adsk.core.Point3D.create(0, -1.95, 0))
        line3 = lines.addByTwoPoints(adsk.core.Point3D.create(13.6,0, 0), adsk.core.Point3D.create(1.95,0, 0))
        line4 = lines.addByTwoPoints(adsk.core.Point3D.create(-13.6,0, 0), adsk.core.Point3D.create(-1.95,0, 0))


        # Create the spline.
        sketch.sketchCurves.sketchFittedSplines.add(points)
        sketch.sketchCurves.sketchFittedSplines.add(points2)
        sketch.sketchCurves.sketchFittedSplines.add(points3)
        sketch.sketchCurves.sketchFittedSplines.add(points4)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))