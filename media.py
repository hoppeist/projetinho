from biblioteca import media

def main():
    a = int(input('1º Valor? '))
    b = int(input('2º valor? '))
    c = int(input('3º valor? '))
    
    # Sintaxe correta para exibir 2 casas decimais: :.2f
    print(f'A média é: {media(a, b, c):.2f}')

if __name__ == '__main__':
    main()
