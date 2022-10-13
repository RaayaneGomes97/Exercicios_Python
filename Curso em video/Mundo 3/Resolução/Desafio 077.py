palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:  # Verifica cada palavra
    print(f'A palavra {p.upper()} tem as vogais: ', end='')
    for letra in p:  # Verifica cada letra da palavra
        if letra in 'aeiou':
            print(letra, end=' ')
    print('')
