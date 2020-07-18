import os;

t=dict()
def ajouter(t):
	c=''
	ajout=input("voulez vous ajouter un contact ?? o / n:");
	if(ajout=="o" or ajout=="O"):
	    while(c!="1"):
		    n=input("entre le nom de la tache :")
		    m=input("la tache a effectuer :")
		    t[n]=m
		    c=input("entrez 1 lorsque vous avez finis d'entrer vos taches: ");
	print(t)
	au=input("vous-voulez utiliser autres fonctionnalitées  ?? o / n : ")
	if au=="o" or au=="O":
		print("1-modifier la tache ?? ")
		print("2-supprimer la tache effectuer ?? ")
		print("3-afficher la liste des taches ??")
		b=int(input("faites votre choix : "))
		if b ==1:
			modifier(t)
		elif b==2 :
			supprime(t)
		elif b==3 :
			afficher(t)
		else:
			print("option inexistant ")
			exit(0)
	else:
		print("Merci")
		exit(0)
def supprime(t):
	i=0
	print(t)
	n=input("entrez le nom de la tache a supprimer :")
	for i in t:
		if i == n:
			i = 1
		else:
			i = 0
	if i == 1:
		del t[n]
		print(t)
	else:
		print("Nom inexistant!!!!")
	
		
def modifier(t):
	print(t)
	n=input("entrez le nom de la tache a modifier :")
	for i in t:
		if i == n:
			i = 1
		else:
			i = 0
	if i == 1:
		m=input(" Entrez la nouvelle tache a effectuer:")	
		t[n]=m
		print(t)
	else:
		print("Nom inexistant!!!!")
def afficher(t):
	print(t)

print("1-ajouter une tache a la liste  ! ")
print("2-modifier une tache ! ")
print("3-supprimer une tache ! ")
print("4-afficher la liste des taches ")
b=int(input("faites votre choix : "))
if b==1:
	ajouter(t)
elif b==2 :
	modifier(t)
elif b==3 :
	supprime(t)
elif b==4:
	afficher(t)
else:
	print("cette option n'est pas valide !!")
	exit(0)		
os.system("pause")		