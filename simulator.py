import random
import matplotlib.pyplot as plt
def symulator_dryfu_genetycznego(poczatkowy_allele_p, liczba_pokolen, wielkosc_populacji):
    allele_p = poczatkowy_allele_p
    allele_q = 1 - allele_p

    czestosci_p = [allele_p]  

    
    for pokolenie in range(liczba_pokolen):
        liczba_alleli_p = 0

        
        for i in range(wielkosc_populacji):
            if random.random() < allele_p:
                liczba_alleli_p += 1

        
        allele_p = liczba_alleli_p / wielkosc_populacji
        allele_q = 1 - allele_p
        czestosci_p.append(allele_p)

        
        print(f"Pokolenie {pokolenie + 1}: Częstość allelu p = {allele_p}")

    plt.plot(range(liczba_pokolen + 1), czestosci_p, marker='o')
    plt.xlabel('Pokolenie')
    plt.ylabel('Częstość allelu p')
    plt.title('Dryf genetyczny')
    plt.show()
symulator_dryfu_genetycznego(poczatkowy_allele_p=0.5, liczba_pokolen=100, wielkosc_populacji=100)