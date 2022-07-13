
# Identificación de áreas susceptibles a inundación.

Las inundaciones constituyen uno de los desastres naturales más frecuentes en varias regiones de Colombia, siendo las poblaciones de asentamientos informales particularmente vulnerables frente a estos eventos producto de la mala calidad de las construcciones y la falta de infraestructura para prevenir inundaciones. 

El objetivo de este proyecto es desarrollar un modelo de susceptibilidad a inundaciones, que contribuirán a la generación de información que permita una gestión basada en datos de la crisis humanitaria que se vive en Colombia. 

Como datos iniciales de entrada, el modelo de susceptibilidad a inundación utiliza:
(I) un dataset de datos raster provenientes de satélites ópticos y de radar que representan los factores condicionantes (topográficos, ambientales, antrópicos) que pueden propiciar la ocurrencia de inundaciones,
(II) información georeferenciada en formato vectorial (anotaciones) de áreas donde hayan ocurrido eventos pasados de inundación a lo largo de toda la zona de interés.

Los factores condicionantes para la ocurrencia de inundaciones utilizados son altitud, pendiente, Índice Topográfico de Humedad (TWI, por sus siglas en inglés), Cobertura y Uso de suelo (LULC, por sus siglas en inglés), distancia a rios y distancia a calles.
La selección de los factores condicionantes para el desarrollo del modelo de susceptibilidad a inundaciones estuvo basado principalmente en las características del área de estudio y la disponibilidad de los datos para dicha área. 

Debido a la extensión del área de estudio (aproximadamente 649792 km2) y el gran tamaño de los polígonos de inundación utilizados como anotaciones, todos los factores condicionantes fueron reescalados a una resolución espacial de 500 m de manera de eficientizar la performance del modelo U-Net. 


## Requerimientos

Se utiliza la herramienta **GDAL** en la primera etapa del pre-procesamiento de los datos. Luego, se emplean nuestros paquetes [satproc](https://github.com/dymaxionlabs/satproc) y [unetseg](https://github.com/dymaxionlabs/satproc) para la generación del dataset y modelo de ML respectivamente.

## Notebooks

Este repositorio contiene un conjunto de notebooks de Jupyter, que describen los pasos necesarios:

1. [Entrenamiento](notebooks/1_Entrenamiento.ipynb): Se procesan las imágenes satelitales y la verdad de campo para generar el dataset de entrenamiento. Luego se entrena y evalua el modelo. 
2. [Prediccion](notebooks/2_Prediccion.ipynb): Predicción sobre la región de interés y procesamiento de los resultados de la predicción.


## :handshake: Contribuciones

Reportes de bugs y *pull requests* pueden ser reportados en la [página de issues](https://github.com/dymaxionlabs/adefinir) de este repositorio. Este proyecto está destinado a ser un espacio seguro y acogedor para la colaboración, y se espera que los contribuyentes se adhieran al código de conducta [Contributor
Covenant](http://contributor-covenant.org).

## :page_facing_up: Licencia

El código está licenciado bajo Apache 2.0. Refiérase a [LICENSE.txt](LICENSE.txt).
