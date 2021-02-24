# -*- coding: utf-8 -*-

import wx
import wx.xrc
from apps import functions

# Class MenuFrame


class MenuFrame(wx.Frame):
    def __init__(self, parent, user):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Menu",
            pos=wx.DefaultPosition,
            size=wx.Size(1020, 750),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )
        # Operador
        self.operador = user
        # Permite setear la variable local para la aplicacion en Espanhol
        self.a = wx.Locale(wx.LANGUAGE_SPANISH)
        self.Maximize(True)
        # Instanciamos el Objeto Funciones para trabajar Metodos Guardados
        self.functions = functions.Functions()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.bMenu = wx.MenuBar(0)
        self.mMenu = wx.Menu()
        self.iExit = wx.MenuItem(
            self.mMenu, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mMenu.Append(self.iExit)

        self.bMenu.Append(self.mMenu, u"Menu")

        self.mSales = wx.Menu()
        self.iClient = wx.MenuItem(
            self.mSales, wx.ID_ANY, u"Cliente", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSales.Append(self.iClient)

        self.iSale = wx.MenuItem(
            self.mSales, wx.ID_ANY, u"Venta", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSales.Append(self.iSale)

        self.sRsales = wx.Menu()
        self.iRsales = wx.MenuItem(
            self.sRsales, wx.ID_ANY, u"Ventas", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRsales.Append(self.iRsales)

        self.iRclient = wx.MenuItem(
            self.sRsales, wx.ID_ANY, u"Clientes", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRsales.Append(self.iRclient)

        self.mSales.AppendSubMenu(self.sRsales, u"Reportes")

        self.bMenu.Append(self.mSales, u"Ventas")

        self.mSupply = wx.Menu()
        self.iProvider = wx.MenuItem(
            self.mSupply, wx.ID_ANY, u"Proveedor", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSupply.Append(self.iProvider)

        self.iMaterial = wx.MenuItem(
            self.mSupply, wx.ID_ANY, u"Material", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSupply.Append(self.iMaterial)

        self.iSupply = wx.MenuItem(
            self.mSupply, wx.ID_ANY, u"Compra", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSupply.Append(self.iSupply)

        self.iStock = wx.MenuItem(
            self.mSupply, wx.ID_ANY, u"Stock", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mSupply.Append(self.iStock)

        self.sRsupply = wx.Menu()
        self.iRsupply = wx.MenuItem(
            self.sRsupply, wx.ID_ANY, u"Compras", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRsupply.Append(self.iRsupply)

        self.iRstock = wx.MenuItem(
            self.sRsupply, wx.ID_ANY, u"Existencia", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRsupply.Append(self.iRstock)

        self.iRprovider = wx.MenuItem(
            self.sRsupply, wx.ID_ANY, u"Proveedores", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRsupply.Append(self.iRprovider)

        self.mSupply.AppendSubMenu(self.sRsupply, u"Reportes")

        self.bMenu.Append(self.mSupply, u"Compras")

        self.mHr = wx.Menu()
        self.iEmployee = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Empleado", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iEmployee)

        self.iDepartament = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Departamento", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iDepartament)

        self.iSection = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Seccion", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iSection)

        self.iPosition = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Cargo", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iPosition)

        self.iUser = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Usuario", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iUser)

        self.iProfile = wx.MenuItem(
            self.mHr, wx.ID_ANY, u"Perfil", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHr.Append(self.iProfile)

        self.sRhr = wx.Menu()
        self.iRemployee = wx.MenuItem(
            self.sRhr, wx.ID_ANY, u"Empleados", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sRhr.Append(self.iRemployee)

        self.mHr.AppendSubMenu(self.sRhr, u"Reportes")

        self.bMenu.Append(self.mHr, u"RRHH")

        self.mHelp = wx.Menu()
        self.iHelp = wx.MenuItem(
            self.mHelp, wx.ID_ANY, u"Aceca de...", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mHelp.Append(self.iHelp)

        self.bMenu.Append(self.mHelp, u"Ayuda")

        self.SetMenuBar(self.bMenu)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.iFondo = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            wx.Bitmap(
                self.functions.opj(u"./apps/image.png"),
                wx.BITMAP_TYPE_ANY,
            ),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer1.Add(self.iFondo, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Eventos
        self.Bind(wx.EVT_MENU, self.OnClosed, id=self.iExit.GetId())

    def OnClosed(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
