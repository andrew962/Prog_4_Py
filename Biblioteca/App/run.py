from App.index import creation,menu

if __name__ == '__main__':
    try:
        creation()
        menu()
    except Exception as e:
        menu()
        print(e)
        print('Success!')