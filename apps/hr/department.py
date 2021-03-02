# -*- coding: utf-8 -*-


import wx
from apps import functions, dbmanage


# Class DepartmentFrame


class DepartmentFrame(wx.Frame):
    def __init__(self, parent, user_operator, user_profile):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Departamento",
            pos=wx.DefaultPosition,
            size=wx.Size(385, 150),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        # User and Profile
        self.user_operator = user_operator
        self.user_profile = user_profile
        # Instanciamos Funciones y Query para trabajar Metodos Guardados
        self.functions = functions.Functions()
        self.dbmng = dbmanage.Query()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(2, 2, 5, 5)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txtCode = wx.StaticText(
            self, wx.ID_ANY, u"Codigo:", wx.Point(-1, -1), wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtCode.Wrap(-1)
        fgSizer1.Add(self.txtCode, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.code = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.code.SetMaxLength(0)
        self.code.Enable(True)

        fgSizer1.Add(self.code, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtName = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Descripcion:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtName.Wrap(-1)
        fgSizer1.Add(self.txtName, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.name = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(180, 20),
            wx.TE_LEFT,
        )
        self.name.SetMaxLength(0)
        self.name.Enable(False)
        fgSizer1.Add(self.name, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(fgSizer1, 0, wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.btn_ok = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size(80, 25), wx.NO_BORDER
        )
        self.btn_ok.Enable(False)

        fgSizer2.Add(self.btn_ok, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btn_update = wx.Button(
            self,
            wx.ID_ANY,
            u"Modificar",
            wx.DefaultPosition,
            wx.Size(80, 25),
            wx.NO_BORDER,
        )
        self.btn_update.Enable(False)

        fgSizer2.Add(self.btn_update, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btn_cancel = wx.Button(
            self,
            wx.ID_ANY,
            u"Cancelar",
            wx.DefaultPosition,
            wx.Size(80, 25),
            wx.NO_BORDER,
        )
        self.btn_cancel.Enable(False)

        fgSizer2.Add(self.btn_cancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btn_exit = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(80, 25), wx.NO_BORDER
        )
        self.btn_exit.Enable(True)
        self.btn_exit.SetDefault()

        fgSizer2.Add(self.btn_exit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(fgSizer2, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Eventos
        self.code.Bind(wx.EVT_KEY_UP, self.on_key_up)
        self.btn_exit.Bind(wx.EVT_BUTTON, self.on_closed)
        self.btn_ok.Bind(wx.EVT_BUTTON, self.click_btn_ok)

    def on_check_code(self, code):
        select = self.dbmng.select_department(code)
        if select:
            self.code.Enable(False)
            self.name.SetValue(select[1])
            self.btn_update.Enable(True)
            self.btn_exit.SetFocus()
        else:
            self.code.SetValue("")
            self.btn_ok.Enable(True)

    def on_save(self, department):
        self.dbmng.insert_department(department)
        self.code.SetFocus()
        self.name.Enable(False)
        self.btn_ok.Enable(False)
        self.btn_exit.SetDefault()

    def on_key_up(self, evt):
        if evt.GetKeyCode() == wx.WXK_TAB or evt.GetKeyCode() == wx.WXK_NUMPAD_ENTER:
            if self.code.GetValue() == "":
                self.name.Enable(True)
                self.name.SetFocus()
                self.code.SetValue("")
                self.btn_ok.Enable(True)
            else:
                self.on_check_code(self.code.GetValue())
        evt.Skip()

    def click_btn_ok(self, evt):
        self.on_save(self.name.GetValue())
        evt.Skip()

    def on_closed(self, evt):
        self.on_clear_fields()
        self.Destroy()
        evt.Skip()

    def on_clear_fields(self):
        self.code.SetValue("")
        self.name.SetValue("")

    def __del__(self):
        pass
