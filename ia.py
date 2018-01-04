﻿'''
# -*- coding: utf-8 -*-
#__author__ = 'lliscano>>>luisthemaster3@gmail.com'
try:
    from conexion import Conectar
    from textblob.classifiers import NaiveBayesClassifier
    import colorama#<---color
    from string import replace
    import csv
except Exception as e:
    print (str(e))

#entrenamiento
import string
train =[
#--------------------------------------------Entrenamiento (NEGATIVO)-----------------------------------------------------------------------
    ('funcionan','pos'),
    ('disponibilidad','pos'),
    ('ticket','pos'),
    ('problema', 'pos'),
    ('incidente', 'pos'),
    ('flota', 'pos'),
    ('caso', 'pos'),
    ('incidente','pos'),
    ('incidencia','pos'),
    ('flota','pos'),
    ('linea','pos'),
    ('disponibilidad','pos'),
    ('dispatch','pos'),
    ('cdh','pos'),
    ('cac','pos'),
    ('ppv','pos'),
    ('peb','pos'),
    ('pa','pos'),
    ('cf','pos'),
    ('ph','pos'),
    ('TRC','pos'),
    ('TRK','pos'),
    ('RE','pos'),
    ('MT','pos'),
    ('CR','pos'),
    ('RC','pos'),
    ('WD','pos'),
    ('perforadora','pos'),
    ('camion','pos'),
    ('pala','pos'),
    ('cigo','pos'),
    ('ptx','pos'),
    ('ap','pos'),
    ('sw','pos'),
    ('hub','pos'),
    ('comunicacion','pos'),
    ('monitoreo','pos'),
    ('perfo','pos'),
    ('server','pos'),
    ('servidor','pos'),
    ('rimo','pos'),
    ('mesh','pos'),
    ('carro','pos'),
    ('cm','pos'),
    ('gps','pos'),
    ('trimble','pos'),
    ('bd','pos'),
    ('sql','pos'),
    ('snow','pos'),
    ('service','pos'),
    ('inc','pos'),
    ('ticket','pos'),
    ('L&S','pos'),
    ('LYS','pos'),
    ('netaxxion','pos'),
    ('netaxion','pos'),
    ('minera','pos'),
    ('titan','pos'),
    ('chancador','pos'),
    ('confluencia','pos'),
    ('placa','pos'),
    ('holding tank','pos'),
    ('survey','pos'),
    ('cobertura','pos'),
    ('conexion','pos'),
    ('access point','pos'),
    ('mantenimiento','pos'),
    ('mantencion','pos'),
    ('panne','pos'),
    ('operativo','pos'),
    ('sistemas sistema SISTEMAS','pos'),
#--------------------------------------------Entrenamiento (NEGATIVO)-----------------------------------------------------------------------
    ('hola', 'neg'),
    ('saludos','neg'),
    ("cordial", 'neg'),
    ('comedor', 'neg'),
    ('Buenos equipos','neg'),
    ('comida','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),]

#gurdamos en archivo csv lo que la ia a aprendido
a=open("learnig/aprendido.csv","w")
a_csv=csv.writer(a)
for i in train:
    a_csv.writerow(i)
a.close()
#entremamos a ia


cl = NaiveBayesClassifier(train,)

#color de salida prinnt
RED = colorama.Fore.RED
BLUE=colorama.Fore.BLUE
#Tabla aplicat ia
cursor1=Conectar.connection.execute("SELECT desc_msg FROM message ORDER BY id_message")#<----en la tabla menssge se agrego una columna id_message para que lo ordene por id pero puede cambiorlo por fecha

from datetime import datetime
t=datetime.now()
fecha=t.date()


for i in cursor1.fetchall():
    i=(str(i))
    #i=string.capitalize(i)
    if cl.classify(i)=="pos":
        #si el resultado es (POSITIVO)
        #se ejecuta el sql
        a=Conectar.connection.execute("SELECT desc_msg ,id_message FROM message WHERE  desc_msg LIKE '"+str(i[3:-4])+"'")

        print(BLUE)#--colorama
        result=(a.fetchall(),"<-----<<<Importante>>>")
        print(result)


        #"Guardar archivo txt "imotante" ")
        archivo_impor = open("metadata/importante_%s.txt"%fecha,'a')
        archivo_impor.write(str(result))
        archivo_impor.write("\n")
        archivo_impor.write("\n")
        archivo_impor.close()

    elif cl.classify(i)=="neg":
        #Si el resultado es (NEGATIVO)
        #se ejecuta el sql
        b=Conectar.connection.execute("SELECT desc_msg,id_message  FROM message WHERE  desc_msg LIKE '"+str(i[3:-4])+"'")

        print(RED)#<--colorama
        result2 = (b.fetchall(),"<-----<<<Irrelevante>>>")
        print result2

        #"Guardar archivo txt "Irrelevante" ")
        archivo_irre = open("metadata/irrelevante_%s.txt"%fecha,'a')
        archivo_irre.write(str(result2))
        archivo_irre.write("\n")
        archivo_irre.write("\n")
        archivo_irre.close()


#tes de entrenamiento
print(cl.classify("reporte de la pala"))# "?"
print(cl.classify("hola como estas "))# "?"
print("Accuracy: {0}".format(cl.accuracy(train)))
'''
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: latin-1 -*-
#__author__ = 'lliscano>>>luisthemaster3@gmail.com'

