import tkinter as tk
import random
from tkinter import messagebox

TLR = tk.Tk()
TLR.title("Bingo Surdo")
TLR.configure(bg="#f0f0f0")

numeros_sorteados = []
botoes_cartela = {}

def gerar_cartela():
    colunas = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    colunas['N'][2] = "FREE"
    return colunas

def sortear_numero():
    if len(numeros_sorteados) >= 75:
        sorteado_label.config(text="Todos os números foram sorteados!")
        return

    while True:
        numero = random.randint(1, 75)
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
            break

    sorteado_label.config(text=f"Número sorteado: {numero}")
    historico_label.config(text=f"Sorteados: {sorted(numeros_sorteados)}")

    if numero in botoes_cartela:
        botao = botoes_cartela[numero]
        botao.config(bg="green", fg="white", state="disabled")

def checar_numero(numero, botao):
    if numero not in numeros_sorteados:
        messagebox.showinfo("Atenção", f"O número {numero} ainda não foi sorteado!")
        return

    cor_atual = botao.cget("bg")
    if cor_atual == "green":
        return

    botao.config(bg="green", fg="white", state="disabled")

cartela = gerar_cartela()

titulo = tk.Label(TLR, text="B I N G O", font=("Arial Black", 24), bg="#f0f0f0")
titulo.pack(pady=10)

frame_cartela = tk.Frame(TLR, bg="#f0f0f0")
frame_cartela.pack()

letras = ['B', 'I', 'N', 'G', 'O']
for i, letra in enumerate(letras):
    l = tk.Label(frame_cartela, text=letra, font=("Arial", 16, "bold"), width=5, bg="#d0d0ff")
    l.grid(row=0, column=i, padx=2, pady=2)

for col_idx, letra in enumerate(letras):
    for row_idx, numero in enumerate(cartela[letra]):
        if numero == "FREE":
            botao = tk.Button(
                frame_cartela, text=numero, width=5, height=2, font=("Arial", 12),
                bg="green", fg="white", state="disabled"
            )
        else:
            botao = tk.Button(
                frame_cartela, text=str(numero), width=5, height=2, font=("Arial", 12),
                command=lambda n=numero, b=None: checar_numero(n, botoes_cartela[n])
            )
            botoes_cartela[numero] = botao
        botao.grid(row=row_idx + 1, column=col_idx, padx=2, pady=2)

sorteado_label = tk.Label(TLR, text="Número sorteado: ", font=("Arial", 14), bg="#f0f0f0")
sorteado_label.pack(pady=10)

sortear_button = tk.Button(TLR, text="Sortear Número", command=sortear_numero, font=("Arial", 12))
sortear_button.pack(pady=10)

historico_label = tk.Label(TLR, text="Sorteados: []", font=("Arial", 10), bg="#f0f0f0")
historico_label.pack(pady=10)

TLR.mainloop()
      
