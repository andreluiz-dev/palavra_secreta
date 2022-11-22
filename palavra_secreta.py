"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavraSecreta = 'travesseiro'
letrasAcertadas = ''
numTentativas = 0

while True:    
    letraDigitada = input('Digite uma letra: ')
    numTentativas += 1

    if len(letraDigitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada
    
    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'
            
    print(f'Palavra formada: {palavraFormada}')       
            
    if palavraFormada == palavraSecreta:
        print('VOCE GANHOU! PARABÉNS!')
        print(f'A palavra era: {palavraSecreta}')
        print(f'Tentativas: {numTentativas}')
        letrasAcertadas = ''
        numTentativas = 0