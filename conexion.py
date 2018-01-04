# -*- coding: utf-8 -*-
try:
    import pyodbc
except Exception as e:
    print(str(e))
#--------------------------configuracion de la base de datos sql-Server
class Conectar:
    connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=VIU110P0176\SQLEXPRESS;'
                            'Database=mw;')
                            #'uid=VIU110P0176\usuario;pwd=')

    #se crea la tabla reporte
    sql = """
        if not exists (select * from sysobjects where name='reporte_pos' and xtype='U')
        create table reporte_pos (

                             message nvarchar(150),
                             plb_dest nvarchar(50),
                             nm_contacto nvarchar(50),
                             id_grup int,
                             f_full nvarchar(50),
                             tiempo_min nvarchar(50))"""


    '''sql2 = """
        if not exists (select * from sysobjects where name='reporte_neg' and xtype='U')
        create table reporte_neg (

                             message nvarchar(150),
                             plb_dest nvarchar(50),
                             nm_contacto nvarchar(50),
                             id_grup int,
                             f_full nvarchar(50),
                             tiempo_min nvarchar(50))"""
'''

    crsr =connection.execute(sql)
    crsr.commit()
   # crsr2=connection.execute(sql2)
    #crsr2.commit()

#------------------------------------------------tes---- descomentar para probar nombre de la TABLA
#cursor=Conectar.connection.execute("SELECT desc_msg FROM message")
#for mensajes in cursor.fetchall():print(mensajes)
