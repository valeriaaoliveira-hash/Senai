import time

print("Iniciando tempo de resfriamento...\n")

for segundos in range(10, -1, -1):
    print(f"Tempo restante: {segundos} segundos")
    time.sleep(1)

print("\nResfriamento concluído! A prensa pode ser aberta.")