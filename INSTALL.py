#! /usr/bin/python

import os
import shutil
import stat

def startcreation():
	desktopfile = "/usr/share/applications/battery_percentage.desktop"
	executable = "/usr/bin/battery_percentage"

	desktop = open(desktopfile,"w")
	desktop.write("""
[Desktop Entry]
Version=1.0
Type=Application
Name=Battery Percentage
GenericName=Bettery Percentage
Comment=Launch Battery Percentage Applet
Icon=/usr/share/icons/battery_percentage/icon.png
Categories=Customization;
Exec=battery_percentage
TryExec=battery_percentage
Terminal=false""")

	desktop.close()

	imageDir = "/usr/share/icons/battery_percentage/"

	if not os.path.exists(imageDir):
		os.makedirs(imageDir)
	
	currentdir = os.path.dirname(os.path.realpath(__file__))

	shutil.copy(currentdir + "/icon.png", "/usr/share/icons/battery_percentage/icon.png")
	shutil.copy(currentdir + "/applet.py", executable)

	# change the permissions of the files
	st = os.stat(desktopfile)
	os.chmod(desktopfile, st.st_mode | stat.S_IEXEC)
	st = os.stat(executable)
	os.chmod(executable, st.st_mode | stat.S_IEXEC)


if __name__ == "__main__":
	startcreation()