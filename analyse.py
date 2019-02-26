import csv
import os
import subprocess

dataType = ["average_costs", "average_time_to_be_delivered", "average_time_to_deliver", "averageThreshold", "competition_between_LH_Antwerp", "distribution_nb_FC_per_LSP", "nb_stocks_awaiting", "number_empty_stock_final_dest", "number_empty_stock_warehouses", "share_leaving_quantities_pet_transport_mode_Antwerpen", "share_leaving_quantities_pet_transport_mode_Basse-Normandie", "share_leaving_quantities_pet_transport_mode_Centre", "share_leaving_quantities_pet_transport_mode_Haute-Normandie", "share_leaving_quantities_pet_transport_mode_Ile-de-France", "share_leaving_quantities_pet_transport_mode_Picardie", "share_leaving_vehicles_per_transport_mode_Antwerpen", "share_leaving_vehicles_per_transport_mode_Basse-Normandie", "share_leaving_vehicles_per_transport_mode_Centre", "share_leaving_vehicles_per_transport_mode_Haute-Normandie", "share_leaving_vehicles_per_transport_mode_Ile-de-France", "share_leaving_vehicles_per_transport_mode_Picardie", "share_port_origin_region_Antwerpen", "share_port_origin_region_Basse-Normandie", "share_port_origin_region_Centre", "share_port_origin_region_Haute-Normandie", "share_port_origin_region_Ile-de-France", "share_port_origin_region_Picardie", "share_transport_mode_Antwerpen", "share_transport_mode_Basse-Normandie", "share_transport_mode_Centre", "share_transport_mode_Haute-Normandie", "share_transport_mode_Ile-de-France", "share_transport_mode_Picardie", "share_transport_mode_quantities_Antwerpen", "share_transport_mode_quantities_Basse-Normandie", "share_transport_mode_quantities_Centre", "share_transport_mode_quantities_Haute-Normandie", "share_transport_mode_quantities_Ile-de-France", "share_transport_mode_quantities_Picardie", "share_transport_mode_quantities", "share_transport_mode", "stocks_final_dests", "stocks_warehouses", "strat1_threshold_adoption_share", "strat2_threshold_adoption_share", "strat3_threshold_adoption_share", "strat4_threshold_adoption_share", "strategies_adoption_share", "traffic_evolution_CSN"]

extractions = os.listdir("./Results")
for ext in extractions:
	averageData = {}

	if not os.path.isdir("./averageResults/"):
		subprocess.run("mkdir averageResults/")

	if not os.path.isdir("./averageResults/"+ext):
		subprocess.run("mkdir averageResults/"+ext)

	for i in range(1, 9):
		path = "./Results/"+ext+"/run"+str(i)+"/CSV/"
		files = os.listdir(path)
		for name in files:
			# Find the right keys
			key = ""
			for k in dataType:
				if k in name:
					key = k
					break

			if key not in averageData.keys():
				averageData[key] = {}

			# Fill the "average" data set with the current one
			with open(path+name) as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=';')
				for row in csv_reader:
					if len(row) > 0:
						if row[0] not in averageData[key].keys():
							averageData[key][row[0]] = []

						averageData[key][row[0]] = [0.0] * (len(row) - 1)
						for d in range(1, len(row)-1):
							averageData[key][row[0]][d-1] = averageData[key][row[0]][d-1] + float(row[d])

	for dt in dataType:
		with open("./averageResults/"+ext+"/"+dt+".csv",mode='w',newline='') as average_data_file:
			writer = csv.writer(average_data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			for step in averageData[dt]:
				row = []
				row.append(step)
				for i in range(0, len(averageData[dt][step])):
					row.append(averageData[dt][step][i] / 8.0)
				writer.writerow(row)