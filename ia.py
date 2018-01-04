'''
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
    ('CAMION CAMIÃ“N','pos'),
    ('PALA','pos'),
    ('CIGO','pos'),
    ('PTX','pos'),
    ('AP','pos'),
    ('SW','pos'),
    ('HUB','pos'),
    ('COMUNICACION COMUNICACIÃ“','pos'),
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
    ('MAÃ‘ANA' ,'neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    ('','neg'),
    (‡è¡
èçö)æáãQÀM	d…ûfA4`r¾,=dğ*£ïµ§5…—.k½	˜ŞÏ«	ô_FXF™„‹Ö†Èõ³¼UTĞbE4ïŞ¼¤9ó¼í<ˆ<±‹pÇ?Ô‚?÷'`|>WÎ|ŸôîYòè­Æ~˜bÊ\\4”wNÄ9f°ß ±y.ï“âw”é›h¾Ÿ+$‰ìZdrfØ°wrûŸ3 u±°£áãäì¶ŠP—*	ÖQ# ›ñ¼Y‡g'_â§F€¬ö–OÌ€tÊm+23˜ÄŠà9æ—e‡Âø¼¨îyb¦Ÿ; ›†5•>#6¥0p²Õ	š çMaÊ•	øRD½5­Lúw½»ÄD¸ùè¢±fì"İö9ÁkÈ?°eœ^¦‰à×*ôõAæ)†CŒ.æt®]“%4œ¡S*WÚD˜‘+Íè)V	[GÄÕzñ¥W9m*­é­»ê|¡-,Då¥`á;ªÿ—\,İaƒØ ÏÜ
Ñ`$gœÍÒ][êlV›c³sæ•Î®YÑ¿yŞOáÚbû‰*6m–Ì(t-E”¡ôhÎ®†ÉPó üÔ5õ“ıµì°éÀÓİ{›bw|é#Ñ†g¢…åAvo
u"s‘°Y'ƒ6ÈsÏsãr7hÅ-g=±§¶Ø›ñÓCü¦Å×œìÏ^…µÎ?è/X|(Qît ¦Ö FÎ›OÔ="³Ò+%*õ&ĞòBk>Í/öOM­ox€‘óKÛ…
ø[ UPÖåÚBÄgı¬!¥“ƒÁËäsÓJW“ö¶D#?ãÿı)Rù,êeŞ­!õTĞï¾	 -£ŠMkP"ùç–eĞh½3fC ÖZƒ²­(4h¢ì2Éè÷¤õÜ:_>Eø*•kÜ{`¬R`hcŒó7êĞŒıŞ½ápnROI•«dùûQ†Uà™ƒ„€&õî“L˜Ø?%R~`£*4*ÂReÓsĞèkº("ïz “ÓÆ…Cj³oöø/¬…İãlöU+„²¾0ÀQà!ÍošiúU@SoÊã«„³æyi4ÄòtÌÖCÖµÎy'ššïOç¥!´"¢U_*"ï/¸,§×¹rÍûÙiİ	ÎBXáK@e¶u{;}v³æî¹@íÄ¯“±³	ë ˜\(²©¿5ˆLŒ½ H?ÏY+¬-ÓšiÆ‘\±û˜´J‹¡xÌjĞ«hPn¬ÇóáùÇö³ÿ^Şbkí|V+äÁéDåŒ	iP6ˆ5`n"x.•©†Z^[5Õî)C0œİÑœO¬ŞÎÓ#—!¥<¾sZ¶+Ä~y¶y˜Eˆ‚ğqËÊN_£:ıxİ3JìÔ!29dv îİËŸÈA½rÉ2Ë0{2d¥ä¡•5kˆÄl ğõû¡ ûólìÆ0Òd_ |¤í'%1n±j2fÑ1JÙQß‚HóP·ù…<¯+r…_fÛ&%–Å0®ãïl§}Q¨w¾!ÏxvîqXÌñeí?§ÉMnä´à2®éÉI“Ë?óé!(¥:B.…?ğ¯(gû»²ùNˆ6öÔÚ´hl&ó4FæléªºÎÿÑºa(0i…,O½zÅ[£_îb+ç®^c<¨YärúC´¢©t„‘·ş“‘ü3îø›‹DÈ¥IÍë?÷Âqpöé¨j˜A¡–6¾Ø3ºŞ:k‰h­À©YeôH¶m+‰û©±™‚B_ÃvkûÚ…ıÓq-õ_$ÀŸ½9vŠ†µŸ¥nmÑëD‚7†õ[Šy’÷w­ÌÙív;7@9g¦ ğ>”&A›œ|.Ñ}Ríp2	M~ ğjÙÆfç2vd1TÌ•1Ö™Ş€‘ª8‹’;C°ºkÄâ´#UŞ=í³Äâ|«Ï±é«›ú™î.œ´×ìddI!¢CDş1CİˆgF²º6Škˆ1sÁdœ›B(K³Uêü'(Èø§0×£l;¥ÆÜTF­˜T&»Ûm²è¤(oh Â¥©Ah½kÂHåwŸ®¶”=L%·)EİŸ“[Q5ƒ%s®g0¤"»?C{«i]‘r:Uu´U$òˆ@PÆÔ³Ò«	üQ·<Ú%>ÚfgÖLŒ†æÆšÇ`¹ïKù[Ë.
]pÄx·9‚XM’›¶k<·p!!Ä„ Mâ]*ÜÔF-Kh•¨´†S)"Ø¯°ÙÄÒû´FÿcĞ…´._‹óõÄğr‡0”¸rÅÈ,{¾sC±øş‡“Á-»ÌH+\#ÓM*¹ÑpYªüÄL	@oğz6‹—ÿJû	*Ö­sS.Ø~|“™-Zío}ÎœÌ h”‚3vÎL¢ñæê<ğ‹¼àœ¿¼õ1Ö!åÁg÷õ¥Æ¸SiéZa–Ã‚Ö¦