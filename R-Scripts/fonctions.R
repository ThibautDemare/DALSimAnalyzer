csvIntoDF = function () {
	vFiles = list.files(pattern="*.csv")
	allData = data.frame(step = 0:15999);
	for (filename in vFiles) {
		print(filename);
		df = read.csv(filename, sep=";");
		allData = merge(allData, df)
	}
	allData
}

lesCorrelations = function (data, pasCanal) {
	lesCors = cor(data);
	lesCorsAvant = cor(data[1:pasCanal,]);
	lesCorsApres = cor(data[(pasCanal+2000):nrow(data),]);
	nbVars = ncol(data);
	correl = numeric();
	correlAvant = numeric();
	correlApres = numeric();
	absCor = numeric();
	var1 = character();
	var2 = character();
	for (i in 1:(nbVars-1)) {
		k = i+1;
		for (j in k:nbVars) {
			absCor= c (absCor, abs(lesCors[i,j]));
			correl= c (correl, lesCors[i,j]);
			var1=c(var1,colnames(lesCors)[i]);
			var2=c(var2,colnames(lesCors)[j]);
			correlAvant= c (correlAvant, lesCorsAvant[i,j]);
			correlApres= c (correlApres, lesCorsApres[i,j]);
		}
	}
	classement = order(absCor, decreasing=TRUE);
	lesPaires = data.frame(correl=correl, correlAvant=correlAvant, correlApres=correlApres, var1=var1, var2=var2, stringsAsFactors=FALSE);
	lesPaires[classement,];
}

# parametres
# longueur du focus
# pas de décalage (par défaut 500)
# variables à traiter
# resulats : vecteurs de corrélation
corByTimeStep = function (var1, var2, focusLength=1000, stepLength = 500) {
	resu = numeric();
	nbMesures = length(var1);
	max = (nbMesures/stepLength)-1;
	for (depart in 0:max) {
		debut = stepLength*depart;
		fin = min(debut+1000,nbMesures);
		resu = c(resu, cor(var1[debut:fin],var2[debut:fin]));
	}
	resu;
}

focusCorrel = function(dfCorrel, min, max) {
	return(dfCorrel[abs(dfCorrel$correl)>min & abs(dfCorrel$correl)<max,])
}
