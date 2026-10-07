
# Cargar todas las librerías
import pandas as pd

'''
import os

print("Carpeta actual:", os.getcwd())
print("Contenido de la carpeta:", os.listdir())
'''

#C:\proye_shada\Comercio\data\Online_Retail.xlsx
df_retail = pd.read_excel('data/Online_Retail.xlsx')

# Muestra los nombres de las columnas

print(df_retail.columns)

#se deberia de cambiar todas las descripciones a minusculas ya que esta mezclado 
'''
Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:

Todos los caracteres deben ser minúsculas.
Elimina los espacios.
Si el nombre tiene varias palabras, utiliza snake_case.
'''

'''
# Bucle en los encabezados poniendo todo en minúsculas
new_columns = []
for col in df_retail.columns:
    col=col.lower()
    new_columns.append(col)
df_retail.columns = new_columns
print(df_retail.columns)
'''


#renombrando los nombres de las columnas, para que este igual que lo de la documentación hacemos esto
# 
# 
# 
# 
#  Cambiar el nombre de la columna "userid"

print(df_retail.columns.tolist())


nuevos_nombres = {
    'InvoiceNo': 'num_factura',
    'StockCode': 'cod_articulo',
    'Description': 'descripcion',
    'Quantity': 'cantidad',
    'InvoiceDate': 'fh_factura',
    'UnitPrice': 'precio_initario',
    'CustomerID': 'id_cliente',
    'Country': 'pais'
}

df_retail = df_retail.rename(columns=nuevos_nombres)



print(df_retail.columns.tolist())


print('*' * 80)
print('*' * 40 +'df_retail------- solo los 5 registros' + '*' * 40)
print(df_retail.head())
print('*' * 80)
print('*' * 80)
print('*' * 40 +'df_retail' + '*' * 40)
#display(df_calls.head())
print('*' * 80)
print(df_retail.info())
print('*' * 80)
print('*' * 40 +'df_retail------- revisión de valores ausentes' + '*' * 40)
print(df_retail.isna().sum())




print('*' * 80)
print('cuenta con valores null--->', df_retail.isnull().sum())
print('*' * 80)
print('*' * 80)



df_retail['id_cliente'] = df_retail['id_cliente'].astype('string')
df_retail['pais'] = df_retail['pais'].astype('string')



print('*' * 80)
print(df_retail.info())
print('*' * 80)
print('*' * 40 +'df_retail------- revisión de valores ausentes' + '*' * 40)
print(df_retail.isna().sum())




'''

# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
#columnas a tratar
colum_cambiar =['track', 'artist','genre']
for col in df.columns:
    if col in colum_cambiar:
        df[col]=df[col].fillna('unknown', inplace =False)
print(df.isna().sum())


'''

ausentes = pd.DataFrame({
    'cantidad': df_retail.isna().sum(),
    'porcentaje': (df_retail.isna().sum() / len(df_retail) * 100).round(2),
    'porcentaje %': (((df_retail.isna().sum() / len(df_retail)) * 100).round(2))*100

})

print(ausentes)

#se observa que hay muy un numero muy mayor de id de cliente ausentes, por lo que haremos procedemos a quitarlos
#print(df_retail.isna.head())
print(df_retail[df_retail['id_cliente'].isna()].head(10))

#para saber cuantos son los registros con <NA>
print(df_retail['id_cliente'].isna().sum())

# veamos los id_cliente de que pasi son :

print(
    df_retail[df_retail['id_cliente'].isna()]['pais'].value_counts()
)
'''

# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
#columnas a tratar
colum_cambiar =['descripcion', 'id_cliente']
for col in df_retail.columns:
    if col in colum_cambiar:
        df_retail[col]=df_retail[col].fillna('unknown', inplace =False)
print(df_retail.isna().sum())



df_retail


'''