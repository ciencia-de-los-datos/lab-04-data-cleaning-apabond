"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    

    #
    # Inserte su código aquí
    #

    return df
df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
df.dropna(inplace=True)

df["sexo"] = df["sexo"].str.lower()
df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.replace("-"," ").str.replace("_"," ")
df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("-"," ").str.replace("_"," ")
df["barrio"] = df["barrio"].str.lower().str.replace("-"," ").str.replace("_"," ")
df["estrato"] = df["estrato"].astype("category")
df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format='mixed', dayfirst=True)
df["monto_del_credito"] = df["monto_del_credito"].str.replace(",","").str.replace(".00","").str.strip("$")
df["monto_del_credito"] = df["monto_del_credito"].astype(int)
df["línea_credito"] = df["línea_credito"].str.lower().str.replace("-"," ").str.replace("_"," ")

df = df.drop_duplicates()







