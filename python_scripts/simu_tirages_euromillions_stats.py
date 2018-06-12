from random import *
import time

no = [3, 8, 11, 16, 29]
# no = [1, 13, 17, 11, 4]
et = [1, 4]

bonNumTirage = 0

bon3Nums2etoi = 0
bon3Nums1etoi = 0
bon3Nums = 0

bon4Nums2etoi = 0
bon4Nums1etoi = 0
bon4Nums = 0

bon5Nums2etoi = 0
bon5Nums1etoi = 0
bon5Nums = 0

i = 0

start = time.time()
while i < 40E6:  # on simule i tirages

    if i % 1e6 == 0:
        now = time.time()
        print("i = " + str(i) + "   temps ecoule = " + str((now - start) / 60)
              + "min")

    numeros = list(range(1, 51))  # liste de 1 a 50
    liste1 = []  # liste dans laquelle sont stockes les numeros tires
    u = 0

    while u < 5:  # on tire 5 numeros
        alea = choice(numeros)  # choix aleatoire parmi la liste "numeros"
        liste1.append(alea)  # on ajoute l'element a la liste des numeros tires
        numeros.remove(alea)  # on enleve l'element de la liste des numeros restants
        u += 1
    # print (liste1)

    # on fait exactement pareil pour les 2 etoiles (entre 1 et 11)
    stars = list(range(1, 12))
    liste2 = []
    v = 0

    while v < 2:
        alea2 = choice(stars)
        liste2.append(alea2)
        stars.remove(alea2)
        v += 1
    # print (liste2)

    bonNumTirage = 0
    for num in range(5):
        if liste1[num] in no:
            bonNumTirage += 1
        elif num < 2:
            break

    if bonNumTirage > 2:
        bonEtoileTirage = 0
        for etoi in range(2):
            if liste2[etoi] in et:
                bonEtoileTirage += 1

    if bonNumTirage == 3:
        if bonEtoileTirage == 0:
            bon3Nums += 1
        elif bonEtoileTirage == 1:
            bon3Nums1etoi += 1
        elif bonEtoileTirage == 2:
            bon3Nums2etoi += 1

    if bonNumTirage == 4:
        if bonEtoileTirage == 0:
            bon4Nums += 1
        elif bonEtoileTirage == 1:
            bon4Nums1etoi += 1
        elif bonEtoileTirage == 2:
            bon4Nums2etoi += 1

    if bonNumTirage == 5:
        if bonEtoileTirage == 0:
            bon5Nums += 1
        elif bonEtoileTirage == 1:
            bon5Nums1etoi += 1
        elif bonEtoileTirage == 2:
            bon5Nums2etoi += 1

            print("GAGNEEEEE APRES " + str(i) + " tirages")
            print(liste1)

    i += 1
print("5 num 2 * " + str(bon5Nums2etoi))
print("5 num 1 * " + str(bon5Nums1etoi))
print("5 num 0 * " + str(bon5Nums))
print("4 num 2 * " + str(bon4Nums2etoi))
print("4 num 1 * " + str(bon4Nums1etoi))
print("4 num 0 * " + str(bon4Nums))
print("3 num 2 * " + str(bon3Nums2etoi))
print("3 num 1 * " + str(bon3Nums1etoi))
print("3 num 0 * " + str(bon3Nums))
