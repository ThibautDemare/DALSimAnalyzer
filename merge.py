import csv
import os
import subprocess

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
 
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False


dataType = ["average_costs", "average_time_to_be_delivered", "average_time_to_deliver", "averageThreshold", "competition_between_LH_Antwerp", "distribution_nb_FC_per_LSP", "nb_stocks_awaiting", "number_empty_stock_final_dest", "number_empty_stock_warehouses", "share_leaving_quantities_per_transport_mode_Antwerpen", "share_leaving_quantities_per_transport_mode_Le Havre", "share_leaving_quantities_per_transport_mode_Basse-Normandie", "share_leaving_quantities_per_transport_mode_Centre", "share_leaving_quantities_per_transport_mode_Haute-Normandie", "share_leaving_quantities_per_transport_mode_Ile-de-France", "share_leaving_quantities_per_transport_mode_Picardie", "share_leaving_vehicles_per_transport_mode_Antwerpen", "share_leaving_vehicles_per_transport_mode_Le Havre", "share_leaving_vehicles_per_transport_mode_Basse-Normandie", "share_leaving_vehicles_per_transport_mode_Centre", "share_leaving_vehicles_per_transport_mode_Haute-Normandie", "share_leaving_vehicles_per_transport_mode_Ile-de-France", "share_leaving_vehicles_per_transport_mode_Picardie", "share_port_origin_region_Antwerpen", "share_port_origin_region_Le Havre", "share_port_origin_region_Basse-Normandie", "share_port_origin_region_Centre", "share_port_origin_region_Haute-Normandie", "share_port_origin_region_Ile-de-France", "share_port_origin_region_Picardie", "share_transport_mode_Antwerpen", "share_transport_mode_Le Havre", "share_transport_mode_Basse-Normandie", "share_transport_mode_Centre", "share_transport_mode_Haute-Normandie", "share_transport_mode_Ile-de-France", "share_transport_mode_Picardie", "share_transport_mode_quantities_Antwerpen", "share_transport_mode_quantities_Le Havre", "share_transport_mode_quantities_Basse-Normandie", "share_transport_mode_quantities_Centre", "share_transport_mode_quantities_Haute-Normandie", "share_transport_mode_quantities_Ile-de-France", "share_transport_mode_quantities_Picardie", "share_transport_mode_quantities", "share_transport_mode", "stocks_final_dests", "stocks_warehouses", "strat1_threshold_adoption_share", "strat2_threshold_adoption_share", "strat3_threshold_adoption_share", "strat4_threshold_adoption_share", "strategies_adoption_share", "traffic_evolution_CSN"]

extractions = os.listdir("./Results")
for ext in extractions:
	averageData = {}

	if not os.path.isdir("./averageResults/"):
		subprocess.run("mkdir averageResults/")

	if not os.path.isdir("./averageResults/"+ext):
		subprocess.run("mkdir averageResults/"+ext)

	# We loop over the 8 simulation runs
	# and we read each CSV files to sum every results
	for i in range(1, 9):
		path = "./Results/"+ext+"/run"+str(i)+"/CSV/"
		files = os.listdir(path)
		for name in files:
			# Find the right keys (i.e. the right kind of result)
			key = ""
			for k in dataType:
				if k in name:
					key = k
					break
			if key: # this test is usefull when debug the script with a subset of dataTypes
				if key not in averageData.keys():
					averageData[key] = {}

				# Fill the "average" data set with the current one
				with open(path+name) as csv_file:
					csv_reader = csv.reader(csv_file, delimiter=';')
					for row in csv_reader: # read each line of the CSV file
						if len(row) > 0:
							if row[0] not in averageData[key].keys(): # if this step doesn't exist, we create it
								averageData[key][row[0]] = []
							for d in range(0, len(row)):
								if is_number(row[d]): # Some lines end with ';', so python consider the last element as an empty element
									if d >= len(averageData[key][row[0]]): # we create a new element of this row
										averageData[key][row[0]].append(float(row[d]))
									else:
										averageData[key][row[0]][d] = float(averageData[key][row[0]][d]) + float(row[d]) # we make the sum between the previous elements and the new one

	# And now we can compute the average of all these data
	for dt in dataType:
		# We create a new CSV file for each kind of result (i.e. dataType)
		with open("./averageResults/"+ext+"/"+dt+".csv",mode='w',newline='') as average_data_file:
			writer = csv.writer(average_data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			for step in averageData[dt]:
				row = []
				for i in range(0, len(averageData[dt][step])):
					if isinstance(averageData[dt][step][i], (int, float, complex)):
						row.append(float(averageData[dt][step][i]) / 8.0)
					else:
						row.append(float(averageData[dt][step][i]))
				writer.writerow(row)