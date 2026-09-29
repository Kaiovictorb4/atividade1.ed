#declaração do conjunto(chaves)
frutas = {"maca", "uva", "maca"}
# duplicadas sao eliminadas
print(frutas) #{'maca, 'uva,}
# teste de pertinencia (acesso)
print("uva" in frutas) #True
#pecorrencdo o conjunto
for f in frutas:
    print(f)