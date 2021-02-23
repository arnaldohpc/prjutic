# -*- coding: utf-8 -*-

import wx
import psycopg2
from apps import functions


class Query(object):
    # Database queries manager
    def __init__(self):
        # Constructor
        self.functions = functions.Functions()

    def conectar(self):
        logtxt = open("log.txt", "a")
        lognow = self.functions.now_txt()
        self.conn = None
        try:
            # Conexion al servidor de PostgreSQL
            self.conn = psycopg2.connect(
                host="192.168.100.36",
                port="5432",
                database="prjutic",
                user="admin",
                password="admin",
            )
        except (Exception, psycopg2.DatabaseError) as msgtext:
            logtext = "%s - No se pudo conectar a la BD\n%s" % (lognow, str(msgtext))
            logtxt.write(logtext)
            # print mensaje
            error = wx.MessageDialog(
                self,
                "No se pudo conectar a la Base de Datos.\nAvise al Administrador",
                "Error de Conexion",
                wx.OK | wx.ICON_HAND,
            )
            result = error.ShowModal()
            if result == wx.ID_OK:
                pass
        logtxt.close()

    def CerraConexion(self, cursor):
        logtxt = open("log.txt", "a")
        lognow = self.functions.now_txt()
        try:
            cursor.close()
            self.conn.close()
        except (Exception, psycopg2.DatabaseError) as msgtext:
            logtext = "%s - No se puede Cerrar la Conexión de la BD\n" % (
                lognow,
                str(msgtext),
            )
            logtxt.write(logtext)
            # print mensaje
            error = wx.MessageDialog(
                self,
                "No se pudo cerrar la conexion a la Base de Datos.\n\
                    Cierre el Programa y avise al Administrador",
                "Error de Conexión",
                wx.OK | wx.ICON_HAND,
            )
            result = error.ShowModal()
            if result == wx.ID_OK:
                pass
        logtxt.close()

    def SelectUser(self, user):
        self.conectar()
        cursor = self.conn.cursor()
        sqluser = """select * from usuario where usuario = '%s';""" % (user)
        # try:
        cursor.execute(sqluser)
        # except:
        #   self.conn.rollback()
        #   cursor.execute(sqlius, user)
        result = cursor.fetchall()
        self.CerraConexion(cursor)
        return result

    def __del__(self):
        pass
