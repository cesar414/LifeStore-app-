"""
Login
credenciales:

usuario:
    Hugo,Lucas,Mateo,Leo,Daniel,Alejandro,Pablo
    contrase;a:
    Dataton, DataDarks, DataRangers, Python Squad
inicio de programa credenciales 
-----------------------------------------------------------------------------------------------------
"""
#librerias usadas en el programa 
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
from datetime import datetime
from operator import itemgetter 
import time
# Variables fijas 
time_duration = 1
usuarioAccedio = False
UsuarioMenu=False
intentos = 0
usuarios=['Hugo', 'Lucas', 'Mateo', 'Leo', 'Daniel', 'Alejandro', 'Pablo']
contras=['Dataton', 'DataDarks', 'DataRangers', 'Python Squad']
#Variables para menus
MenuPrincipal= """
Por favor seleccione la opcion que mas le agrade
1- Productos mas vendidos y productos rezagados
2- Productos por rese;a en el servicio
3- ingresos y ventas
4- Estrategias
5- Exit
"""
# Bienvenida!
mensaje_bienvenida = 'Bienvenide al sistema!\nAccede con tus credenciales'
print(mensaje_bienvenida)

# Bucle donde el usuario ingresa credenciales 
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contra = input('Contrase;a: ')
    intentos += 1
    # Reviso si usuari y contraseña coencide 
    if usuario in usuarios and contra in contras:
        usuarioAccedio = True
        print('Bienvenido a LifeStore app')
    else:
        # print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario in usuarios:
            print('Te equivocaste en la contrase;a')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
    if intentos == 4:
        exit()
"""
Fin de bucle credenciales
-------------------------------------------------------------------------------------------------------------------------------
"""
"""
Creacion de diccionarios
-------------------------------------------------------------------------------------------------------------------------------
"""
#funcion para contar numero repetido solo sirve para listas
def contar(datos):
      result = {}
      for dato in datos:
        if dato not in result: #si dato no se encuentra en la lista resultado se agrega el contador
          result[dato] = 0    # Meter contador de los numeros repetidos
        result[dato] += 1     # Incrementar el contador
      return result 
#Fin funcion contar numero repetido
#Orden por dia, Mes y año los productos de la lifestore_sales 
#dentro de este diccionario se quitan los productos regresados a la tienda 
id_Ventas=[[Dato[1], Dato[3]] for Dato in lifestore_sales if Dato[4]==0]
date =  [Fecha[1] for Fecha in id_Ventas]
#se hace uso de la funcion date para saber que dato corresponde para dia/mes/ año
date.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y')) 
#creacion de diccionarios para clasificar por Mes y Año los productos 
Productos_ClasificadosporMes= {}
for par in id_Ventas:
  id = par[0]           #id_product
  date = par[1]         #date
  MesAño=date[3:]       #se quita la parte de dia
  if MesAño not in Productos_ClasificadosporMes.keys():
    Productos_ClasificadosporMes[MesAño] = []
  Productos_ClasificadosporMes[MesAño].append(id)
#fin de diccionario para clasificar por mes y año a productos
#diccionarios con todos los productos por fecha
id_Ventas=[[Dato[1], Dato[3]] for Dato in lifestore_sales ]
date =  [Fecha[1] for Fecha in id_Ventas]
#se hace uso de la funcion date para saber que dato corresponde para dia/mes/ año
date.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y')) 
#creacion de diccionarios para clasificar por Mes y Año los productos 
Productostotal_ClasificadosporMes= {}
for par in id_Ventas:
  id = par[0]
  date = par[1]
  MesAño=date[3:]
  if MesAño not in Productostotal_ClasificadosporMes.keys():
    Productostotal_ClasificadosporMes[MesAño] = []
  Productostotal_ClasificadosporMes[MesAño].append(id)
