from server_access_infos import *
import subprocess
import datetime
import os.path

if not os.path.isdir("Results"):
	subprocess.Popen("mkdir Results")
extractionDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
if not os.path.isdir("Results/"+extractionDate):
	subprocess.Popen("mkdir Results/"+extractionDate)

for i in range(1, 9):
	pathCurrentRun = "Results/"+extractionDate+"/run"+str(i)
	subprocess.Popen("mkdir "+pathCurrentRun)
	subprocess.Popen("scp -r "+username+"@"+servername+":~/simus022019/run"+str(i)+"/CSV "+pathCurrentRun)