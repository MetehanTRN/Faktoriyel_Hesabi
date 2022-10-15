while(True):

	print("Lutfen faktoriyelini istediginiz sayiyi giriniz (Cikmak icin -1 ' i tuslayiniz): ", end = "")
	sayi = int(input())
	faktoriyel = 1

	if(sayi == -1):
		print("Cikis yapiliyor...")
		break
		
	elif(sayi < 0):
		print("Negatif sayilarin faktoriyeli alinamaz")
		continue

	elif(sayi == 0):
		print("{} faktoriyeli : 1".format(sayi))
		continue

	else:
		temp = sayi
		while(sayi != 0):
			faktoriyel *= sayi
			sayi -= 1
		print("{} faktoriyeli : ".format(temp), faktoriyel)
		continue