#fin de diccionarios para clasificar por Mes y Año los productos 
#unir Id_product con name 
id_name=[[Dato[0], Dato[1]] for Dato in lifestore_products ]
#creacion de diccionarios para unir Id_product con name 
Productos_name= {}
for par in id_name:
  id = par[1]
  name = par[0]
  if name not in Productos_name.keys():
    Productos_name[name] = []
  Productos_name[name].append(id)
#fin de diccionarios para unir Id_product con name 
# unir Id_product con id_search 
id_search=[[Dato[0], Dato[1]] for Dato in lifestore_searches ]
#creacion de diccionarios para unir Id_product con id_search 
Productos_Buscados= {}
for par in id_search:
  id= par[0]
  Productos = par[1]
  if Productos not in Productos_Buscados.keys() :
      Productos_Buscados[Productos] = []
  Productos_Buscados[Productos].append(id)
#fin de diccionarios para unir Id_product con id_search    
# unir Id_product con id_price 
id_price=[[Dato[0], Dato[2]] for Dato in lifestore_products ]
#creacion de diccionarios para unir Id_product con precio 
Productos_precio= {}
for par in id_price:
  id= par[1]
  precio = par[0]
  if precio not in Productos_precio.keys() :
      Productos_precio[precio] = []
  Productos_precio[precio].append(id)
#fin de diccionarios para unir Id_product con precio 
#unir Id_product con score 
score=[[Dato[1], Dato[2]] for Dato in lifestore_sales ]
#creacion de diccionarios para unir Id_product con score 
Productos_Score= {}
for par in score:
  id= par[1]
  ReseUser = par[0]
  if ReseUser not in Productos_Score.keys() :
      Productos_Score[ReseUser] = []
  Productos_Score[ReseUser].append(id)
producto=list(Productos_Score.keys())
resproducto_list=[]
#creo el diccionario que junta el producto y el promedio de reseñas
for par in Productos_Score:
  longscore=len(Productos_Score[par])
  resproducto_list.append(sum(Productos_Score[par])/longscore)
score_dic={}
for par in range(len(producto)):
  score_dic[producto[par]]=resproducto_list[par]
# fin de dicionario que une Id_product con score 
# inicio de dicionario que une Id_product con id_categoria 
id_categoria = [ [producto[0], producto[3]] for producto in lifestore_products]
productos_clasificados = {}
for par in id_categoria:
    id = par[0]
    cat = par[1]
    if cat not in productos_clasificados.keys():
        productos_clasificados[cat] = []
    productos_clasificados[cat].append(id)
# fin de dicionario que une Id_product con id_categoria 
# inicio de dicionario que une Id_product con id_stock
id_stock = [ [producto[0], producto[4]] for producto in lifestore_products]
productos_stock = {}
for par in id_stock:
    id = par[1]
    stock = par[0]
    if stock not in productos_stock.keys():
        productos_stock[stock] = []
    productos_stock[stock].append(id)
