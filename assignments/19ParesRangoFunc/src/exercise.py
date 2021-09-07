
def main():
    num1 = int(input("Valor 1: "))
    num2 = int(input("Valor 2: "))

    v1=num1
    v2=num2

    if v1>0 and v2>0:
        if v2>v1:
                for valor in range(v1,v2+1):
                    if valor%2==0:
                        print(valor)
        elif v1>v2:
                for valor in range(v2,v1+1):
                    if valor%2==0:
                        print(valor)
    else:
            print("No hay pares")     


if __name__=='__main__':
    main()
