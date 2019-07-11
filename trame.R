dataSimulation = data.frame(n = 1:6000);

df = read.table("average_costs.csv", sep=";", col.names=c("n", "Average costs"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("average_time_to_be_delivered.csv", sep=";", col.names=c("n", "Average time to be delivered (to final consignee)"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("average_time_to_deliver.csv", sep=";", col.names=c("n", "Average time to be delivered (to warehouses)"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("averageThreshold.csv", sep=";", col.names=c("n", "Average threshold of selected LSPs"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("competition_between_LH_Antwerp.csv", sep=";", col.names=c("n", "Number of LSPs who selected Le Havre", "Number of LSPs who selected Antwerp"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("nb_stocks_awaiting.csv", sep=";", col.names=c("n", "Number of stocks awaiting to enter building of final consignee", "Number of stocks awaiting to enter warehouses", "Number of stocks awaiting to leave warehouses", "Number of stocks awaiting to leave provider"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("number_empty_stock_final_dest.csv", sep=";", col.names=c("n", "Number of stock shortages in final consignees"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("number_empty_stock_warehouses.csv", sep=";", col.names=c("n", "Number of stock shortages in warehouses"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("traffic_evolution_CSN.csv", sep=";", col.names=c("n", "Goods traffic on the CSN"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("stocks_final_dests.csv", sep=";", col.names=c("n", "Total stock quantities in final consignees", "Total free surface in final consignees"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("stocks_warehouses.csv", sep=";", col.names=c("n", "Total stock quantities in warehouses", "Total free surface in warehouses"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Antwerpen.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_Antwerpen_Road", "share_leaving_quantities_per_transport_mode_Antwerpen_River", "share_leaving_quantities_per_transport_mode_Antwerpen_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_LeHavre.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_LeHavre_Road", "share_leaving_quantities_per_transport_mode_LeHavre_River", "share_leaving_quantities_per_transport_mode_LeHavre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Basse-Normandie.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_Basse-Normandie_Road", "share_leaving_quantities_per_transport_mode_Basse-Normandie_River", "share_leaving_quantities_per_transport_mode_Basse-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Centre.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_Centre_Road", "share_leaving_quantities_per_transport_mode_Centre_River", "share_leaving_quantities_per_transport_mode_Centre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Haute-Normandie.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_Haute-Normandie_Road", "share_leaving_quantities_per_transport_mode_Haute-Normandie_River", "share_leaving_quantities_per_transport_mode_Haute-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Ile-de-France.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_IdF_Road", "share_leaving_quantities_per_transport_mode_IdF_River", "share_leaving_quantities_per_transport_mode_IdF_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_quantities_per_transport_mode_Picardie.csv", sep=";", col.names=c("n", "share_leaving_quantities_per_transport_mode_Picardie_Road", "share_leaving_quantities_per_transport_mode_Picardie_River", "share_leaving_quantities_per_transport_mode_Picardie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Antwerpen.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_Antwerpen_Road", "share_leaving_vehicles_per_transport_mode_Antwerpen_River", "share_leaving_vehicles_per_transport_mode_Antwerpen_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_LeHavre.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_LeHavre_Road", "share_leaving_vehicles_per_transport_mode_LeHavre_River", "share_leaving_vehicles_per_transport_mode_LeHavre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Basse-Normandie.csv",sep=";", col.names=c("n",  "share_leaving_vehicles_per_transport_mode_Basse-Normandie_Road", "share_leaving_vehicles_per_transport_mode_Basse-Normandie_River", "share_leaving_vehicles_per_transport_mode_Basse-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Centre.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_Centre_Road", "share_leaving_vehicles_per_transport_mode_Centre_River", "share_leaving_vehicles_per_transport_mode_Centre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Haute-Normandie.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_Haute-Normandie_Road", "share_leaving_vehicles_per_transport_mode_Haute-Normandie_River", "share_leaving_vehicles_per_transport_mode_Haute-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Ile-de-France.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_IdF_Road", "share_leaving_vehicles_per_transport_mode_IdF_River", "share_leaving_vehicles_per_transport_mode_IdF_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_leaving_vehicles_per_transport_mode_Picardie.csv", sep=";", col.names=c("n", "share_leaving_vehicles_per_transport_mode_Picardie_Road", "share_leaving_vehicles_per_transport_mode_Picardie_River", "share_leaving_vehicles_per_transport_mode_Picardie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Antwerpen.csv", sep=";", col.names=c("n", "share_port_origin_region_Antwerpen_Number of LSPs who selected Antwerp", "share_port_origin_region_Antwerpen_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_LeHavre.csv", sep=";", col.names=c("n", "share_port_origin_region_LeHavre_Number of LSPs who selected Antwerp", "share_port_origin_region_LeHavre_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Basse-Normandie.csv", sep=";", col.names=c("n", "share_port_origin_region_Basse-Normandie_Number of LSPs who selected Antwerp", "share_port_origin_region_Basse-Normandie_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Centre.csv", sep=";", col.names=c("n", "share_port_origin_region_Centre_Number of LSPs who selected Antwerp", "share_port_origin_region_Centre_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Haute-Normandie.csv", sep=";", col.names=c("n", "share_port_origin_region_Haute-Normandie_Number of LSPs who selected Antwerp", "share_port_origin_region_Haute-Normandie_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Ile-de-France.csv", sep=";", col.names=c("n", "share_port_origin_region_Ile-de-France_Number of LSPs who selected Antwerp", "share_port_origin_region_Ile-de-France_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_port_origin_region_Picardie.csv", sep=";", col.names=c("n", "share_port_origin_region_Picardie_Number of LSPs who selected Antwerp", "share_port_origin_region_Picardie_Number of LSPs who selected Le Havre"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Antwerpen.csv", sep=";", col.names=c("n", "share_transport_mode_Antwerpen_Road", "share_transport_mode_Antwerpen_River", "share_transport_mode_Antwerpen_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_LeHavre.csv", sep=";", col.names=c("n", "share_transport_mode_LeHavre_Road", "share_transport_mode_LeHavre_River", "share_transport_mode_LeHavre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Basse-Normandie.csv", sep=";", col.names=c("n", "share_transport_mode_Basse-Normandie_Road", "share_transport_mode_Basse-Normandie_River", "share_transport_mode_Basse-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Centre.csv", sep=";", col.names=c("n", "share_transport_mode_Centre_Road", "share_transport_mode_Centre_River", "share_transport_mode_Centre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Haute-Normandie.csv", sep=";", col.names=c("n", "share_transport_mode_Haute-Normandie_Road", "share_transport_mode_Haute-Normandie_River", "share_transport_mode_Haute-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Ile-de-France.csv", sep=";", col.names=c("n", "share_transport_mode_IdF_Road", "share_transport_mode_IdF_River", "share_transport_mode_IdF_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_Picardie.csv", sep=";", col.names=c("n", "share_transport_mode_Picardie_Road", "share_transport_mode_Picardie_River", "share_transport_mode_Picardie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Antwerpen.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Antwerpen_Road", "share_transport_mode_quantities_Antwerpen_River", "share_transport_mode_quantities_Antwerpen_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_LeHavre.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_LeHavre_Road", "share_transport_mode_quantities_LeHavre_River", "share_transport_mode_quantities_LeHavre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Basse-Normandie.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Basse-Normandie_Road", "share_transport_mode_quantities_Basse-Normandie_River", "share_transport_mode_quantities_Basse-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Centre.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Centre_Road", "share_transport_mode_quantities_Centre_River", "share_transport_mode_quantities_Centre_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Haute-Normandie.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Haute-Normandie_Road", "share_transport_mode_quantities_Haute-Normandie_River", "share_transport_mode_quantities_Haute-Normandie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Ile-de-France.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_IdF_Road", "share_transport_mode_quantities_IdF_River", "share_transport_mode_quantities_IdF_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities_Picardie.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Picardie_Road", "share_transport_mode_quantities_Picardie_River", "share_transport_mode_quantities_Picardie_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode_quantities.csv", sep=";", col.names=c("n", "share_transport_mode_quantities_Road", "share_transport_mode_quantities_River", "share_transport_mode_quantities_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("share_transport_mode.csv", sep=";", col.names=c("n", "share_transport_mode_Road", "share_transport_mode_River", "share_transport_mode_Maritime"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("strat1_threshold_adoption_share.csv", sep=";", col.names=c("n", "strat1_Low threshold", "strat1_Low to medium threshold", "strat1_Medium to high threshold", "strat1_High threshold"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("strat2_threshold_adoption_share.csv", sep=";", col.names=c("n", "strat2_Low threshold", "strat2_Low to medium threshold", "strat2_Medium to high threshold", "strat2_High threshold"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("strat3_threshold_adoption_share.csv", sep=";", col.names=c("n", "strat3_Low threshold", "strat3_Low to medium threshold", "strat3_Medium to high threshold", "strat3_High threshold"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("strat4_threshold_adoption_share.csv", sep=";", col.names=c("n", "strat4_Low threshold", "strat4_Low to medium threshold", "strat4_Medium to high threshold", "strat4_High threshold"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}

df = read.table("strategies_adoption_share.csv", sep=";", col.names=c("n", "Strategy : biased random selection", "Strategy :  accessibility", "Strategy : closest/largest", "Strategy : pure random selection"));
df = df [2:length(df)]
for (var in colnames(df)) {
  dataSimulation[[var]] = df[[var]]
}


    # étape 1 :    Suppression des colonnes à 0
    # on vire les var constantes sauf initialisation à 0
    toDelete = c();
    for (numCol in 1:length(dataSimulation)) {
	    if (abs(max(dataSimulation[,numCol])-mean(dataSimulation[2:nrow(dataSimulation),numCol])) < 1e-16)
	       toDelete = c(toDelete, numCol)
	}
	dataSimulation = dataSimulation[ , -toDelete]


	lesCor = cor (dataSimulation)

	lesPaires = c()
	for (i in 1:(ncol(lesCor)-1)) {
	    k = i+1
	    for (j in k:(ncol(lesCor))) {
		absCor = abs(lesCor[i,j])
		if (absCor > 0.88 && absCor <= 0.90) 
		   lesPaires = c(lesPaires, list(colnames(lesCor)[i], colnames(lesCor)[j], lesCor[i,j]))
		}
        }



	    

		   
#[[97]]
#[1] "share_leaving_vehicles_per_transport_mode_LeHavre_Maritime"

#[[98]]
#[1] "share_leaving_vehicles_per_transport_mode_Haute.Normandie_Maritime"

#[[99]]
#[1] 1


plot(dataSimulation[,"share_leaving_vehicles_per_transport_mode_LeHavre_Maritime"], dataSimulation[,"share_leaving_vehicles_per_transport_mode_Haute.Normandie_Maritime"])


#[[28]]
#[1] "Average.time.to.be.delivered..to.warehouses."

#[[29]]
#[1] "Total.free.surface.in.warehouses"

#[[30]]
#[1] -0.9838596

plot(dataSimulation[,"Average.time.to.be.delivered..to.warehouses."], dataSimulation[,"Total.free.surface.in.warehouses"])

plot(dataSimulation[,"Total.stock.quantities.in.warehouses"])


plot(dataSimulation[,"Number.of.stock.shortages.in.final.consignees"])


plot(dataSimulation[,share_port_origin_region_Ile.de.France_Number.of.LSPs.who.selected.Antwerp])


#[[13]]
#[1] "Average.costs"

#[[14]]
#[1] "Total.free.surface.in.warehouses"

#[[15]]
#[1] 0.9453139

#TODO : regarder de plus près


#[[7]]
#[1] "Average.costs"

#[[8]]
#[1] "Number.of.LSPs.who.selected.Antwerp"

#[[9]]
#[1] 0.9412055


# exclusion des 100 valeurs initiales avant stabilisation de la simulation
plot(dataSimulation[100:6000,"Number.of.LSPs.who.selected.Le.Havre"],dataSimulation[100:6000,"Average.costs"])
cor(dataSimulation[100:6000,"Number.of.LSPs.who.selected.Le.Havre"],dataSimulation[100:6000,"Average.costs"])
#[1] 0.5900893  => influence plus importante des autres params que le coût de transport

#TODO : LINEAR MODEL


plot(dataSimulation[,"Number.of.LSPs.who.selected.Antwerp"])

#[[28]]
#[1] "Number.of.stock.shortages.in.final.consignees"

#[[29]]
#[1] "Total.stock.quantities.in.warehouses"

#[[30]]
#[1] 0.8941982

#[[31]]
#[1] "Number.of.stock.shortages.in.final.consignees"

#[[32]]
#[1] "Total.free.surface.in.warehouses"

#[[33]]
#[1] -0.8941982



plot(dataSimulation[,"Number.of.stock.shortages.in.final.consignees"],dataSimulation[,"Total.free.surface.in.warehouses"])
