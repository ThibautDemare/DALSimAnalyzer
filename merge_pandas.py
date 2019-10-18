import os
import pandas as pd

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

dataType = ["average_costs", "average_time_to_be_delivered", "average_time_to_deliver", "averageThreshold", "competition_between_LH_Antwerp",  "nb_stocks_awaiting", "number_empty_stock_final_dest", "number_empty_stock_warehouses", "share_leaving_quantities_per_transport_mode_Antwerpen", "share_leaving_quantities_per_transport_mode_Le Havre", "share_leaving_quantities_per_transport_mode_Basse-Normandie", "share_leaving_quantities_per_transport_mode_Centre", "share_leaving_quantities_per_transport_mode_Haute-Normandie", "share_leaving_quantities_per_transport_mode_Ile-de-France", "share_leaving_quantities_per_transport_mode_Picardie", "share_leaving_vehicles_per_transport_mode_Antwerpen", "share_leaving_vehicles_per_transport_mode_Le Havre", "share_leaving_vehicles_per_transport_mode_Basse-Normandie", "share_leaving_vehicles_per_transport_mode_Centre", "share_leaving_vehicles_per_transport_mode_Haute-Normandie", "share_leaving_vehicles_per_transport_mode_Ile-de-France", "share_leaving_vehicles_per_transport_mode_Picardie", "share_port_origin_region_Antwerpen", "share_port_origin_region_Le Havre", "share_port_origin_region_Basse-Normandie", "share_port_origin_region_Centre", "share_port_origin_region_Haute-Normandie", "share_port_origin_region_Ile-de-France", "share_port_origin_region_Picardie", "share_transport_mode_Antwerpen", "share_transport_mode_Le Havre", "share_transport_mode_Basse-Normandie", "share_transport_mode_Centre", "share_transport_mode_Haute-Normandie", "share_transport_mode_Ile-de-France", "share_transport_mode_Picardie", "share_transport_mode_quantities_Antwerpen", "share_transport_mode_quantities_Le Havre", "share_transport_mode_quantities_Basse-Normandie", "share_transport_mode_quantities_Centre", "share_transport_mode_quantities_Haute-Normandie", "share_transport_mode_quantities_Ile-de-France", "share_transport_mode_quantities_Picardie", "share_transport_mode_quantities", "share_transport_mode", "stocks_final_dests", "stocks_warehouses", "strat1_threshold_adoption_share", "strat2_threshold_adoption_share", "strat3_threshold_adoption_share", "strat4_threshold_adoption_share", "strategies_adoption_share", "traffic_evolution_CSN", "vehicles_occupancy_road", "vehicles_occupancy_river", "vehicles_occupancy_maritime", "vehicles_occupancy_secondary"]
#"distribution_nb_FC_per_LSP",

if not os.path.exists("./averageResults-pandas/"):
	os.makedirs("./averageResults-pandas/")

extractions = os.listdir("./Results")
for ext in extractions:
	dataFrames = {}

	if not os.path.exists("./averageResults-pandas/"+ext):
		os.makedirs("./averageResults-pandas/"+ext)

	# We loop over the 8 simulation runs
	# and we read each CSV files to sum every results
	for run in os.listdir("./Results/"+ext+"/"):
		path = "./Results/"+ext+"/"+run+"/CSV/"
		for name in os.listdir(path):
			# Find the right keys (i.e. the right kind of result)
			key = ""
			for k in dataType:
				if k in name:
					key = k
					break
			if key: # this test is usefull when debug the script with a subset of dataTypes
				if key not in dataFrames.keys():
					dataFrames[key] = pd.read_csv(path+name, sep=";", skip_blank_lines=True)
				else:
					tmp = pd.read_csv(path+name, sep=";", skip_blank_lines=True)
					frames = [dataFrames[key], tmp]
					dataFrames[key] = pd.concat(frames, sort=True, ignore_index=True)

	# And now we can compute the average of all these data
	for dfName in dataFrames.keys():
		print(dfName)
		dataFrames[dfName] = dataFrames[dfName].dropna(axis=1,how='all') # This line deletes columns when they only contains null values => should only happen with older versions of DALSim
		dataFrames[dfName] = dataFrames[dfName].groupby('step').mean()
		dataFrames[dfName].to_csv("./averageResults-pandas/"+ext+"/"+dfName+".csv", index=True, sep=";")