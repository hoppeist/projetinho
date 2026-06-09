def media(a, b, c):
    return(a + b + c / 3)

def main():
    a = int(input('1 Valor? '))
    b = int(input('2 valor? '))
    c = int(input('3 valor? '))
    print(f'A média e {media(a, b, c): 2.f}')


if __name__ == '__main__':
    main()
