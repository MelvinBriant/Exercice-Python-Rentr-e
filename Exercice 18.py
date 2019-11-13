adnMoutarde = ['CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN', 'Colonel Moutarde']
adnRose = ['CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN', 'Mlle Rose']
adnPervenche = ['AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN', 'Mme Pervenche']
adnLeblanc = ['CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG', 'Mr Leblanc']

echantillonSuspect1 = 'CATA'
echantillonSuspect2 = 'ATGC'

suspects = [adnMoutarde, adnRose, adnPervenche, adnLeblanc]
echantillons = [echantillonSuspect1, echantillonSuspect2]

def trouver_coupable ():

    for suspectCourant in suspects:
        ressemblance = 0
        for echantillonCourant in echantillons:
            if echantillonCourant in suspectCourant[0]: # Si l'échantillon est dans l'ADN du suspect courant
                suspectCourant[0] = suspectCourant[0].replace(echantillonCourant,'____') # Quand on trouve l'échantillon dans l'ADN du suspect courant on le remplace par _____
                ressemblance = ressemblance + 1

            if ressemblance == 2: # Si il ressemble aux deux échantillons trouvés
                return suspectCourant[1] # Retourne uniquement le nom du suspect

    return "Aucun de ces suspects ne correspondent aux échantillons donnés"

print("Le suspect est :", trouver_coupable())




