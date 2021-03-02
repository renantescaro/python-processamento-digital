import array

class Histograma:
    def __init__(self, linha, coluna, imagem_original):
        self._linha  = linha
        self._coluna = coluna
        self._imagem = imagem_original
        # array de inteiro
        array.array('i')
        self.vet_histo_original = array.array('i', (0 for i in range(0,256)))
        # inicia histograma na imagem
        self.processar()


    def processar(self):
        # linha
        for i in range(self._linha):
            # coluna
            for j in range(self._coluna):
                rgb_imagem = self._imagem.convert('RGB')

                r, _, _ = rgb_imagem.getpixel((j, i))

                self.vet_histo_original[r] = self.vet_histo_original[r]+1


    def imprimir(self):
        histograma = ''
        for h in self.vet_histo_original:
            histograma += str(h)+str(',')
        print(histograma)