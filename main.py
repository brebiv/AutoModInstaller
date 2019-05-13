import shutil
import glob
import os

cwd = os.getcwd()
print("Curent cwd: ", cwd)

if os.path.isdir('mods'):
    mods_path = os.path.abspath('mods')
    mods = glob.glob(f'{mods_path}/*.jar')
    print(mods)
    print("Folder for mods: ", mods_path)
    app_data_path = os.environ['APPDATA']
    try:
        minecraft_path = str(glob.glob(f"{app_data_path}/.minecraft"))
        print("Minecraft_path = ", minecraft_path)
    except:
        print("Unknown error :(")
    else:
        if minecraft_path == []:
            print("Please install minecraft")
        else:
            os.chdir(minecraft_path[2:-2])
            print(os.getcwd())
            if glob.glob('mods') != []:
                mods_folder = os.path.abspath('mods')
                print("Mods folder: ", mods_folder)
                for mod in mods:
                    mod_name = mod
                    shutil.copy(mod_name, mods_folder)
            else:
                print("Install forge and launch minecraft please.")

else:
    os.mkdir('mods')
    print("Пожалуйста добавьте моды в папку")
a = input()