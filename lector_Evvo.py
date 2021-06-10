import fitz
import os
import csv


ruta = 'C:/Users/Usuario/Desktop/Master Python/TFM Lector Facturas/Evvo Home'
def factura_evvo():
    myFile = open('Modelo EvvoHome.csv', 'w')
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
        for ele in lista:                  #!Nos volvemos a recorrer el bucle
            if ele == 'BASE IMPONIBLE':                #!Al encontrar este valor...
                encontrado = True          #!Comenzaremos a añadir los valores siguientes.
            elif encontrado == True:        
                lista_nueva.append(ele)    #!Añade el elemento a la lista_nueva

        numero_de_factura = lista[0]
        print('Numero de factura: ' , numero_de_factura)
        fecha_factura = lista[10]
        print('Fecha Factura: ' ,fecha_factura)
        importe_neto = lista_nueva[0]
        print('Importe neto: ' ,importe_neto,'\n')

        myData = [[numero_de_factura,fecha_factura,importe_neto]]
        writer.writerows(myData)
        print("Writing complete", '\n')
        #input('presiona enter')
factura_evvo()