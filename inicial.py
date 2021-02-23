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


    def criar_componentes(self):
        # botão selecionar imagem
        self.btn_selecionar_imagem = tk.Button(
            self, text='Selecionar Imagem',
            command=self.selecionar_imagem)
        self.btn_selecionar_imagem.grid(row=1, column=1)


    def selecionar_imagem(self):
        caminho_imagem =  filedialog.askopenfilename(initialdir = '/',title = 'Select file',filetypes = (('PNG','*.png'),('JPG','*.jpg'),('Todos Arquivos','*.*')))
        if len(caminho_imagem) > 0:
            image = Image.open(caminho_imagem)
            photo = ImageTk.PhotoImage(image)
            self.lbl_imagem = tk.Label(master=self.master, text = 'Imagem Origem', image=photo)
            self.lbl_imagem.image = photo
            self.lbl_imagem.grid(row=2, column=1)
        print(caminho_imagem)


root = tk.Tk()
root.geometry('800x600')
root.title('Processamento de Imagens')
app = Inicial(master=root)

# thread = threading.Thread( target=app.verificar )
# thread.daemon = True 
# thread.start()

app.mainloop()