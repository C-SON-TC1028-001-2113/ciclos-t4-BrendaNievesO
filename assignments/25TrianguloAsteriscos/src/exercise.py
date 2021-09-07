
def main():
    #escribe tu código abajo de esta línea
    height = int(input("Enter triangle height: "))
    if height > 0:
        for p in range(1, height+1):
            print(' '*(height-p)+ '*'*p)



if __name__=='__main__':
    main()
