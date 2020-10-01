# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 06:33:09 2020

@author: ibsan
"""
import os
import data_services

exit = False;
while exit == False:
    print("**********************************************")
    print("MENU DE CONSULTA")
    print("**********************************************")
    print("1.- Top 10 Exportacion Importacion")
    print("2.- Top 3 Medio de Transporte")
    print("3.- Top Importaciones Exportaciones por Pais")
    print("4.- Salir")
    print("\n")
    menu_item_select = input("Introdusca la opcion deseada: ")
    #Comparaciones para realizar los proceso correspondientes al menu seleccionado
    if(menu_item_select == '1'):
      regresar_programa = 'n'
      while regresar_programa == 'n':
        #os.system('clear')
        print("**********************************************")
        print("Top Exportacion")
        print("**********************************************")
        data_services.getTopTenExportImport("Exports")  
        print("**********************************************")
        print("Top Importaciones")
        print("**********************************************")
        data_services.getTopTenExportImport("Imports")
        print("\n")
        regresar_programa = data_services.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
      #os.system('clear')
    elif(menu_item_select == "2"):
      regresar_programa = 'n'
      while regresar_programa == 'n':
        #os.system('clear')
        print("**********************************************")
        print("Top 3 Medio de Transporte Exportaciones")
        print("**********************************************")
        data_services.getTopThreeTrasnportImportExport("Exports")
        print("**********************************************")
        print("Top 3 Medio de Transporte Importaciones")
        print("**********************************************")
        data_services.getTopThreeTrasnportImportExport("Imports")
        print("\n")
        regresar_programa = data_services.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
      #os.system('clear')
    elif(menu_item_select == "3"):
      regresar_programa = 'n'
      while regresar_programa == 'n':
       #os.system('clear')
        print("**********************************************")
        print("Top 80% Exportaciones valor total por Pais")
        print("**********************************************")
        data_services.getTotalImportacionesExportacionesPais("Exports")
        print("**********************************************")
        print("Top 80% Importaciones valor total por Pais")
        print("**********************************************")
        data_services.getTotalImportacionesExportacionesPais("Imports")
        print("\n")
        regresar_programa = data_services.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
      #os.system('clear')
    elif(menu_item_select == "4"):
      #os.system('clear')
      exit = True
    else:
      #os.system('clear')
      print("\n")
      print("**** ERROR: Seleccione una Opcion valida ****")
      print("\n")



