source("fonctions.R")

# chargement des données dans allData

allData = csvIntoDF("../averageResults-pandas/test/")

# étape 1 : Suppression des colonnes à 0
# on vire les var constantes sauf initialisation à 0
toDelete = c();
lesdiff = c();
for (numCol in 1:length(allData)) {
	if (abs(max(allData[-1,numCol])-mean(allData[-1,numCol])) < 1e-16)
		toDelete = c(toDelete, numCol)
	lesdiff = c(lesdiff,abs(max(allData[,numCol])-mean(allData[,numCol])))
}
allData = allData[ , -toDelete]

# étape 2 :on vire step

allData = allData[, -1]

# étape 3 on calcule les corrélations
# recherche de var coréllé globalement [2000;16000]
	
allData = allData[2000:16000,]

lesCorrels = lesCorrelations(allData, 6000);

for(i in 1:nrow(lesCorrels)) {
	# ne pas afficher > 0.97
	if(abs(lesCorrels[i,]$correl) < 0.97) {
		print(lesCorrels[i,]);
		nomVar1 = lesCorrels[i,]$var1
		nomVar2 = lesCorrels[i,]$var2
		# device divisé en trois ligne
		par(mfrow=c(4,1))
		rangeVar1 = c(min(allData[[nomVar1]]),max(allData[[nomVar1]]))
		rangeVar2 = c(min(allData[[nomVar2]]),max(allData[[nomVar2]]))

		# affichage de tout en 3 couleurs selon le pas de temps
		plot(allData[[nomVar1]],allData[[nomVar2]], xlab=nomVar1, ylab=nomVar2, xlim=rangeVar1, ylim=rangeVar2, col = c(rep("red",6000),rep("black",2000),rep("green",6000)))
		reg = lm(allData[[nomVar2]] ~ allData[[nomVar1]])
		print(reg)
		abline(reg, col="blue")

		# affichage de la première phase (avant ouverture canal)
		plot(allData[[nomVar1]][1:6000],allData[[nomVar2]][1:6000], xlab=nomVar1, ylab=nomVar2, col="red", xlim=rangeVar1, ylim=rangeVar2)
		reg = lm(allData[[nomVar2]][1:6000] ~ allData[[nomVar1]][1:6000])
		print(reg)
		abline(reg, col="blue")

		# affichage de la 2e phase (après ouverture canal et stabilasation)
		plot(allData[[nomVar1]][8000:14000],allData[[nomVar2]][8000:14000], xlab=nomVar1, ylab=nomVar2, col="green", xlim=rangeVar1, ylim=rangeVar2)
		reg = lm(allData[[nomVar2]][8000:14000] ~ allData[[nomVar1]][8000:14000])
		print(reg)
		abline(reg, col="blue")

		corByTime =corByTimeStep(allData[[nomVar1]],allData[[nomVar2]], focusLength=2000, stepLength=250)
		plot(corByTime, col="blue", xlab="step", ylab="Cor", pcl=23, ylim=c(-1,1))
		# abline(v=length(corByTime)/2)
		# 14000/250/2
		# [1] 28
		# > 16000/250/2
		# [1] 32
		abline(v=24) # Draw a vertical line to show the opening of the SCN

		readline();
	}
}

