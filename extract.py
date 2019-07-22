from server_access_infos import *
import subprocess
import datetime
import os.path
import sys

if not os.path.isdir("Results"):
	subprocess.run("mkdir Results")

extractionDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

if not os.path.isdir("Results/"+extractionDate):
	subprocess.run("mkdir Results/"+extractionDate)

for i in range(1, int(sys.argv[2]) + 1):
	pathCurrentRun = "Results/"+extractionDate+"/run"+str(i)
	subprocess.run("mkdir "+pathCurrentRun)
	subprocess.Popen("scp -r "+username+"@"+servername+":"+str(sys.argv[1])+"/run"+str(i)+"/CSV "+pathCurrentRun)
