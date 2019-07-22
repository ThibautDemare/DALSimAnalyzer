from subprocess import run, Popen, PIPE
import multiprocessing
import time

def nbContainers():
		result=run("docker ps -aq | wc -l", shell=True, stdout=PIPE).stdout.decode('utf-8')
		return int(result)

nbCpus = multiprocessing.cpu_count()
maxNbSim = 20
nbSimStarted = 1
while nbSimStarted <= maxNbSim:

		resultPath = "run"+str(nbSimStarted)
		run("cp -r ./source ./"+str(resultPath), shell = True)

		command = ["docker run --rm --name gama"+str(nbSimStarted)+" -v $(pwd)/"+str(resultPath)+"/simulation_configs:/simulation_configs -v $(pwd)/"+str(resultPath)+"/output:/output -v $(pwd)/"+str(resultPath)+"/CSV:/CSV -v $(pwd)/"+str(resultPath)+"/bd:/bd -v $(pwd)/"+str(resultPath)+"/DALSim:/DALSim gama > out"+str(nbSimStarted)+" 2>&1"]
		Popen(command, shell = True)
		nbSimStarted += 1
		time.sleep(30) # wait 30 sec to make sure the container is really started
		# Loop if the current number of running containers is greater or equal than the number of available cpus
		while nbCpus <= nbContainers():
				time.sleep(350)
