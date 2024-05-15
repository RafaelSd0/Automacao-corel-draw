import pyautogui
import time
import pyperclip
from tkinter import messagebox

# Função para aparecer mensagen na tela
def mensagen():
    messagebox.showinfo(title='Salvo', message='Os nomes foram salvos' )


# Função para copiar o texto para a área de transferência usando pyperclip
def copiar_texto(texto):
    pyperclip.copy(texto)

# Função para salvar os dados digitados pelo o usuario e apagar os anteriores
def salva():
    # Abre o arquivo em modo de escrita, apagando qualquer conteúdo anterior
    with open('nomes.txt', 'w', encoding='utf-8') as arquivo:
        # Obtém o texto digitado pelo usuário
        nomes = vNoms.get("1.0", "end").strip()
        # Escreve os nomes no arquivo
        arquivo.write(nomes)    
    #Notifica para o usuario que os dados foram salvos    
    mensagen()

    

def escrever_nomes():

    messagebox.showinfo(title='Atenção o codigo vai ser iniciado', message='atenção ao clicar em ok, não aperte teclas no teclado ou mexa o mouse até a execulção terminar')


    time.sleep(1)
    

    x = 100
    y = 250
    i = 0
    nome = []

    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.press('f8')
    time.sleep(2)


    # Lendo os nomes do arquivo
    with open('nomes.txt', 'r', encoding='UTF-8') as arquivo:
        for linha in arquivo:
            nome.append(linha.strip())  # Adicionando cada nome na lista 'nome'

    # Loop para clicar e escrever os nomes
    while i < 151:
        pyautogui.click(x, y)
        
        # Copiando o texto correto para a área de transferência
        try:
            copiar_texto(nome[i])
        except IndexError:
            messagebox.showinfo("Concluído", "Todos os nomes foram digitados com sucesso!")
            break
        
        # Colando o texto da área de transferência
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.775)
        
        y += 20

        if i == 29 or i == 59 or i == 89 or i == 119:
            x += 250
            y = 250

        i += 1
    
    
    


from tkinter import *

def escreverAgora():
    escrever_nomes()
    
    


janela = Tk()
janela.title("teste do app")
janela.geometry('600x640')

Label(janela,text="Instruções:", foreground="#000",anchor=W).place(x=10,y=10)
Label(janela,text="1 - Escreva os nomes e quando terminar não esqueça de apertar em salvar", foreground="#000",anchor=W).place(x=10,y=30)
Label(janela,text="2 - Para iniciar a execução click no botão 'Começar'", foreground="#000",anchor=W).place(x=10,y=50)
Label(janela,text="3 - Não mexa no mouse ou escreva no teclado enquanto o programa estiver rodando", foreground="#000",anchor=W).place(x=10,y=70)



Label(janela, text="Insira os nomes:", background="#fff", foreground="#009",anchor=W).place(y=100,x=10,width=550,height=20)
vNoms = Text(janela)
vNoms.place(x=10, y=120, width=550,height=400)

btn_res=Button(janela,text="Salvar",command=salva)
btn_res.pack()
btn_res.place(x=10,y=530)

btn_res=Button(janela,text="Começar",command=escreverAgora)
btn_res.pack()
btn_res.place(x=10,y=580)

janela.mainloop()