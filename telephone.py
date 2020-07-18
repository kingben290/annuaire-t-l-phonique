import os;

t=dict()
def ajouter(t):
	c=''
	ajout=input("voulez vous ajouter un contact ?? o / n:");
	if(ajout=="o" or ajout=="O"):
	    while(c!="1"):
		    n=input("entre le nom du contact :")
		    m=input("le numero du contact  avec 9 chiffres:")
		    while len(m)!=9:
		    	m =input("le numero du contact avec 9 chiffres:")
		    t[n]=m
		    c=input("entrez 1 lorsque vous avez finis d'entrer vos contacts: ");
	print(t)
	au=input("vous-voulez utiliser autres fonctionnalitées  ?? o / n : ")
	if au=="o" or au=="O":
		print("1-modifier un contact ! ")
		print("2-supprimer un contact ! ")
		b=int(input("faites votre choix : "))
		if b ==1:
			modifier(t)
		elif b==2 :
			supprime(t)
		elif b!={1,2} :
			print("cette option n'existe pas !")
	else:
		print("Merci")
		exit(0)		

def supprime(t):
	i=0
	print(t)
	n=input("entrez le nom a supprimer :")
	for i in t:
		if i == n:
			i = 1
		else:
			i = 0
	if i == 1:
		del t[n]
		print(t)
	else:
		print("Numero inexistant!!!!")
	
		
def modifier(t):
	print(t)
	n=input("entrez le nom a modifier :")
	for i in t:
		if i == n:
			i = 1
		else:
			i = 0
	if i == 1:
		m=input("le nouveau numero du contact  avec 9 chiffres:")
		while len(m)!=9:
			m =input("le nouveau numero du contact avec 9 chiffres:")	
		t[n]=m
		print(t)
	else:
		print("Numero inexistant!!!!")

print("1-ajouter un contact ! ")
print("2-modifier un contact ! ")
print("3-supprimer un contact ! ")
b=int(input("faites votre choix : "))
if b==1:
	ajouter(t)
elif b==2 :
	modifier(t)
elif b==3 :
	supprime(t)	
os.system("pause")