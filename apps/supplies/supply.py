# -*- coding: utf-8 -*-


import wx
import wx.xrc
import wx.grid

# Class SupplyFrame


class SupplyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Compras",
            pos=wx.DefaultPosition,
            size=wx.Size(840, 600),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(2, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txtProvider = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Proveedor:",
            wx.DefaultPosition,
            wx.Size(60, 15),
            wx.ALIGN_LEFT,
        )
        self.txtProvider.Wrap(-1)
        fgSizer1.Add(self.txtProvider, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.SetMinSize(wx.Size(-1, 20))
        self.code = wx.SearchCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 20), 0
        )
        self.code.ShowSearchButton(True)
        self.code.ShowCancelButton(False)
        fgSizer2.Add(self.code, 0, wx.ALIGN_CENTER_VERTICAL, 5)

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

        fgSizer2.Add(self.name, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3.AddSpacer((150, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.employee = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(180, 20),
            wx.TE_LEFT,
        )
        self.employee.SetMaxLength(0)
        self.employee.Enable(False)

        fgSizer3.Add(self.employee, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fgSizer1.Add(fgSizer3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtInvoice = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Factura: ",
            wx.DefaultPosition,
            wx.Size(60, 15),
            wx.ALIGN_LEFT,
        )
        self.txtInvoice.Wrap(-1)
        fgSizer1.Add(self.txtInvoice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fgSizer4 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.invoice = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(160, 20),
            wx.TE_LEFT,
        )
        self.invoice.SetMaxLength(0)
        self.invoice.Enable(False)

        fgSizer4.Add(self.invoice, 0, wx.ALL, 5)

        self.txtDate = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Fecha Compra:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtDate.Wrap(-1)
        fgSizer4.Add(self.txtDate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.date = wx.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.Size(125, 20),
            wx.DP_DEFAULT,
        )
        self.date.Enable(False)

        fgSizer4.Add(self.date, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer4, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5.AddSpacer((135, 20), 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.txtWarehouse = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Deposito:",
            wx.DefaultPosition,
            wx.Size(60, 15),
            wx.ALIGN_LEFT,
        )
        self.txtWarehouse.Wrap(-1)
        fgSizer1.Add(self.txtWarehouse, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fgSizer6 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        warehouseChoices = []
        self.warehouse = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(160, 20),
            warehouseChoices,
            0,
        )
        self.warehouse.Enable(False)

        fgSizer6.Add(self.warehouse, 0, wx.ALL, 5)

        self.txtOffice = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Sucursal: ",
            wx.DefaultPosition,
            wx.Size(50, 15),
            wx.ALIGN_LEFT,
        )
        self.txtOffice.Wrap(-1)
        fgSizer6.Add(self.txtOffice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.office = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(155, 20),
            wx.TE_LEFT,
        )
        self.office.SetMaxLength(0)
        self.office.Enable(False)

        fgSizer6.Add(self.office, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer6, 1, wx.EXPAND, 5)

        fgSizer1.AddSpacer((135, 20), 1, wx.EXPAND, 5)

        self.txtObs = wx.StaticText(
            self, wx.ID_ANY, u"Obs:", wx.DefaultPosition, wx.Size(60, 15), wx.ALIGN_LEFT
        )
        self.txtObs.Wrap(-1)
        fgSizer1.Add(self.txtObs, 0, wx.ALL, 5)

        self.obs = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(385, 40),
            wx.TE_LEFT,
        )
        self.obs.SetMaxLength(0)
        self.obs.Enable(False)

        fgSizer1.Add(self.obs, 0, wx.ALL, 5)

        fgSizer7 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer7.SetMinSize(wx.Size(-1, 40))

        fgSizer7.AddSpacer((235, 10), 1, wx.ALL, 5)

        self.txtTotal = wx.StaticText(
            self,
            wx.ID_ANY,
            u"TOTAL",
            wx.DefaultPosition,
            wx.Size(100, 15),
            wx.ALIGN_CENTRE,
        )
        self.txtTotal.Wrap(-1)
        fgSizer7.Add(self.txtTotal, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer7.AddSpacer((10, 10), 1, 0, 5)

        self.employee1 = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_LEFT,
        )
        self.employee1.SetMaxLength(0)
        self.employee1.Enable(False)

        fgSizer7.Add(self.employee1, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer1.Add(fgSizer7, 1, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 0, 0, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.grilla = wx.grid.Grid(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(820, 345), 0
        )

        # Grid
        self.grilla.CreateGrid(15, 6)
        self.grilla.EnableEditing(False)
        self.grilla.EnableGridLines(True)
        self.grilla.EnableDragGridSize(False)
        self.grilla.SetMargins(0, 0)

        # Columns
        self.grilla.SetColSize(0, 100)
        self.grilla.SetColSize(1, 300)
        self.grilla.SetColSize(2, 85)
        self.grilla.SetColSize(3, 85)
        self.grilla.SetColSize(4, 100)
        self.grilla.SetColSize(5, 100)
        self.grilla.EnableDragColMove(False)
        self.grilla.EnableDragColSize(True)
        self.grilla.SetColLabelSize(25)
        self.grilla.SetColLabelValue(0, u"CODIGO")
        self.grilla.SetColLabelValue(1, u"MATERIAL")
        self.grilla.SetColLabelValue(2, u"CANTIDAD")
        self.grilla.SetColLabelValue(3, u"STOCK")
        self.grilla.SetColLabelValue(4, u"PRECIO")
        self.grilla.SetColLabelValue(5, u"MONTO")
        self.grilla.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)

        # Rows
        self.grilla.SetRowSize(0, 20)
        self.grilla.AutoSizeRows()
        self.grilla.EnableDragRowSize(True)
        self.grilla.SetRowLabelSize(45)
        self.grilla.SetRowLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grilla.SetLabelFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString)
        )

        # Cell Defaults
        self.grilla.SetDefaultCellFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString)
        )
        self.grilla.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
        bSizer2.Add(self.grilla, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer2, 0, 0, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        fgSizer8 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.btnOk = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size(80, 30), wx.NO_BORDER
        )
        self.btnOk.SetDefault()
        self.btnOk.Enable(False)

        fgSizer8.Add(self.btnOk, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnCancel = wx.Button(
            self,
            wx.ID_ANY,
            u"Cancelar",
            wx.DefaultPosition,
            wx.Size(80, 25),
            wx.NO_BORDER,
        )
        self.btnCancel.Enable(False)

        fgSizer8.Add(self.btnCancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnExit = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(80, 30), wx.NO_BORDER
        )
        fgSizer8.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer3.Add(fgSizer8, 0, wx.ALIGN_BOTTOM, 5)

        bSizer1.Add(bSizer3, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def on_closed(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
