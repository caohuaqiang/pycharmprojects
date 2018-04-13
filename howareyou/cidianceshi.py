A = {'username': 'caohuaqiang', 'password': '123456'}



if __name__ == '__main__':
    B = sorted(A.keys())
    C = sorted(A.values())
    print(B)
    print(C)
    print(C[0])
    D = int(C[0])
    if D < 100:
        print('CHQ')
    else:
        print('go away')
    print(A['username'])
