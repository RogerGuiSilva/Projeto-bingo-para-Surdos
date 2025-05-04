import tkinter as tk
import random

def sortear_numero():
    numero = random.randint(1, 75)  
    sorteado_label.config(text=f'Número sorteado: {numero}')
    
    if numero in cartela:
        resultado_label.config(text="Você tem")
    else:
        resultado_label.config(text="Você não tem")

root = tk.Tk()
root.title("Bingo Surdo")

cartela = random.sample(range(1, 76), 5)

cartela_label = tk.Label(root, text=f'Sua cartela: {cartela}', font=("Arial", 12))
cartela_label.pack(pady=10)

sorteado_label = tk.Label(root, text="Número sorteado: ", font=("Arial", 14))
sorteado_label.pack(pady=10)

resultado_label = tk.Label(root, text="Aguardando sorteio...", font=("Arial", 12))
resultado_label.pack(pady=10)

sortear_button = tk.Button(root, text="Sortear Número", command=sortear_numero, font=("Arial", 12))
sortear_button.pack(pady=20)

root.mainloop()
