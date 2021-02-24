import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import array

class Inicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()

        self.sv_tamanho = tk.StringVar() 
        self.sv_linha   = tk.StringVar()
        self.sv_coluna  = tk.StringVar()
        self.sv_limiar  = tk.StringVar()

        self.criar_componentes()

        self.img_original = None
        self.img_altura   = 0
        self.img_largura  = 0
        self.linha        = 0
        self.coluna       = 0
        self.aux          = 0

        array.array('i')
        self.vetHistoOriginal = array.array('i', (0 for i in range(0,256)))


    def criar_componentes(self):
        # botão selecionar imagem
        self.btn_selecionar_imagem = tk.Button(
            self, text='Selecionar Imagem',
            command=self.selecionar_imagem)
        self.btn_selecionar_imagem.grid(row=1, column=1)

        # botão processar imagem
        self.btn_processar_imagem = tk.Button(
            self, text='Processar Imagem',
            command=self.processar_imagem)
        self.btn_processar_imagem.grid(row=1, column=2)

        # Tamanho
        self.lbl_tamanho = tk.Label(
            self, text='Tamanho')
        self.lbl_tamanho.grid(row=2, column=1)
        self.edt_tamanho = tk.Entry(self, width=15, textvariable=self.sv_tamanho)
        self.edt_tamanho.grid(row=2, column=2)

        # Linha
        self.lbl_linha = tk.Label(
            self, text='Linha')
        self.lbl_linha.grid(row=3, column=1)
        self.edt_linha = tk.Entry(self, width=15, textvariable=self.sv_linha)
        self.edt_linha.grid(row=3, column=2)

        # Coluna
        self.lbl_coluna = tk.Label(
            self, text='Coluna')
        self.lbl_coluna.grid(row=4, column=1)
        self.edt_coluna = tk.Entry(self, width=15, textvariable=self.sv_coluna)
        self.edt_coluna.grid(row=4, column=2)

        # Limiar
        self.lbl_limiar = tk.Label(
            self, text='Limiar')
        self.lbl_limiar.grid(row=5, column=1)
        self.edt_limiar = tk.Entry(self, width=15, textvariable=self.sv_limiar)
        self.edt_limiar.grid(row=5, column=2)


    def selecionar_imagem(self):
        # seleciona imagem do computador
        caminho_imagem =  filedialog.askopenfilename(initialdir = '',title = 'Select file',filetypes = (('BMP','*.bmp'), ('JPG','*.jpg'), ('PNG','*.png'),('Todos Arquivos','*.*')))
        if len(caminho_imagem) > 0:
            # abre imagem selecionada
            image = Image.open(caminho_imagem)
            self.img_largura, self.img_altura = image.size
            self.img_original = image
            # diminui tamanho da imagem na tela
            image = image.resize((round(100 / self.img_altura * self.img_largura), round(100)))
            # componente pra mostrar a imagem
            photo = ImageTk.PhotoImage( image )
            self.lbl_imagem = tk.Label(master=self.master, text = 'Imagem Origem', image=photo)
            self.lbl_imagem.image = photo
            self.lbl_imagem.grid(row=1, column=3)
            # variaveis para futura manipulação da imagem
            self.linha  = self.img_altura
            self.coluna = self.img_largura
            self.aux = self.linha *  self.coluna

            self.sv_tamanho.set(self.aux)
            self.sv_linha.set(self.linha)
            self.sv_coluna.set(self.coluna)

    
    def processar_imagem(self):
        self.montar_histograma()

    
    def montar_histograma(self):
        for i in range(self.linha):
            for j in range(self.coluna):
                rgb_imagem = self.img_original.convert('RGB')
                r, g, b = rgb_imagem.getpixel((j, i))
                self.vetHistoOriginal[r] = self.vetHistoOriginal[r]+1

        print('Histograma: ')
        histograma = ''
        for h in self.vetHistoOriginal:
            histograma += str(h)+str(',')
        print(histograma)


    def binarizacao(self):
        for i in range(self.linha):
            for j in range(self.coluna):
                rgb_imagem = self.img_original.convert('RGB')
                r, g, b = rgb_imagem.getpixel((j, i))
                if int(r) <= int(self.sv_limiar.get()):
                    r = 0
                else:
                    r = 255

                # ImgProcessada->Canvas->Pixels[j][i]=RGB(pix,pix,pix);



root = tk.Tk()
root.geometry('800x600')
root.title('Processamento de Imagens')
app = Inicial(master=root)

# thread = threading.Thread( target=app.verificar )
# thread.daemon = True 
# thread.start()

app.mainloop()