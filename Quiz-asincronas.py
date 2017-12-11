def letras():
    for i in range(ord('a'), ord('m')+1):
        yield (chr(i))

def impar():
    for i in range(100):
        if i % 2 == 1:
            yield (i)



if __name__ == '__main__':
    letra = letras()
    try:
        for i in range(ord('m')):
            print(next(letra))
            if i == 'm':
                break
    except Exception as e:
        print(e)

    imp = impar()
    try:
        for i in range(100):
            print(next(imp))
    except Exception as e:
        print(e)