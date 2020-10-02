# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 06:41:24 2020

@author: ibsan
"""
#importacion de libreria pandsa
import pandas as pd
#variable para asignacion de archivo con informacion
archivo_csv = 'synergy_logistics_database.csv'

#Metodo para regresar a menu
def yes_or_no_regresar(question):
    while "the answer is invalid":
      #os.system('clear')
      reply = str(input(question+' (y/n): ')).lower().strip()
      if reply[0] == 'y':
          return 'y'
      if reply[0] == 'n':
          return 'n'
#Metodo para Generar resumen en consola y creacion de archivo en excel de informacion de top Exports Imports  
def getTopTenExportImport(direction):
    #lectura y guardado de informacion de archivo en memoria
    data = pd.read_csv(archivo_csv)
    print("------TOTAL DE REGISTROS------")
    grouped1 = data[data['direction'] == direction].groupby(['origin', 'destination']).size().reset_index().rename(columns={0:'Cantidad'}).sort_values(by=['Cantidad'], ascending=False).reset_index() 
    #imprecion en consola de informacion
    print(grouped1[['origin','destination','Cantidad']])
    total_value = grouped1['Cantidad'].sum()
    print("Total de Cantidades por listado: ",total_value)
    print("------TOP 10 REGISTROS------")
    #filtro y query de informacion 
    #IMPORTANTE al cambiar el numero en Head se muestran el numero de registro deseados, al quitarla se optiene todos los registros
    grouped = data[data['direction'] == direction].groupby(['origin', 'destination']).size().reset_index().rename(columns={0:'Cantidad'}).sort_values(by=['Cantidad'], ascending=False).reset_index().head(10) 
    #imprecion en consola de informacion
    print(grouped[['origin','destination','Cantidad']])
    total_value = grouped['Cantidad'].sum()
    print("Total de Cantidades por listado: ",total_value)
    #generacion de archivo excel
    prueba = pd.DataFrame(grouped[['origin','destination','Cantidad']])
    prueba.to_excel('1resumen'+direction+'.xlsx', sheet_name='top10'+direction, index=False)
    
# Metodo para generacion resumen en consola y creacion de archivo en excel de informacion transportes Exports Imports
def getTopThreeTrasnportImportExport(direction):
    #lectura y guardado de informacion de archivo en memoria
    data = pd.read_csv(archivo_csv)
    #filtrado y query de informacion
    grouped = data[data['direction'] == direction].groupby(['transport_mode']).sum().sort_values(by=['total_value'], ascending=False).reset_index()
    #impresion de informacion en consola
    print(grouped[['transport_mode','total_value']])
    #grabado de archico excel
    prueba = pd.DataFrame(grouped[['transport_mode','total_value']])
    prueba.to_excel('2resumen'+direction+'.xlsx', sheet_name='transport'+direction, index=False)
   
# Metodo para genera resumen en consola y creacion de archivo en excel de informacion total por pais Exports Imports
def getTotalImportacionesExportacionesPais(direction):
    #varaibles locales 
    suma_total_values_temp = 0
    suma_total_values = 0
    select_value_final = 0
    count_registros = 0
    #lectura y guardado de informacion de archivo en memoria
    data = pd.read_csv(archivo_csv)
    #filtrado y query de informacion
    grouped = data[data['direction'] == direction].groupby(['origin', 'destination']).sum().sort_values(by=['total_value'], ascending=False).reset_index()
    #suma de totales y obtener el 80% del total
    suma_total_values_temp = grouped['total_value'].sum() * .8
    #comparacion para saber en que registro de total de obtiene el 80% de las ventas
    for valueTotal in grouped['total_value']:
        count_registros += 1
        if(suma_total_values <= suma_total_values_temp):
            suma_total_values += valueTotal
            select_value_final = valueTotal
    #print(select_value_final)
    #print(suma_total_values_temp)
    data_final = grouped[['origin','destination','total_value']]
    #imprime en consola con validacion del total value mayor o igual al obtenido del 80%
    print(data_final[data_final['total_value'] >= select_value_final])
    print("Total de registros de archivo",count_registros)
    #grabado de archivo excel
    prueba = pd.DataFrame(data_final[data_final['total_value'] >= select_value_final])
    prueba.to_excel('3resumen'+direction+'.xlsx', sheet_name='total_value'+direction, index=False )
   