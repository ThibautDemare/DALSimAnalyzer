# Dans ce script on essaie de construire un modèle bi-linéaire avec averageCosts comme composante principale et deux autres variables.
# L'intérêt du script est de trouver ces deux autres variables pour que le modèle bi-linéaire soit intéressant

# les correlations avec averageCosts
lesCorrels[lesCorrels$var1 == "averageCosts",]$correl

# vecteur avec la liste des noms de varaibles correctement corrélé avec averageCosts
lesVars2 = lesCorrels[lesCorrels$var1 == "averageCosts" & abs(lesCorrels$correl)>0.8 ,]$var2

# matrice de corrélation entre les variables de lesVars2
matCor = cor(allData[,lesVars2])

for ( i in 1:ncol(matCor)) {
	model1 = lm(as.formula(paste ("averageCosts ~ ", colnames(matCor)[i], sep =" ")), data = allData)
	model2 = lm(
			as.formula( # on reconstruit un chaîne de caractère qui sera traité comme une formule de la forme "averageCosts ~ nomVar1 + nomVar2"
				paste ("averageCosts ~ ", colnames(matCor)[i], "+", 
					colnames(matCor)[(abs(matCor[i,]) == min(abs(matCor[i,])))], # le nom de la variable variable la moins corrélée avec la variable i
					sep =" ")
			), data = allData)
	R2 = summary(model2)$r.squared

	# On ne conserve que les modèle bi-linéaire dont le R-Squarred est vraiment interessant
	if (R2 > 0.9) {
		print(summary(model1))
		print(summary(model2))
		print("======================================================")
		readline()
	}
}

