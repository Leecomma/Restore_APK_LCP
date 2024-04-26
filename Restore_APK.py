import os
import subprocess
import urllib.request
import time


class Restore:
    def __init__(self):
        self.des_path = " "


Restore = Restore()

#___ADD_NEW_FUNCTION__
# def check_install_adb():
    # try:
       #  subprocess.run(["adb", "--verison", check==True])
      #   print("ADB installed -> OK")
    # except subprocess.CalledProcessError as e:
       #  print(f"Error, please install adb: {e}\n")

def prepare_to_install():

    # Instruction
    print("\nScript tested on Linux (Ubuntu 20.04) with adb tools, if adb not installed -> use 1\n")
    print("(1).(Not work) Install adb and run script\n(2).(work)Run script without install adb\n(3).Exit\n")

    # Start manu
    user_input = input("Write option 1,2,3 in console -> ")
    if user_input == "1":
        print("adb installing\n")
    elif user_input == "2":
        print("run script\n")
    else: 
        print("Exit Script\n")
        exit()

    # Show devices ADB
    subprocess.run(["adb", "devices"])
    time.sleep(3)

    # set ROOT on device
    # subprocess.run(["adb", "root"])
    # time.sleep(3)

    # Download APK
    url = "___FULL_HTTP_LINK_To_APP___" #add link HTTP to file 
    apk_filename = os.path.basename(url)

    # Ask USER set path
    print("STAGE 1/5")
    Restore.des_path = input("Write Path: Example /home/s1/Desktop ->")
    print(f"Downloading file APK to {Restore.des_path}\n")

    # split full pass (path + name APK file)
    Restore.des_path = os.path.join(Restore.des_path, apk_filename)

    # Download file APK to PC
    urllib.request.urlretrieve(url, Restore.des_path)
    print("STAGE 2/5")
    print(f"Success download to {Restore.des_path}\n")

    # if all ok, 1 func will return true and start 2 func
    return True


def remove_app():

    print("STAGE 3/5")

    # list of commands to delete apps
    commands = ["___ADD___", "___Second_ADD___"] #add two name of APK_APP

    for command in commands:
        try:
            subprocess.run(["adb", "shell", "pm", "uninstall", command], check=True)
            print(f"Uninstalled old app: {command}\n")
        except subprocess.CalledProcessError as e:
            print(f"Error {command}: {e}\n")

        time.sleep(1)

    # reboot tablet (commented because need rewrite)
    # subprocess.run(["adb", "reboot"])

    # if 2 func is ok, will return true and start 3 func
    return True


def final_install_apk():

    print("STAGE 4/5")

    # install apk to LCP10
    try:
        subprocess.run(['adb', 'install', Restore.des_path], check=True)
        print("Installed new APP\n")
    except subprocess.CalledProcessError as e:
        print(f"Error installing APK: {e}\n")

    # final stage
    print("STAGE FINAL")
    print("after REBOOT you can disconnect LCP from PC")
    time.sleep(3)
    subprocess.run(["adb", "reboot"])

if prepare_to_install() and remove_app():
    final_install_apk()
else:
    print("Error of func") 
        # Error of func means some of func not complete
   #  print("Error adb not check ")

