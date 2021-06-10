import fitz
import os
import csv


ruta = 'C:/Users/Usuario/Desktop/Master Python/TFM Lector Facturas/Aliexpress'
def factura_comisionesaliexpress():
    myFile = open('Modelo ComisionesAE.csv', 'w',newline= "")
    myData = [["N_Factura", "Fecha Factura", "Importe Neto"]]
    writer = csv.writer(myFile, delimiter=",")
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
        print(lista,'\n')                 

        lista_nueva_factura = []                   
        encontrado_factura = False                 
        for ele in lista:                  
            if ele == 'Invoice No.':                
                encontrado_factura = True         
            elif encontrado_factura == True:        
                lista_nueva_factura.append(ele)

        lista_nueva_precio = []                   
        encontrado_precio = False                 
        for ele in lista:                  
            if ele == 'Total amount in EUR':                
                encontrado_precio = True         
            elif encontrado_precio == True:        
                lista_nueva_precio.append(ele)    

        numero_de_factura = lista_nueva_factura[2]
        print('Numero de factura: ' , numero_de_factura)
        fecha_factura = lista_nueva_factura[1]
        print('Fecha Factura: ' ,fecha_factura)
        importe_neto = lista_nueva_precio[0]
        print('Importe neto: ' ,importe_neto,'\n')

        myData = [[numero_de_factura,fecha_factura,importe_neto]]
        writer.writerows(myData)
        print("Writing complete", '\n')
        #input('presiona enter')
factura_comisionesaliexpress()