print(30*'*')
print('****bem vindo ao jogo da forca!***')
print(30*'*')

palavra_secreta = 'banana'
letras_acertadas = ['_','_','_','_','_','_',]

acertou = False
enforcou = False
erros = 0
print(letras_acertadas)

while (not acertou and not enforcou):
    chute = input('qual letra? ')

    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
            #print('Encontrei a letra{} na posição {}'.format(letra,posição))
                    letras_acertadas[posicao] = letra
                posicao += 1
    else:
        erros += 1
        
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6

    print(letras_acertadas)

if(acertou):
    print('\n Você ganhou!! \n')
else:
    print('\n Você perdeu!! \n')
print('Fim de jogo')    
