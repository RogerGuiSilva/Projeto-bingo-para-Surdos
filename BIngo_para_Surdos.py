import tkinter as tk
from tkinter import messagebox
import random

def mostrar_tela_inicial():
    tela_inicial = tk.Toplevel()
    tela_inicial.title("Bem-vindo ao Bingo Surdo")
    tela_inicial.geometry("400x300")
    tela_inicial.configure(bg="#f0f0f0")

    titulo = tk.Label(tela_inicial, text="Bingo Surdo", font=("Arial Black", 24), bg="#f0f0f0")
    titulo.pack(pady=20)

    btn_comecar = tk.Button(tela_inicial, text="Começar Jogo", font=("Arial", 14), command=lambda: iniciar_jogo(tela_inicial))
    btn_comecar.pack(pady=10)

    btn_ajuda = tk.Button(tela_inicial, text="Ajuda / Instruções", font=("Arial", 12), command=mostrar_ajuda)
    btn_ajuda.pack(pady=10)

def mostrar_ajuda():
    mensagem = (
        "Bem-vindo ao Bingo Surdo!\n\n"
        "1. Clique em 'Sortear Número' para iniciar.\n"
        "2. Os números sorteados aparecerão na tela.\n"
        "3. Clique nos números da sua cartela se eles forem sorteados.\n"
        "4. Ao completar uma linha, coluna ou diagonal, o sistema reconhecerá automaticamente o BINGO!\n"
        "5. O botão 'FREE' no centro já vem marcado.\n\n"
        "Boa sorte!"
    )
    messagebox.showinfo("Ajuda", mensagem)

TLR = tk.Tk()
TLR.withdraw()  
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
        lbl_sorteio.config(text="Todos os números foram sorteados!")
        return

    while True:
        numero = random.randint(1, 75)
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
            break

    lbl_sorteio.config(text=f"Número sorteado: {numero}")
    lbl_hist.config(text=f"Sorteados: {sorted(numeros_sorteados)}")

    if numero in botoes_cartela:
        botao = botoes_cartela[numero]
        botao.config(bg="green", fg="white", state="disabled")
        checar_bingo()

def checar_numero(numero, botao):
    if numero not in numeros_sorteados:
        messagebox.showinfo("Atenção", f"O número {numero} ainda não foi sorteado!")
        return

    if botao.cget("bg") == "green":
        return

    botao.config(bg="green", fg="white", state="disabled")
    checar_bingo()

def checar_bingo():
    
    for i in range(5):
        if all(botao_esta_marcado(i, j) for j in range(5)) or \
           all(botao_esta_marcado(j, i) for j in range(5)):
            mostrar_bingo()
            return

    if all(botao_esta_marcado(i, i) for i in range(5)) or \
       all(botao_esta_marcado(i, 4 - i) for i in range(5)):
        mostrar_bingo()

def botao_esta_marcado(linha, coluna):
    botao = btn_matriz[linha][coluna]
    return botao.cget("bg") == "green"

def mostrar_bingo():
    for linha in btn_matriz:
        for botao in linha:
            botao.config(bg="green", fg="white", state="disabled")
    messagebox.showinfo("Parabéns!", "BINGO!")

def iniciar_jogo(tela_inicial):
    tela_inicial.destroy()
    TLR.deiconify()
    criar_interface()

def criar_interface():
    global botoes_cartela, btn_matriz, lbl_sorteio, lbl_hist

    cartela = gerar_cartela()
    botoes_cartela = {}
    btn_matriz = []

    titulo = tk.Label(TLR, text="B I N G O", font=("Arial Black", 24), bg="#f0f0f0")
    titulo.pack(pady=10)

    frame_cartela = tk.Frame(TLR, bg="#f0f0f0")
    frame_cartela.pack()

    letras = ['B', 'I', 'N', 'G', 'O']
    for i, letra in enumerate(letras):
        l = tk.Label(frame_cartela, text=letra, font=("Arial", 16, "bold"), width=5, bg="#d0d0ff")
        l.grid(row=0, column=i, padx=2, pady=2)

    for row_idx in range(5):
        linha_botoes = []
        for col_idx, letra in enumerate(letras):
            numero = cartela[letra][row_idx]
            if numero == "FREE":
                botao = tk.Button(frame_cartela, text=numero, width=5, height=2, font=("Arial", 12),
                                  bg="green", fg="white", state="disabled")
            else:
                botao = tk.Button(frame_cartela, text=str(numero), width=5, height=2, font=("Arial", 12),
                                  command=lambda n=numero: checar_numero(n, botoes_cartela[n]))
                botoes_cartela[numero] = botao
            botao.grid(row=row_idx + 1, column=col_idx, padx=2, pady=2)
            linha_botoes.append(botao)
        btn_matriz.append(linha_botoes)

    lbl_sorteio = tk.Label(TLR, text="Número sorteado: ", font=("Arial", 14), bg="#f0f0f0")
    lbl_sorteio.pack(pady=10)

    sortear_button = tk.Button(TLR, text="Sortear Número", command=sortear_numero, font=("Arial", 12))
    sortear_button.pack(pady=10)

    lbl_hist = tk.Label(TLR, text="Sorteados: []", font=("Arial", 10), bg="#f0f0f0")
    lbl_hist.pack(pady=10)

mostrar_tela_inicial()
TLR.mainloop()
