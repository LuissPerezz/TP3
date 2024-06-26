def comparar_cofres(cofre1, cofre2):
   
    cofre1_set = set(cofre1)
    cofre2_set = set(cofre2)

   
    monedas_comunes = list(cofre1_set.intersection(cofre2_set))

    return monedas_comunes


cofre1 = [50, 10, 2, 100]
cofre2 = [5, 50, 10, 150]

monedas_comunes = comparar_cofres(cofre1, cofre2)
print("Monedas comunes en ambos cofres:", monedas_comunes)
