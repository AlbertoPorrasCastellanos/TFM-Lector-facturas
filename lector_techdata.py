import fitz
import os
import csv


ruta = 'C:/Users/Usuario/Desktop/Master Python/TFM Lector Facturas/Pruebas'

def factura_techdata():
    myFile = open('Modelo Techdata.csv', 'w')
    myData = [["N_Factura", "Fecha Factura", "Importe Neto"]]
    writer = csv.writer(myFile)
    writer.writerows(myData)
    for archivo in os.listdir(ruta):
        with fitz.open(ruta + '/' + archivo) as doc:
            text = ""                      
            pages = []                     
            for page in doc:               
                pages.append(page)         
            
            text += pages[0].getText()     
        lista = text.split('\n')           
        #print(text,'\n')                  
        #print(lista,'\n')                 

        lista_nueva = []                   
        encontrado = False
        abono = True
        
        for ele in lista:
            cadena = lista[1]
            subcadena = cadena
            if subcadena == 'Factura rectificativa':
                abono = True
                                    
        for ele in lista:                  
            if ele == 'Importe IVA':       
                encontrado = True          
            elif encontrado == True:        
                lista_nueva.append(ele)    

        if abono == True:
            numero_de_factura = lista[5]
            print('Numero de factura: ' , numero_de_factura)
            fecha_factura = lista[6]
            print('Fecha Factura: ' ,fecha_factura)
            importe_neto = "-"+str(lista_nueva[2])
            print('Importe neto: ', importe_neto,'\n')
        else:
            numero_de_factura = lista[5]
            print('Numero de factura: ' , numero_de_factura, '\n')
            fecha_factura = lista[6]
            print('Fecha Factura: ' ,fecha_factura,'\n')
            importe_neto = lista_nueva[2]
            print('Importe neto: ' ,importe_neto)

        myData = [[numero_de_factura,fecha_factura,importe_neto]]
        writer.writerows(myData)
        print("Writing complete", '\n')
        #input('presiona enter')

    myFile.close()
factura_techdata()