try:
    # --------------Importante para el manejo de string )----------------
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    from conexion import Conectar # DATA BASE
    from textblob.classifiers import NaiveBayesClassifier as NBC #el clasificador
    from datetime import datetime #<--- fecha al archivo
    import string
except Exception as e:
    print (str(e))

fecha=str(datetime.now()).replace(":","-").replace(" ","_")
print(fecha)

train =[
#--------------------------------------------Entrenamiento (POSITIVO)-----------------------------------------------------------------------
    ('FUNCIONA','pos'),
    ('DISPONIBILIDAD DISPONIBLE','pos'),
    ('TICKET','pos'),
    ('PROBLEMA PROBLEMAS', 'pos'),
    ('INCIDENTE', 'pos'),
    ('FLOTA', 'pos'),
    ('CASO', 'pos'),
    ('SERVIDOR','pos'),
    ('INICIDENCIA','pos'),
    ('SERVICIOS,','pos'),
    ('LINEA','pos'),
    ('TRC20 ','pos'),
    ('DISPATCH','pos'),
    ('CDH','pos'),
    ('CAC','pos'),
    ('PPV','pos'),
    ('PEB','pos'),
    ('PA','pos'),
    ('CF','pos'),
    ('PH','pos'),
    ('TRC','pos'),
    ('TRK','pos'),
    ('RE','pos'),
    ('MT','pos'),
    ('CR','pos'),
    ('RC','pos'),
    ('WD','pos'),
    ('PERFORADORA','pos'),
    ('CAMION CAMIÓN','pos'),
    ('PALA','pos'),
    ('CIGO','pos'),
    ('PTX','pos'),
    ('AP','pos'),
    ('SW','pos'),
    ('HUB','pos'),
    ('COMUNICACION COMUNICACIÓ','pos'),
    ('MANITOREO','pos'),
    ('PERFO','pos'),
    ('SERVER','pos'),
    ('SERVIDOR','pos'),
    ('RIMO','pos'),
    ('MESH','pos'),
    ('CARRO','pos'),
    ('CM','pos'),
    ('GPS','pos'),
    ('TRIMBLE','pos'),
    ('DB','pos'),
    ('SQL','pos'),
    ('SNOW','pos'),
    ('SERVICE','pos'),
    ('INC','pos'),
    ('TICKETE','pos'),
    ('L&S','pos'),
    ('LYS','pos'),
    ('NETAXXION','pos'),
    ('NETAXION','pos'),
    ('MINERA','pos'),
    ('TITAN','pos'),
    ('CHANCADOR','pos'),
    ('CONFLUENCIA','pos'),
    ('PLACA','pos'),
    ('HOLDING TANK','pos'),
    ('SURVEY','pos'),
    ('COBERTURA','pos'),
    ('CONEXION','pos'),
    ('ACCESS POINT','pos'),
    ('MANTENIMIENTO','pos'),
    ('MANTENCION','pos'),
    ('PANNE POWERVIEW','pos'),
    ('OPERATIVO','pos'),
    ('SISTEMAS SISTEMA','pos'),
#--------------------------------------------Entrenamiento (NEGATIVO)-----------------------------------------------------------------------
    ('HOLA GRUPO', 'neg'),
    ('SALUDOS','neg'),
    ('CORDIAL', 'neg'),
    ('COMEDOR', 'neg'),
    ('BUENAS','neg'),
    ('COMIDA','neg'),
    ('PLAYA','neg'),
    ('MAÑANA' ,'neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    (��
���)���Q�M�	d��fA4`r��,�=d�*�ﵧ5��.k��	��ϫ	�_FX�F���������UT�bE4����9��<�<��p�?Ԃ?�'`|>W�|���Y���~�b��\\4�wN�9f�� �y.�w��h��+$��Zdrfذwr��3 u������춊P�*	�Q# �����Y�g'_�F�����Òt��m+23�Ċ�9�e������yb��;���5�>#6��0p��	� �Maʕ	�RD�5�L�w����D��袱f�"��9�k�?�e�^����*��A�)�C�.�t�]�%4��S*W�D��+��)V	[�G��z�W�9m*�魻�|�-,D�`�;���\,�a�� ��
�`$g���][�lV�c�s�ήYѿy�O��b��*6m��(t-E���hή��P� ��5���������{�bw|�#цg���Avo
u"s��Y'�6�s�s�r7h�-g=�������C���ōל��^���?�/X|(Q�t �� FΛO�="��+%*�&��B�k>�/�OM�ox���Kۅ
�[ UP���B�g��!������s�JW���D#?���)R�,�eޭ!�T��	 -��MkP"���e�h�3fC �Z���(4h��2������:_>E�*�k�{`�R`hc��7�Ќ�޽�pnROI��d��Q�U������&��L��?%R~`�*4*�Re�s��k�("�z ��ƅCj�o��/����l�U+���0�Q�!�o�i�U@So�㫄��yi4��t��Cֵ�y'���O��!�"�U_*"�/��,�׹r���i�	�BX�K@e�u{;}v���@�į����	� �\(���5�L�� H?�Y+�-ӚiƑ\�����J��x�jЫhPn���������^�bk�|V+���D�	iP6�5`n"x.���Z^[5��)C0����O����#�!�<�sZ��+�~y�y�E���q��N_�:�x�3J��!29d�v ��˟ȞA�r�2�0{2d�䡕5k��l ����� ��l��0�d_�|��'%1n�j2�f��1J�Q߂H�P���<�+r�_f�&%��0���l�}Q�w�!�xv�qX��e�?��Mn䁴�2���I��?��!(�:B.�?��(g�����N�6�ԏ��hl&�4�F�l骺��Ѻa(0i�,O�z��[�_�b+�^c<�Y�r��C���t�������3����D��I��?��qp��j�A��6��3��:k�h���Ye�H�m+������B_�vk��څ��q-�_$���9v�����nm��D�7���[�y��w����v;7@9g���>�&A��|.�}R�p2	M~��j��f�2vd1T̕1֙ހ��8��;C��k��#�U��=���|�ϱ髛���.����d�dI!�CD�1C݈gF��6�k�1s��d��B(K�U��'(���0���l;���TF��T&��m����(oh ¥�Ah�k�H��w����=L%�)Eݟ��[Q5�%s�g0�"�?C{�i]�r:Uu�U$�@P�Գҫ	��Q�<�%>�fg�L�������`��K�[�.
]p�x�9�XM���k<�p!!Ą�M�]*��F-Kh����S)"د������F�cЅ�._�����r�0��r�ȍ,{�sC�������-��H+\#�M*��pY���L	@o�z6���J�	*֭sS.�~|��-�Z�o}Μ̞�h��3v�L����<��������1�!��g����ƸSi�Za�Â֦