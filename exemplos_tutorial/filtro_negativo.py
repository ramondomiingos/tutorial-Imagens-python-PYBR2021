def filtro_negativo():
    f = open("demo_img1.ppm", "r")

    count = 0
    valores = []
    for line in  f.readlines():
        line = line.replace("\n", "")
        if count == 0 :
            magic_number = line
            count+=1
        elif line[0] == "#":
           pass
        elif count == 1:
            line = line.split(' ')
            if len(line) > 1:
                largura = line[0]
                altura = line[1]
                count += 2
            else:
                largura = line[0]
                count += 1

        elif count == 2:
            altura = line
            count += 1
        elif count == 3:
            max_color = line
            count += 1
            escreve_header(magic_number, largura,altura, max_color)

        else:
            valores = line.split(" ")
            escreve(valores)


def escreve_header(magic_number, largura,altura, maxmax_color):
    img = open("demo_img1_negativo.ppm", "w")
    #print(f'{magic_number}\n{largura}\n{altura}\n{maxmax_color}\n')
    #return
    img.write(f'{magic_number}\n{largura}\n{altura}\n{maxmax_color}\n')
    img.close()
    return

def escreve(valores):
    img = open("demo_img1_negativo.ppm", "a")
    for valor in valores:
        valor=valor.replace("\n", "")

        if valor.isdigit():

            img.write( str(255-int(valor) ) +" \n")

    img.close()



