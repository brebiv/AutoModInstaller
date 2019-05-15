import shutil
import glob
import os

def main():
    cwd = os.getcwd()
    print("Curent workspace: " ,cwd)
    if os.path.isdir('mods'):
        mods = glob.glob('mods/*.jar')
        k = input("If you want to see mods enter 'y': ")
        if k == 'y':
            for mod in mods:
                print(mod)
            del k
        mods_folder = os.path.abspath('mods')
        print("Curent mods folder: ", mods_folder)
        if os.path.exists(f"{os.environ['APPDATA']}/.minecraft"):
            minecraft_path = f"{os.environ['APPDATA']}/.minecraft"
            print("Minecraft folder: ", minecraft_path)
            if os.path.exists(f"{minecraft_path}/mods"):
                mods_target = os.path.abspath(f"{minecraft_path}/mods")
                print("Minecraft mods folder: ", mods_target)
                for mod in mods:
                    try:
                        shutil.copy(mod, mods_target)
                    except:
                        print(f"I can't copy {mod}, sorry :(")
                    else:
                        print("Mod installed successfully")

            else:
                print("Please install forge and run minecraft first.")
        else:
            print("Please install minecraft.")
    else:
        os.mkdir('mods')
        print("Put mods in mods folder please.")
    a = input()

if __name__ == "__main__":
    main()