# -*- coding: utf-8 -*-


import wx
from apps import login


class App(wx.App):
    def OnInit(self):
        # Permite setear la variable local para la aplicacion en Espanhol
        self.local = wx.Locale(wx.LANGUAGE_SPANISH)
        # redirect = False
        self.frame = login.LoginFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = App(False)
    app.MainLoop()