# fin de dicionario que une Id_product con id_stock 
"""
Fin de Creacion de diccionarios
-------------------------------------------------------------------------------------------------------------------------------
"""
"""
inicio del programa donde se vera el menu 
-----------------------------------------------------------------------------------------------------------------------------
"""
time.sleep(time_duration)
#Bucle menu principal
while not UsuarioMenu:
  print(MenuPrincipal)
  opcion=input("introduzca un digito entre 1 y 5 \n")
  if opcion== '1':
    
    #paso uno se organizan los productos vendidos al mes
    # se selecciona el mes deceado
    opcion1=input("introduzca mes de la siguiente forma MM\n")
    opcion2=input("introduzca  a;o de la siguiente forma YYYY\n")
    #se meten los productos vendidos en el mes en id_productos
    id_product=Productos_ClasificadosporMes.get(F"{opcion1}/{opcion2}",0)
    #se hace ve si se vendio de ser el caso se regresa al menu
    if id_product==0:
      print("no hubo compras\n intente de nuevo con otro mes")
      print("--"*50)
      time.sleep(time_duration)
      continue
    else:
      #se cuentan los productos vendidos
      cuenta = contar(id_product)
      #se ordenan en Desendente  
      Desc_cuenta=sorted(cuenta.items(),key=itemgetter(1))
      #se ordenan en ascendente  
      Asc_cuenta=sorted(cuenta.items(),key=itemgetter(1),reverse=True)
      n=0
      #imprimo resultados
      print("productos con mayores ventas")
      for Datos in Asc_cuenta[:5]:
        n+=1
        Productos=Productos_name[Datos[0]]
        cantidad=Datos[1]
        print(f"\t{n}.- el producto {Productos} \n\t\ttuvo {cantidad} ventas este mes")

      print("--"*50)
      time.sleep(time_duration)
      n=0
      print("productos con menores ventas")
      for Datos in Desc_cuenta[:5]:
        n+=1
        Productos=Productos_name[Datos[0]]
        cantidad=Datos[1]
        print(f"\t{n}.- el producto {Productos} \n\t\ttuvo {cantidad} ventas este mes")
      
      #funcion busqueda 
      Productos_del_mes=set(id_product)
      cuenta_busquedas={}
      for Datos in Productos_del_mes:
        id=Datos
        if Productos_Buscados.get(Datos,0) == 0:
          cantidad_buscada=0
        else:
          cantidad_buscada=len(Productos_Buscados.get(Datos))
        if id not in cuenta_busquedas.keys() :
          cuenta_busquedas[id] = []
        cuenta_busquedas[id].append(cantidad_buscada)
      #fin funcion busqueda 
      #se ordenan en Desendente  
      Desc_busquedas=sorted(cuenta_busquedas.items(),key=itemgetter(1))
      #se ordenan en ascendente  
      Asc_busquedas=sorted(cuenta_busquedas.items(),key=itemgetter(1),reverse=True)
      n=0
      print("--"*50)
      time.sleep(time_duration)
      #imprimo resultados
      print("productos con mayor busquedas")
      for Datos in Asc_busquedas[:10]:
        n+=1
        cantidad=Datos[1]
        name=Productos_name[Datos[0]]
        print(f"\t{n}.- el producto {name} \n\t\ttuvo {cantidad} busquedas este mes")
      n=0
      print("--"*50)
      time.sleep(time_duration)
      print("productos con menores busquedas")
      for Datos in Desc_busquedas[:10]:
        n+=1
        cantidad=Datos[1]
        name=Productos_name[Datos[0]]
        print(f"\t{n}.- el producto {name} \n\t\ttuvo {cantidad} busquedas este mes")
      print("--"*50)
      time.sleep(time_duration)
  elif opcion == '2':
    
    #paso uno se organizan los productos vendidos al mes
    # se selecciona el mes deceado
    opcion1=input("introduzca mes de la siguiente forma MM\n")
    opcion2=input("introduzca  a;o de la siguiente forma YYYY\n")
    #se meten los productos vendidos en el mes en id_productos
    id_product=Productostotal_ClasificadosporMes.get(F"{opcion1}/{opcion2}",0)
     #se hace ve si se vendio de ser el caso se regresa al menu
    if id_product==0:
      print("no hubo compras\n intente de nuevo con otro mes")
      print("--"*50)
      time.sleep(time_duration)
      continue
    else:
      Productos_del_mes=list(set(id_product))
      score_mes={}
      for Datos in Productos_del_mes:
        if Datos not in score_mes.keys() :
          score_mes[Datos]=[]
        score_mes[Datos].append(score_dic[Datos]) 
      #se ordenan en Desendente  
      Desc_busquedas=sorted(score_mes.items(),key=itemgetter(1))
      #se ordenan en ascendente  
      Asc_busquedas=sorted(score_mes.items(),key=itemgetter(1),reverse=True)
      n=0
      time.sleep(time_duration)
      #imprimo resultados
      print("productos con mayor score")
      for Datos in Asc_busquedas[:5]:
        n+=1
        cantidad=Datos[1]
        name=Productos_name[Datos[0]]
        print(f"\t{n}.- el producto {name} \n\t\ttuvo un score de {cantidad}  este mes")
      print("--"*50)
      time.sleep(time_duration)
      n=0
      print("productos con menor score")
      for Datos in Desc_busquedas[:5]:
        n+=1
        cantidad=Datos[1]
        name=Productos_name[Datos[0]]
        print(f"\t{n}.- el producto {name} \n\t\ttuvo un score de {cantidad}  este mes")
      n=0
      print("--"*50)
      time.sleep(time_duration)
      
  elif opcion == '3':
    #paso uno se ordena los meses para facilitar la impresion de datos 
    listsuma_precios_mes=[]
    list_meses=[]
    listcont_ventas=[]
    Productos_utiles=[]
    for i in range(12):
      suma_precios_mes=0
      i+=1
      if i>9:
        mes=str(i)+'/2020'
      else:
        mes='0'+str(i)+'/2020'
      #se introduce la informacion del mes ya ordenada, mes a mes en id_product 
      id_product=Productos_ClasificadosporMes.get(mes,[])
      #se saca el dato de precio de cada producto 
      for dato in id_product:
        precios_productos_mes=Productos_precio[dato]
      # se cuenta cuantas ventas se hicieron usando la funcion len()
      cont_ventas=len(id_product)
      # si no hubo ventas confirmo que cont_ventas es 0
      if cont_ventas==0:
        suma_precios_mes=0
      else:
        suma_precios_mes=sum(precios_productos_mes)
      listsuma_precios_mes.append(suma_precios_mes)
      listcont_ventas.append(cont_ventas)
      list_meses.append(mes)
    n=0
    #imprimo resultados
    for i in range(12):
      print(f"esta fecha {list_meses[i]} se vendieron {listcont_ventas[i]} de productos generando una ganacia de {listsuma_precios_mes[i]}")
      if   listcont_ventas[i] > listcont_ventas[i-1]:
        n=i
    print("--"*50)
    time.sleep(time_duration)
    print(f"el mejor mes fue {list_meses[n]} con {listcont_ventas[n]} ventas\n")
    print(f"las ventas  anual fueron {sum(listcont_ventas)}\n")
    print(f"las ventas promedio anual fueron {sum(listcont_ventas)/len(listcont_ventas)}\n")
    
    
  elif opcion == '4':
    #saco todos los productos del año
    Productos_utiles=list(Productos_ClasificadosporMes.values())
    #aplano la lista de lista generada 
    productos_anuales=[elemento for sublista in Productos_utiles for elemento in sublista]
    #quito productos repetidos 
    productos_usados=list(set(productos_anuales))
    productos_a_eliminar=[]
    #se checa que productos no se compraron 
    for i in range(len(lifestore_products)):
      i+=1
      if i not in productos_usados:
        productos_a_eliminar.append(i)
    print("los productos no comprados fueron los siguientes")
    print(productos_a_eliminar)
    print("se recomiendad retirar")
    print("--"*50)
    time.sleep(time_duration)
    Id_stock={}
    #creo el diccionario de Id_stock con producto
    for producto in productos_stock.keys():
      if producto in productos_usados:
        Id_stock[producto]=productos_stock.get(producto)
    Desc_stock=sorted(Id_stock.items(),key=itemgetter(1))
    #fin el diccionario de Id_stock con producto
    n=1
    #imprimo resultados
    for [producto, [stock]] in Desc_stock:
     
      if stock <= 5:
          name=Productos_name[producto]
          print(f"el producto {name} \ntiene {stock} de stock es necesario rellenar\n")
      n+=1
  elif opcion == '5':
    exit()
  else:
    print("opcion no valida")
#Tabla producto con mayores Busquedas 