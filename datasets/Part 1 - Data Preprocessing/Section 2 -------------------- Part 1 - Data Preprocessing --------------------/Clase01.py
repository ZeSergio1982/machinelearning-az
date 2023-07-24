# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:56:06 2023

@author: clopezs
"""

# Plantilla de pre procesado

# Cómo importar las librerías

#numpy contiene herramientas matemáticas para python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('Data.csv')

# Tomamos todas las columnas, excepto la última (-1), al poner los 2 puntos indicamos todas las filas, y todas las columnas, excepto la última
# iloc = localizar index, [fila, columna]
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Tratamiento de los valores nan's - quitar los nulos
# solo descargamos la función o fase que necesitamos de la librería sklearn


# from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer

#valores con nan se sustotuyen con la media de la columna: mean y el axis 0, para fila es axis = 1
# imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", axis = 0)
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(x[:, 1:3])     # toma las columnas 1 y 2, recordando que empieza en cero
x[:, 1:3] = imputer.transform(x[:, 1:3])