python 2.7
librerias

#pip install nltk ---->nltk machineLearnig
#python -m textblob.download_corpora --->herramientas de nltk para funcionar
#pip pyodbc -->controlador sqlserver
#pip colorama ---->("color a las salida de los print")---se puede omitir e eliminar los colores


1)En el modulo conexión va la configuración de la base de datos MYSQLServer

----------------------------------------------------------------------------------------

2)En el modulo (ia) esta la lógica..

configuración para aprender (ia)
en la variable train es una list que contiene los valores para aprender

train =[('falla en gps pala','pos'),('hola como están','neg')]

"ajustar el entrenamiento de acuerdo a sus políticas, entre mas datos le enseñemos, mas preparado estará para responder ia"


3)********************************************Sql********************************************
ia aplica sobre un tabla determinada y según el contenido string de una columna ia tomara una decisión

* >>> if cl.classify(i)=="pos":Si el resultado es 'pos'=positivo "podremos ejecutar cualquier consulta sql ejempo (select * from order by ) inner join etc..."

* >>> if cl.classify(i)=="neg":Si el resultado es 'neg' negativo "ejecutar cualquier otra instrucción"


PD:podremos modificar la sentencia SQL a nuestra nesesidades....