import os
import subprocess
from pathlib import Path

HELIOS_PATH = r"PATH/TO/helios.exe"
SURVEY_PATH = r"mapleFlight2.xml"
SCENE_PATH = r"mapleScene.xml"

def main(model_dir):
    doit = True
    for model in sorted(Path(model_dir).glob('*.obj')):
        # next one: mapleSceneWS1ID50
        if 'WS1ID50' in str(model.stem):
            doit = True
        if doit is False:
            print(f"Skipping {model.stem}...")
            continue
        name = model.stem
        print(f"Running {model.stem}...")
        new_survey_path = SURVEY_PATH.replace('.xml', f'{name}.xml')
        if Path(new_survey_path).exists():
            print("Survey exists, skipping...")
            continue
        new_scene_path = SCENE_PATH.replace('.xml', f'{name}.xml')
        with open(SURVEY_PATH, 'r') as sp:
            with open(new_survey_path, 'w') as so:
                for line in sp:
                    so.writelines(line.format(
                        scenepath=new_scene_path,
                        name=name
                    ))

        with open(SCENE_PATH, 'r') as sp:
            with open(new_scene_path, 'w') as so:
                for line in sp:
                    so.writelines(line.format(
                        objfile=model
                    ))

        f = subprocess.Popen([
            HELIOS_PATH,
            new_survey_path,
            #'--lasOutput', '1',
        ])

        f.wait()
        os.remove(new_scene_path.replace('.xml', '.scene'))


if __name__ == '__main__':
    print("Starting script...")
    main(model_dir=r'PATH/TO/OBJ_MODELS')