import os
import subprocess

list = os.listdir(".")
unzipped = []
for f in list:
	if f != __file__ and f.endswith(".zip"):
		subprocess.call(["unzip", f])
		unzipped.append(f)
print "Unzipped file : " + str(unzipped)
print os.listdir(".")
