import fitz
import os
import csv   

ruta = 'C:/Users/Usuario/Desktop/Master Python/TFM Lector Facturas/Latrastienda'
def factura_latrastienda():
    myFile = open('Modelo LaTrastienda.csv', 'w',newline= "")
    myData = [["N_Factura", "Fecha Factura", "Importe Neto"]]
    writer = csv.writer(myFile)
    writer.writerows(myData)
    for archivo in os.listdir(ruta):
        with fitz.open(ruta + '/' + archivo) as doc:
            text = ""                      #!Cadena que almacena todo el texto del PDF
            pages = []                     #!Lista del numero de paginas
            for page in doc:               #!Recorrer todas las paginas
                pages.append(page)         #!Añade cada pagina por separado a la lista Pages
            
            text += pages[0].getText()     #!Convierte todo el PDF a texto

        lista = text.split('\n')           #!Te divide todos los \n que hay dentro del PDF y los devuelve como cadena de caracteres dentro de una lista
        #print(text,'\n')                  #!Te imprime todo el texto del pdf
        #print(lista,'\n')                 #!Te imprime la lista

        lista_nueva = []                   #!Nueva lista donde partiran los valores desde Importe IVA.
        encontrado = False                 #!Creamos el Booleano para localizar el momento en el que apendeamos los valores a la lista_nueva
        abono = False

        for ele in lista:
            if ele == 'Abono':
                abono = True

        for ele in lista:                  #!Nos volvemos a recorrer el bucle
            if ele == 'Importe Total':      #!Al encontrar este valor...
                encontrado = True          #!Comenzaremos a añadir los valores siguientes.
            elif encontrado == True:        
                lista_nueva.append(ele)    #!Añade el elemento a la lista_nueva

        if abono == True:
            numero_de_factura = lista[25]
            print('Numero de factura: ' , numero_de_factura)
            fecha_factura = lista[26]
            print('Fecha Factura: ' ,fecha_factura)
            importe_neto = "-"+str(lista_nueva[0])
            print('Importe neto: ', importe_neto,'\n')
        else:
            numero_de_factura = lista[27]
            print('Numero de factura: ' , numero_de_factura, '\n')
            fecha_factura = lista[28]
            print('Fecha Factura: ' ,fecha_factura,'\n')
            importe_neto = lista_nueva[0]
            print('Importe neto: ' ,importe_neto)

        myData = [[numero_de_factura,fecha_factura,importe_neto]]
        writer.writerows(myData)
        print("Writing complete", '\n')
        #input('presiona enter')
factura_latrastienda()