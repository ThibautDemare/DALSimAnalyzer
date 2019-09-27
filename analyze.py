import os
import subprocess

# The different kinds of results and the arguments associated to each result and necessary for the GnuPlot script
dataType = {
	"average_costs":
		{"dataFile":"average_costs.csv", "outfile":"average_costs", "xlab":"Time (hour)", "ylab":"Average costs", "mainTitle":"Costs", 
		"curve1Label":"Average costs"},
	"average_time_to_be_delivered":
		{"dataFile":"average_time_to_be_delivered.csv", "outfile":"average_time_to_be_delivered", "xlab":"Time (hour)", "ylab":"time (hour)", "mainTitle":"Average time to be delivered (to final consignees)",
		"curve1Label":"Average time to be delivered (to final consignee)"},
	"average_time_to_deliver":
		{"dataFile":"average_time_to_deliver.csv", "outfile":"average_time_to_deliver", "xlab":"Time (hour)", "ylab":"time (hour)", "mainTitle":"Average time to be delivered (to warehouses)",
		"curve1Label":"Average time to be delivered (to warehouses)"},
	"averageThreshold":
		{"dataFile":"averageThreshold.csv", "outfile":"averageThreshold", "xlab":"Time (hour)", "ylab":"Threshold of selected LSPs (en %)", "mainTitle":"Average threshold of selected LSPs",
		"curve1Label":"Average threshold of selected LSPs"},
	"competition_between_LH_Antwerp":
		{"dataFile":"competition_between_LH_Antwerp.csv", "outfile":"competition_between_LH_Antwerp", "xlab":"Time (hour)", "ylab":"Number of LSPs", "mainTitle":"Competition between Le Havre and Antwerp",
		"curve1Label":"Number of LSPs who selected Le Havre", "curve2Label":"Number of LSPs who selected Antwerp"},

	"nb_stocks_awaiting":
		{"dataFile":"nb_stocks_awaiting.csv", "outfile":"nb_stocks_awaiting", "xlab":"Time (hour)", "ylab":"Number of stocks", "mainTitle":"Number of stocks awaiting to enter or leave building",
		"curve1Label":"Number of stocks awaiting to enter building of final consignee", "curve2Label":"Number of stocks awaiting to enter warehouses",
		"curve3Label":"Number of stocks awaiting to leave warehouses", "curve4Label":"Number of stocks awaiting to leave provider"},
	"number_empty_stock_final_dest":
		{"dataFile":"number_empty_stock_final_dest.csv", "outfile":"number_empty_stock_final_dest", "xlab":"Time (hour)", "ylab":"Number of stocks", "mainTitle":"Number of stock shortages in final consignees",
		"curve1Label":"Number of stock shortages in final consignees"},
	"number_empty_stock_warehouses":
		{"dataFile":"number_empty_stock_warehouses.csv", "outfile":"number_empty_stock_warehouses", "xlab":"Time (hour)", "ylab":"Number of stocks", "mainTitle":"Number of stock shortages in warehouses",
		"curve1Label":"Number of stock shortages in warehouses"},
	"traffic_evolution_CSN":
		{"dataFile":"traffic_evolution_CSN.csv", "outfile":"traffic_evolution_CSN", "xlab":"Time (hour)", "ylab":"Goods quantities on CSN", "mainTitle":"Evolution of goods traffic on the CSN", "curve1Label":"Goods traffic on the CSN"},

	"stocks_final_dests":
		{"dataFile":"stocks_final_dests.csv", "outfile":"stocks_final_dests", "xlab":"Time (hour)", "ylab":"Surface (in m²)", "mainTitle":"Average stock quantities in final consignees",
		"curve1Label":"Total stock quantities in final consignees", "curve2Label":"Total free surface in final consignees"},
	"stocks_warehouses":
		{"dataFile":"stocks_warehouses.csv", "outfile":"stocks_warehouses", "xlab":"Time (hour)", "ylab":"Surface (in m²)", "mainTitle":"Average stock quantities in warehouses",
		"curve1Label":"Total stock quantities in warehouses", "curve2Label":"Total free surface in warehouses"},

	"share_leaving_quantities_per_transport_mode_Antwerpen":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Antwerpen.csv", "outfile":"share_leaving_quantities_per_transport_mode_Antwerpen", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Antwerp)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Le Havre":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Le Havre.csv", "outfile":"share_leaving_quantities_per_transport_mode_Le Havre", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Le Havre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Basse-Normandie":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Basse-Normandie.csv", "outfile":"share_leaving_quantities_per_transport_mode_Basse-Normandie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Basse-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Centre":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Centre.csv", "outfile":"share_leaving_quantities_per_transport_mode_Centre", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Centre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Haute-Normandie":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Haute-Normandie.csv", "outfile":"share_leaving_quantities_per_transport_mode_Haute-Normandie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Le Havre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Ile-de-France":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Ile-de-France.csv", "outfile":"share_leaving_quantities_per_transport_mode_Ile-de-France", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of share_transport_mode_Ile-de-France)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_quantities_per_transport_mode_Picardie":
		{"dataFile":"share_leaving_quantities_per_transport_mode_Picardie.csv", "outfile":"share_leaving_quantities_per_transport_mode_Picardie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		 "mainTitle":"Average quantities of goods per transport mode (Region of Picardie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"share_leaving_vehicles_per_transport_mode_Antwerpen":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Antwerpen.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Antwerpen", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Antwerp)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Le Havre":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Le Havre.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Le Havre", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Le Havre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Basse-Normandie":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Basse-Normandie.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Basse-Normandie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Basse-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Centre":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Centre.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Centre", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Centre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Haute-Normandie":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Haute-Normandie.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Haute-Normandie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Haute-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Ile-de-France":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Ile-de-France.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Ile-de-France", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Ile-de-France)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_leaving_vehicles_per_transport_mode_Picardie":
		{"dataFile":"share_leaving_vehicles_per_transport_mode_Picardie.csv", "outfile":"share_leaving_vehicles_per_transport_mode_Picardie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		 "mainTitle":"Average number of moving vehicles per transport mode (Region of Picardie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"share_port_origin_region_Antwerpen":
		{"dataFile":"share_port_origin_region_Antwerpen.csv", "outfile":"share_port_origin_region_Antwerpen", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Antwerp)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Le Havre":
		{"dataFile":"share_port_origin_region_Le Havre.csv", "outfile":"share_port_origin_region_Le Havre", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Le Havre)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Basse-Normandie":
		{"dataFile":"share_port_origin_region_Basse-Normandie.csv", "outfile":"share_port_origin_region_Basse-Normandie", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Basse-Normandie)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Centre":
		{"dataFile":"share_port_origin_region_Centre.csv", "outfile":"share_port_origin_region_Centre", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Centre)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Haute-Normandie":
		{"dataFile":"share_port_origin_region_Haute-Normandie.csv", "outfile":"share_port_origin_region_Haute-Normandie", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Haute-Normandie)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Ile-de-France":
		{"dataFile":"share_port_origin_region_Ile-de-France.csv", "outfile":"share_port_origin_region_Ile-de-France", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Ile-de-France)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},
	"share_port_origin_region_Picardie":
		{"dataFile":"share_port_origin_region_Picardie.csv", "outfile":"share_port_origin_region_Picardie", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Average number of selected LSPs according to their associated port (Region of Picardie)",
		"curve1Label":"Number of LSPs who selected Antwerp", "curve2Label":"Number of LSPs who selected Le Havre"},

	"share_transport_mode_Antwerpen":
		{"dataFile":"share_transport_mode_Antwerpen.csv", "outfile":"share_transport_mode_Antwerpen", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Antwerp)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Le Havre":
		{"dataFile":"share_transport_mode_Le Havre.csv", "outfile":"share_transport_mode_Le Havre", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Le Havre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Basse-Normandie":
		{"dataFile":"share_transport_mode_Basse-Normandie.csv", "outfile":"share_transport_mode_Basse-Normandie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Basse-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Centre":
		{"dataFile":"share_transport_mode_Centre.csv", "outfile":"share_transport_mode_Centre", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Centre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Haute-Normandie":
		{"dataFile":"share_transport_mode_Haute-Normandie.csv", "outfile":"share_transport_mode_Haute-Normandie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Haute-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Ile-de-France":
		{"dataFile":"share_transport_mode_Ile-de-France.csv", "outfile":"share_transport_mode_Ile-de-France", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Ile-de-France)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_Picardie":
		{"dataFile":"share_transport_mode_Picardie.csv", "outfile":"share_transport_mode_Picardie", "xlab":"Time (hour)", "ylab":"Number of vehicles",
		"mainTitle":"Average number of vehicles per transport mode (Region of Picardie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"share_transport_mode_quantities_Antwerpen":
		{"dataFile":"share_transport_mode_quantities_Antwerpen.csv", "outfile":"share_transport_mode_quantities_Antwerpen", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Antwerp)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Le Havre":
		{"dataFile":"share_transport_mode_quantities_Le Havre.csv", "outfile":"share_transport_mode_quantities_Le Havre", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Le Havre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Basse-Normandie":
		{"dataFile":"share_transport_mode_quantities_Basse-Normandie.csv", "outfile":"share_transport_mode_quantities_Basse-Normandie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Basse-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Centre":
		{"dataFile":"share_transport_mode_quantities_Centre.csv", "outfile":"share_transport_mode_quantities_Centre", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Centre)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Haute-Normandie":
		{"dataFile":"share_transport_mode_quantities_Haute-Normandie.csv", "outfile":"share_transport_mode_quantities_Haute-Normandie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Haute-Normandie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Ile-de-France":
		{"dataFile":"share_transport_mode_quantities_Ile-de-France.csv", "outfile":"share_transport_mode_quantities_Ile-de-France", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Ile-de-France)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},
	"share_transport_mode_quantities_Picardie":
		{"dataFile":"share_transport_mode_quantities_Picardie.csv", "outfile":"share_transport_mode_quantities_Picardie", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode (Region of Picardie)",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"share_transport_mode_quantities":
		{"dataFile":"share_transport_mode_quantities.csv", "outfile":"share_transport_mode_quantities", "xlab":"Time (hour)", "ylab":"Quantities of goods",
		"mainTitle":"Average quantities of carried goods per transport mode",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"share_transport_mode":
		{"dataFile":"share_transport_mode.csv", "outfile":"share_transport_mode", "xlab":"Time (hour)", "ylab":"Number of vehicles", "mainTitle":"Average number of vehicles per transport mode",
		"curve1Label":"Road", "curve2Label":"River",
		"curve3Label":"Maritime"},

	"strat1_threshold_adoption_share":
		{"dataFile":"strat1_threshold_adoption_share.csv", "outfile":"strat1_threshold_adoption_share", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Evolution of strategies adopted to restock (Strategy used to select warehouses: biased random selection)",
		"curve1Label":"Low threshold", "curve2Label":"Strategy :  Low to medium threshold",
		"curve3Label":"Medium to high threshold", "curve4Label":"High threshold",
		"color1":"#077f2f", "color2":"#29cc5f", "color3":"#33ff77", "color4":"#63ff97"},
	"strat2_threshold_adoption_share":
		{"dataFile":"strat2_threshold_adoption_share.csv", "outfile":"strat2_threshold_adoption_share", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Evolution of strategies adopted to restock (Strategy used to select warehouses: accessibility)",
		"curve1Label":"Low threshold", "curve2Label":"Strategy :  Low to medium threshold",
		"curve3Label":"Medium to high threshold", "curve4Label":"High threshold",
		"color1":"#7f0b00", "color2":"#cc3629", "color3":"#ff4433", "color4":"#ff7063"},
	"strat3_threshold_adoption_share":
		{"dataFile":"strat3_threshold_adoption_share.csv", "outfile":"strat3_threshold_adoption_share", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Evolution of strategies adopted to restock (Strategy used to select warehouses: closest/largest)",
		"curve1Label":"Low threshold", "curve2Label":"Strategy :  Low to medium threshold",
		"curve3Label":"Medium to high threshold", "curve4Label":"High threshold",
		"color1":"#001e7f", "color2":"#3755cc", "color3":"#456aff", "color4":"#89a1ff"},
	"strat4_threshold_adoption_share":
		{"dataFile":"strat4_threshold_adoption_share.csv", "outfile":"strat4_threshold_adoption_share", "xlab":"Time (hour)", "ylab":"Number of selected LSPs",
		"mainTitle":"Evolution of strategies adopted to restock (Strategy used to select warehouses: pure random)",
		"curve1Label":"Low threshold", "curve2Label":"Strategy :  Low to medium threshold",
		"curve3Label":"Medium to high threshold", "curve4Label":"High threshold",
		"color1":"#70267f", "color2":"#a800cc", "color3":"#d200ff", "color4":"#e04cff"},

	"strategies_adoption_share":
		{"dataFile":"strategies_adoption_share.csv", "outfile":"strategies_adoption_share", "xlab":"Time (hour)", "ylab":"Number of selected LSPs", "mainTitle":"Evolution of strategies adopted to select warehouses",
		"curve1Label":"Strategy : biased random selection", "curve2Label":"Strategy :  accessibility",
		"curve3Label":"Strategy : closest/largest", "curve4Label":"Strategy : pure random selection"},

	"vehicles_occupancy_road":
		{"dataFile":"vehicles_occupancy_road.csv", "outfile":"vehicles_occupancy_road", "xlab":"Time (hour)", "ylab":"Goods quantity", "mainTitle":"Road vehicles occupancy",
		"curve1Label":"Road vehicles occupancy - "}
	"vehicles_occupancy_river":
		{"dataFile":"vehicles_occupancy_river.csv", "outfile":"vehicles_occupancy_river", "xlab":"Time (hour)", "ylab":"Goods quantity", "mainTitle":"River vehicles occupancy",
		"curve1Label":"River vehicles occupancy"}
	"vehicles_occupancy_maritime":
		{"dataFile":"vehicles_occupancy_maritime.csv", "outfile":"vehicles_occupancy_maritime", "xlab":"Time (hour)", "ylab":"Goods quantity", "mainTitle":"Maritime vehicles occupancy",
		"curve1Label":"Maritime vehicles occupancy"}
	"vehicles_occupancy_secondary":
		{"dataFile":"vehicles_occupancy_secondary.csv", "outfile":"vehicles_occupancy_secondary", "xlab":"Time (hour)", "ylab":"Goods quantity", "mainTitle":"Secondary vehicles occupancy",
		"curve1Label":"Secondary vehicles occupancy"}

}

if not os.path.isdir("Charts-pandas"):
	subprocess.run("mkdir Charts-pandas")

for ext in os.listdir("./averageResults-pandas"):

	if not os.path.isdir("Charts-pandas/"+ext):
		subprocess.run("mkdir Charts-pandas/"+ext)

	for csvName in os.listdir("./averageResults-pandas/"+ext):

		# get the key associated to this CSV
		########################
		# Use this when with every results and not subset => 
		key = os.path.splitext(csvName)[0] # os.path.splitext(os.path.basename(csvName))[0] => if it bugs, try this instead
		# key = ""
		# for k in dataType:
		# 	if k in csvName:
		# 		key = k
		# 		break
		########################

		if key and key in dataType.keys():
			# use this line if you want svg
			# arguments = "dataFile='./averageResults/"+ext+"/"+dataType[key]["dataFile"]+"'; outfile='./Charts/"+ext+"/"+dataType[key]["outfile"]+".svg'; xlab='"+dataType[key]["xlab"]+"'; ylab='"+dataType[key]["ylab"]+"'; mainTitle='"+dataType[key]["mainTitle"]+"'; curve1Label='"+dataType[key]["curve1Label"]+"';"
			# and this line if you want png
			arguments = "dataFile='./averageResults-pandas/"+ext+"/"+dataType[key]["dataFile"]+"'; outfile='./Charts-pandas/"+ext+"/"+dataType[key]["outfile"]+".png'; xlab='"+dataType[key]["xlab"]+"'; ylab='"+dataType[key]["ylab"]+"'; mainTitle='"+dataType[key]["mainTitle"]+"'; curve1Label='"+dataType[key]["curve1Label"]+"';"
			# Add the other curves if they exist
			if "curve2Label" in dataType[key].keys():
				arguments = arguments + " curve2Label='"+dataType[key]["curve2Label"]+"';"
			if "curve3Label" in dataType[key].keys():
				arguments = arguments + " curve3Label='"+dataType[key]["curve3Label"]+"';"
			if "curve4Label" in dataType[key].keys():
				arguments = arguments + " curve4Label='"+dataType[key]["curve4Label"]+"';"
			# Add colors if they exists
			if "color1" in dataType[key].keys():
				arguments = arguments + " color1='"+dataType[key]["color1"]+"';"
			if "color2" in dataType[key].keys():
				arguments = arguments + " color1='"+dataType[key]["color2"]+"';"
			if "color3" in dataType[key].keys():
				arguments = arguments + " color1='"+dataType[key]["color3"]+"';"
			if "color4" in dataType[key].keys():
				arguments = arguments + " color1='"+dataType[key]["color4"]+"';"
			# and run the gnuplot script for this file
			command = "gnuplot -e \""+arguments+"\" genericGnuplot.gp"
			print(key)
			subprocess.run(command)


	# "distribution_nb_FC_per_LSP":
	# {"dataFile":"average_costs.csv", "outfile":"average_costs", "xlab":"Time (hour)", "ylab":"Average costs", "mainTitle":"Average costs", "curve1Label":"Average costs"},