class Binarizacao:
    def __init__(self, linha, coluna, imagem_original, imagem_final, limiar):
        self._linha  = linha
        self._coluna = coluna
        self._imagem = imagem_original
        self._limiar = limiar
        self.imagem_final = imagem_final


    def processar(self):
        # linha
        for i in range(self._linha):
            # coluna
            for j in range(self._coluna):
                rgb_imagem = self._imagem.convert('RGB')
                r, _, _ = rgb_imagem.getpixel((j, i))

                cor = 0
                if int(r) > int(self._limiar):
                    cor = 255

                self.imagem_final[j, i] = (cor, cor, cor)
        return self.imagem_final