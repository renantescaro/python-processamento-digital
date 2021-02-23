import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import threading

class Inicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.criar_componentes()

        self.img_altura  = 0
        self.img_largura = 0
        self.linha       = 0
        self.coluna      = 0
        self.aux         = 0


    def criar_componentes(self):
        # botão selecionar imagem
        self.btn_selecionar_imagem = tk.Button(
            self, text='Selecionar Imagem',
            command=self.selecionar_imagem)
        self.btn_selecionar_imagem.grid(row=1, column=1)


    def selecionar_imagem(self):
        # seleciona imagem do computador
        caminho_imagem =  filedialog.askopenfilename(initialdir = '/',title = 'Select file',filetypes = (('PNG','*.png'),('JPG','*.jpg'),('Todos Arquivos','*.*')))
        if len(caminho_imagem) > 0:
            # abre imagem selecionada
            image = Image.open(caminho_imagem)
            self.img_largura, self.img_altura = image.size
            # diminui tamanho da imagem na tela
            image = image.resize((round(100 / self.img_altura * self.img_largura), round(100)))
            # componente pra mostrar a imagem
            photo = ImageTk.PhotoImage( image )
            self.lbl_imagem = tk.Label(master=self.master, text = 'Imagem Origem', image=photo)
            self.lbl_imagem.image = photo
            self.lbl_imagem.grid(row=2, column=1)
            # variaveis para futura manipulação da imagem
            self.linha  = self.img_altura
            self.coluna = self.img_largura
            self.aux = self.linha *  self.coluna

    
    def processar_imagem(self):
        pass




root = tk.Tk()
root.geometry('800x600')
root.title('Processamento de Imagens')
app = Inicial(master=root)

# thread = threading.Thread( target=app.verificar )
# thread.daemon = True 
# thread.start()

app.mainloop()