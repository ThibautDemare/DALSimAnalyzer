
# Fonction qui retourne une liste de corrélation entre deux variables sur des fenêtres temporelles glissante
# variables à traiter
# longueur du focus
# pas de décalage (par défaut 500)
# resulats : vecteurs de corrélation
corByTimeStep = function (var1, var2, focusLength=1000, stepLength = 500) {
	resu = numeric()
	nbMesures = length(var1)
	max = (nbMesures/stepLength)-1
	for (depart in 0:max) {
		debut = stepLength*depart
		fin = min(debut+1000,nbMesures)
		resu = c(resu, cor(var1[debut:fin],var2[debut:fin]))
	}
	resu
}


# étape 1 : Suppression des colonnes inutiles
# on supprime d'abord les var constantes sauf initialisation à 0
toDelete = c();
lesdiff = c();
for (numCol in 1:length(allData)) {
	if (abs(max(allData[-1,numCol])-mean(allData[-1,numCol])) < 1e-16)
		toDelete = c(toDelete, numCol)
	lesdiff = c(lesdiff,abs(max(allData[,numCol])-mean(allData[,numCol])))
}
allData = allData[ , -toDelete]

# puis on supprime la colonne step car inutile pour les corrélations
allData = allData[, -1]


# étape 2 on calcules les corrélations
# recherche de var coréllé globalement sur le range [2000;16000]
lesCors = cor(allData[2000:16000,])
lesPaires = c()
for (i in 1:(ncol(lesCors)-1)) {
	k = i+1
	for (j in k:(ncol(lesCors))) {
		absCor = abs(lesCors[i,j])
		if (absCor > 0.90 && absCor <= 0.97) 
			lesPaires = c(lesPaires, list(colnames(lesCors)[i], colnames(lesCors)[j], lesCors[i,j]))
	}
}