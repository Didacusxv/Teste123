Nomes = ["Joao","Maria","Jose"]
Notas = [7,3,10]
S = (0)

while S < 3:
    if Notas[S] >= 7:
        print(Nomes[S], "passou com", Notas[S])
    else:
        print(Nomes[S], "nao passou com", Notas[S])
    S = S + 1