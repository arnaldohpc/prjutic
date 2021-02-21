# -*- coding: utf-8 -*-

import wx
import wx.xrc
from apps import menu


# Class LoginFrame


class LoginFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Acceso",
            pos=wx.DefaultPosition,
            size=wx.Size(320, 148),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        fgSizer1 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txtUser = wx.StaticText(
            self, wx.ID_ANY, u"Usuario: ", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.txtUser.Wrap(-1)
        fgSizer1.Add(
            self.txtUser,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.user = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.user.SetMaxLength(0)
        fgSizer1.Add(
            self.user,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.txtPwd = wx.StaticText(
            self, wx.ID_ANY, u"Contraseña: ", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.txtPwd.Wrap(-1)
        fgSizer1.Add(self.txtPwd, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pwd = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_PASSWORD,
        )
        self.pwd.SetMaxLength(0)
        fgSizer1.Add(self.pwd, 0, wx.ALL, 5)

        bSizer2.Add(fgSizer1, 0, 0, 5)

        bSizer1.Add(bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnOk = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.btnOk.SetDefault()
        self.btnOk.Enable(True)

        bSizer3.Add(self.btnOk, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btnCancel = wx.Button(
            self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer3.Add(self.btnCancel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Instancias Objetos para trabajar con Metodos Guardados
        # self.dbmng = cr_querybd.Querys()
        # self.funciones = cr_funciones.Funciones()
        # Eventos
        self.btnCancel.Bind(wx.EVT_BUTTON, self.ClickCancel)
        self.btnOk.Bind(wx.EVT_BUTTON, self.ClickOk)

    def ComparaPass(self, user):
        # self.usuario = self.dbmng.SelectUser(user)
        self.usuario = "admin"
        if self.usuario:
            if self.usuario == str(self.pwd.GetValue()):
                # nivel = self.usuario[0][4]
                # self.frame = menu.MenuFrame(None, nivel, user)
                self.frame = menu.MenuFrame(None)
                self.Destroy()
                self.frame.Show()
            else:
                error = wx.MessageDialog(
                    self,
                    u"El usuario o Contraseña no corresponde.",
                    "Error de Login",
                    wx.OK | wx.ICON_HAND,
                )
                result = error.ShowModal()
                if result == wx.ID_OK:
                    pass
                # self.user.SetValue('')
                # self.pwd.SetValue('')
                # self.user.SetFocus()
        else:
            error = wx.MessageDialog(
                self,
                u"El usuario o Contraseña no corresponde.",
                "Error de Login",
                wx.OK | wx.ICON_HAND,
            )
            result = error.ShowModal()
            if result == wx.ID_OK:
                pass
            # self.user.SetValue('')
            # self.pwd.SetValue('')
            # self.user.SetFocus()

    def ClickOk(self, evt):
        self.ComparaPass(str(self.user.GetValue()))
        evt.Skip()

    def ClickCancel(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
