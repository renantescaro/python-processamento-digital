class Passa:
    def __init__(self, altura, largura, imagem_original, imagem_final):
        self._altura       = altura
        self._largura      = largura
        self._imagem       = imagem_original
        self._imagem_final = imagem_final

    def baixa(self):
        for i in range(1, self._altura-2):
            print(i)
            for j in range(1, self._largura-2):
                soma  = 0
                media = 0
                for kl in range(i-1, i+1):
                    for kc in range(j-1, j+1):
                        rgb_imagem = self._imagem.convert('RGB')
                        r, _, _ = rgb_imagem.getpixel((j, i))
                        soma = soma + r
                media = (soma/9)
                self._imagem_final[j, i] = (int(media), int(media), int(media))
        return self._imagem_final


    def alta(self):
        mascara_laplace = [
                [0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]]
        for i in range(0, self._altura-2):
            print(i)
            for j in range(0, self._largura-2):
                vermelho = 0
                verde    = 0
                azul     = 0
                for kl in range(0, 3):
                    for kc in range(0, 3):
                        rgb_imagem = self._imagem.convert('RGB')
                        r, g, b = rgb_imagem.getpixel((j+kl, i+kc))
                        vermelho = vermelho + (r * mascara_laplace[kc][kl])
                        verde    = verde    + (g * mascara_laplace[kc][kl])
                        azul     = azul     + (b * mascara_laplace[kc][kl])

                if vermelho < 0:
                    vermelho = 0
                elif vermelho > 255:
                    vermelho = 255

                if verde < 0:
                    verde = 0
                elif verde > 255:
                    verde = 255

                if azul < 0:
                    azul = 0
                elif azul > 255:
                    azul = 255

                self._imagem_final[j+1, i+1] = (int(vermelho), int(verde), int(azul))
        return self._imagem_final