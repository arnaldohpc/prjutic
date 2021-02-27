# -*- coding: utf-8 -*-


import wx
import wx.xrc


# Class MaterialFrame


class MaterialFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Material",
            pos=wx.DefaultPosition,
            size=wx.Size(420, 520),
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
            wx.Size(280, 20),
            wx.TE_LEFT,
        )
        self.name.SetMaxLength(0)
        self.name.Enable(False)

        fgSizer1.Add(self.name, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtType = wx.StaticText(
            self, wx.ID_ANY, u"Tipo:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtType.Wrap(-1)
        fgSizer1.Add(self.txtType, 0, wx.ALL, 5)

        typeChoices = []
        self.type = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            typeChoices,
            0,
        )
        self.type.Enable(False)

        fgSizer1.Add(self.type, 0, wx.ALL, 5)

        self.txtUnit = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Unidad:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtUnit.Wrap(-1)
        fgSizer1.Add(self.txtUnit, 0, wx.ALL, 5)

        unitChoices = []
        self.unit = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            unitChoices,
            0,
        )
        self.unit.Enable(False)

        fgSizer1.Add(self.unit, 0, wx.ALL, 5)

        self.txtColor = wx.StaticText(
            self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtColor.Wrap(-1)
        fgSizer1.Add(self.txtColor, 0, wx.ALL, 5)

        colorChoices = []
        self.color = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            colorChoices,
            0,
        )
        self.color.Enable(False)

        fgSizer1.Add(self.color, 0, wx.ALL, 5)

        self.txtSize = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Tamaño:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtSize.Wrap(-1)
        fgSizer1.Add(self.txtSize, 0, wx.ALL, 5)

        sizeChoices = []
        self.size = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            sizeChoices,
            0,
        )
        self.size.Enable(False)

        fgSizer1.Add(self.size, 0, wx.ALL, 5)

        self.txtLine = wx.StaticText(
            self, wx.ID_ANY, u"Linea:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtLine.Wrap(-1)
        fgSizer1.Add(self.txtLine, 0, wx.ALL, 5)

        lineChoices = []
        self.line = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            lineChoices,
            0,
        )
        self.line.Enable(False)

        fgSizer1.Add(self.line, 0, wx.ALL, 5)

        self.txtTax = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Impuesto:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtTax.Wrap(-1)
        fgSizer1.Add(self.txtTax, 0, wx.ALL, 5)

        taxChoices = []
        self.tax = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(100, 20),
            taxChoices,
            0,
        )
        self.tax.Enable(False)

        fgSizer1.Add(self.tax, 0, wx.ALL, 5)

        self.txtPrice = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Precio:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtPrice.Wrap(-1)
        fgSizer1.Add(self.txtPrice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.price = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.price.SetMaxLength(0)
        self.price.Enable(False)

        fgSizer1.Add(self.price, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtObs = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Observación:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtObs.Wrap(-1)
        fgSizer1.Add(self.txtObs, 0, wx.ALIGN_TOP | wx.ALL, 5)

        self.obs = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(280, 50),
            wx.TE_RIGHT,
        )
        self.obs.SetMaxLength(0)
        self.obs.Enable(False)

        fgSizer1.Add(self.obs, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtDate = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Fecha Mod.:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtDate.Wrap(-1)
        fgSizer1.Add(self.txtDate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.date = wx.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.DP_DEFAULT,
        )
        self.date.Enable(False)

        fgSizer1.Add(self.date, 0, wx.ALL, 5)

        self.txtActive = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Activado:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtActive.Wrap(-1)
        fgSizer1.Add(self.txtActive, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.active = wx.CheckBox(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(15, 15),
            wx.ALIGN_RIGHT,
        )
        self.active.Enable(False)

        fgSizer1.Add(self.active, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(
            fgSizer1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5
        )

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
        self.btnCancel.Enable(False)

        fgSizer2.Add(self.btnCancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnExit = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(80, 25), wx.NO_BORDER
        )
        fgSizer2.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(fgSizer2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
