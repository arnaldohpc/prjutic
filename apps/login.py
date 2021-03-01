# -*- coding: utf-8 -*-

import wx
import wx.xrc
from apps import dbmanage, menu


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

        self.txtuser = wx.StaticText(
            self, wx.ID_ANY, u"Usuario: ", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.txtuser.Wrap(-1)
        fgSizer1.Add(
            self.txtuser,
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

        self.txtpwd = wx.StaticText(
            self, wx.ID_ANY, u"Contraseña: ", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.txtpwd.Wrap(-1)
        fgSizer1.Add(self.txtpwd, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

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

        self.btn_ok = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.btn_ok.SetDefault()
        self.btn_ok.Enable(True)

        bSizer3.Add(self.btn_ok, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_cancel = wx.Button(
            self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer3.Add(self.btn_cancel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Instancias Objetos para trabajar con Metodos Guardados
        self.dbmng = dbmanage.Query()
        # self.functions = funtions.Functions()
        # Eventos
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.click_cancel)
        self.btn_ok.Bind(wx.EVT_BUTTON, self.click_ok)

    def on_check_user(self, user):
        self.selectuser = self.dbmng.select_user(user)
        if self.selectuser:
            if self.selectuser[0][5] is True and self.selectuser[0][4] is True:
                if self.selectuser[0][2].strip() == self.pwd.GetValue():
                    self.frame = menu.MenuFrame(
                        None, self.selectuser[0][1].strip(), self.selectuser[0][3]
                    )
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
                    self.user.SetValue("")
                    self.pwd.SetValue("")
                    self.user.SetFocus()
            else:
                error = wx.MessageDialog(
                    self,
                    u"El usuario no esta activo.",
                    "Error de Login",
                    wx.OK | wx.ICON_HAND,
                )
                result = error.ShowModal()
                if result == wx.ID_OK:
                    pass
                self.user.SetValue("")
                self.pwd.SetValue("")
                self.user.SetFocus()
        else:
            error = wx.MessageDialog(
                self,
                u"Usuario no encontrado",
                "Error de Login",
                wx.OK | wx.ICON_HAND,
            )
            result = error.ShowModal()
            if result == wx.ID_OK:
                pass
            self.user.SetValue("")
            self.pwd.SetValue("")
            self.user.SetFocus()

    def click_ok(self, evt):
        self.on_check_user(str(self.user.GetValue()))
        evt.Skip()

    def click_cancel(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
