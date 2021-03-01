# -*- coding: utf-8 -*-


import wx
import wx.xrc

# Class UnitFrame


class UnitFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Unidad de Medida",
            pos=wx.DefaultPosition,
            size=wx.Size(385, 180),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

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
        self.code.Enable(False)

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
        fgSizer1.Add(self.name, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtAlias = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Abreviado:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtAlias.Wrap(-1)
        fgSizer1.Add(self.txtAlias, 0, wx.ALL, 5)

        self.alias = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(40, 20),
            wx.TE_RIGHT,
        )
        self.alias.SetMaxLength(0)
        self.alias.Enable(False)

        fgSizer1.Add(self.alias, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.btnOk = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size(80, 25), wx.NO_BORDER
        )
        self.btnOk.Enable(False)

        fgSizer2.Add(self.btnOk, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnModify = wx.Button(
            self,
            wx.ID_ANY,
            u"Modificar",
            wx.DefaultPosition,
            wx.Size(80, 25),
            wx.NO_BORDER,
        )
        self.btnModify.Enable(False)

        fgSizer2.Add(self.btnModify, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnCancel = wx.Button(
            self,
            wx.ID_ANY,
            u"Cancelar",
            wx.DefaultPosition,
            wx.Size(80, 25),
            wx.NO_BORDER,
        )
        self.btnCancel.SetDefault()
        fgSizer2.Add(self.btnCancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnExit = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(80, 25), wx.NO_BORDER
        )
        fgSizer2.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(fgSizer2, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def on_closed(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
