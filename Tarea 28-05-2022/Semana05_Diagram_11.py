goalsPaco = int(input("Digite los goles anotado por Paco: "))
goalsLuis = int(input("Digite los goles anotado por Luis: "))
goalsHugo = int(input("Digite los goles anotado por Hugo: "))

pair = goalsPaco+goalsLuis

if goalsHugo > pair :
    print("Gano Hugo")
elif pair == goalsHugo:
    print("Empataron")
else :
    print("Ganaron Paco y Luis")