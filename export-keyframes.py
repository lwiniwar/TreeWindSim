import bpy
from pathlib import Path

outpath = Path(r'PATH/TO/OUTPUT/FILES')

for frame in range(10,60,10):
    print(f"Writing frame {frame}")
    bpy.context.scene.frame_current = frame
    bpy.ops.wm.obj_export(
         filepath=str(outpath /  f"WS0.6ID{frame}.obj"),  # SET THE windspeed HERE
         check_existing=True,
         forward_axis='X',
         up_axis='Z',
         filter_glob="*.obj;*.mtl",
         export_selected_objects=True,
         global_scale=1,
         path_mode='AUTO'
        )

    print(f"Done (frame {frame})")