# -*- coding: utf-8 -*-

import wx
import wx.xrc
from apps import functions
from apps.hr import department, employee, position, profile, section
from apps.sales import client, sale, tax
from apps.supplies import provider, supply
from apps.warehousemng import (
    color,
    line,
    material,
    office,
    size,
    subline,
    typepro,
    unitmt,
    warehouse,
)

# Class MenuFrame


class MenuFrame(wx.Frame):
    def __init__(self, parent, user_operator, user_profile):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Menu",
            pos=wx.DefaultPosition,
            size=wx.Size(1020, 750),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )
        # User and Profile
        # self.user_operator = user_operator
        # self.user_profile = user_profile
        # Permite setear la variable local para la aplicacion en Espanhol
        self.a = wx.Locale(wx.LANGUAGE_SPANISH)
        self.Maximize(True)
        # Instanciamos el Objeto Funciones para trabajar Metodos Guardados
        self.functions = functions.Functions()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.b_menu = wx.MenuBar(0)
        self.m_menu = wx.Menu()
        self.i_exit = wx.MenuItem(
            self.m_menu, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu.Append(self.i_exit)

        self.b_menu.Append(self.m_menu, u"Menu")

        self.m_hr = wx.Menu()
        self.i_employee = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Empleado", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_employee)

        self.i_departament = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Departamento", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_departament)

        self.i_section = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Seccion", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_section)

        self.i_position = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Cargo", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_position)

        self.i_user = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Usuario", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_user)

        self.i_profile = wx.MenuItem(
            self.m_hr, wx.ID_ANY, u"Perfil", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_hr.Append(self.i_profile)

        self.sm_r_hr = wx.Menu()
        self.i_r_employee = wx.MenuItem(
            self.sm_r_hr, wx.ID_ANY, u"Empleados", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_hr.Append(self.i_r_employee)

        self.m_hr.AppendSubMenu(self.sm_r_hr, u"Reportes")

        self.b_menu.Append(self.m_hr, u"RRHH")

        self.m_sales = wx.Menu()
        self.i_client = wx.MenuItem(
            self.m_sales, wx.ID_ANY, u"Cliente", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_sales.Append(self.i_client)

        self.i_sale = wx.MenuItem(
            self.m_sales, wx.ID_ANY, u"Venta", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_sales.Append(self.i_sale)

        self.i_tax = wx.MenuItem(
            self.m_sales, wx.ID_ANY, u"Impuestos", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_sales.Append(self.i_tax)

        self.sm_r_sales = wx.Menu()
        self.i_r_sales = wx.MenuItem(
            self.sm_r_sales, wx.ID_ANY, u"Ventas", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_sales.Append(self.i_r_sales)

        self.i_r_client = wx.MenuItem(
            self.sm_r_sales, wx.ID_ANY, u"Clientes", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_sales.Append(self.i_r_client)

        self.m_sales.AppendSubMenu(self.sm_r_sales, u"Reportes")
        self.b_menu.Append(self.m_sales, u"Ventas")

        self.m_supplies = wx.Menu()
        self.i_provider = wx.MenuItem(
            self.m_supplies, wx.ID_ANY, u"Proveedor", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_supplies.Append(self.i_provider)

        self.i_material = wx.MenuItem(
            self.m_supplies, wx.ID_ANY, u"Material", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_supplies.Append(self.i_material)

        self.i_supply = wx.MenuItem(
            self.m_supplies, wx.ID_ANY, u"Compra", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_supplies.Append(self.i_supply)

        self.sm_r_supply = wx.Menu()
        self.i_r_supply = wx.MenuItem(
            self.sm_r_supply, wx.ID_ANY, u"Compras", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_supply.Append(self.i_r_supply)

        self.i_r_stock = wx.MenuItem(
            self.sm_r_supply, wx.ID_ANY, u"Existencia", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_supply.Append(self.i_r_stock)

        self.i_r_provider = wx.MenuItem(
            self.sm_r_supply, wx.ID_ANY, u"Proveedores", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_supply.Append(self.i_r_provider)

        self.m_supplies.AppendSubMenu(self.sm_r_supply, u"Reportes")

        self.b_menu.Append(self.m_supplies, u"Compras")

        self.m_warehousemng = wx.Menu()
        self.i_color = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Color", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_color)

        self.i_line = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Line", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_line)

        self.i_material = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Material", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_material)

        self.i_office = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Sucursal", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_office)

        self.i_size = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Tamaño", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_size)

        self.i_subline = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"SubLinea", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_subline)

        self.i_typepro = wx.MenuItem(
            self.m_warehousemng,
            wx.ID_ANY,
            u"Tipo Producto",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.m_warehousemng.Append(self.i_typepro)

        self.i_unitmt = wx.MenuItem(
            self.m_warehousemng,
            wx.ID_ANY,
            u"Unidad de Medida",
            wx.EmptyString,
            wx.ITEM_NORMAL,
        )
        self.m_warehousemng.Append(self.i_unitmt)

        self.i_warehouse = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Deposito", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_warehouse)

        self.i_stock = wx.MenuItem(
            self.m_warehousemng, wx.ID_ANY, u"Stock", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_warehousemng.Append(self.i_stock)

        self.sm_r_warehouse = wx.Menu()
        self.i_r_material = wx.MenuItem(
            self.sm_r_warehouse, wx.ID_ANY, u"Materiales", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_warehouse.Append(self.i_r_material)

        self.i_r_stock = wx.MenuItem(
            self.sm_r_warehouse, wx.ID_ANY, u"Stock", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.sm_r_warehouse.Append(self.i_r_stock)

        self.m_warehousemng.AppendSubMenu(self.sm_r_warehouse, u"Reportes")

        self.b_menu.Append(self.m_warehousemng, u"Deposito")

        self.m_help = wx.Menu()
        self.i_help = wx.MenuItem(
            self.m_help, wx.ID_ANY, u"Aceca de...", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_help.Append(self.i_help)

        self.b_menu.Append(self.m_help, u"Ayuda")

        self.SetMenuBar(self.b_menu)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.i_fondo = wx.StaticBitmap(
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
        bSizer1.Add(self.i_fondo, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Activar menus
        if user_profile > 0:
            self.i_client
        # Eventos
        self.Bind(wx.EVT_MENU, self.on_department, id=self.i_departament.GetId())
        self.Bind(wx.EVT_MENU, self.on_employee, id=self.i_employee.GetId())
        self.Bind(wx.EVT_MENU, self.on_position, id=self.i_position.GetId())
        self.Bind(wx.EVT_MENU, self.on_profile, id=self.i_profile.GetId())
        self.Bind(wx.EVT_MENU, self.on_section, id=self.i_section.GetId())
        self.Bind(wx.EVT_MENU, self.on_client, id=self.i_client.GetId())
        self.Bind(wx.EVT_MENU, self.on_sale, id=self.i_sale.GetId())
        self.Bind(wx.EVT_MENU, self.on_tax, id=self.i_tax.GetId())
        self.Bind(wx.EVT_MENU, self.on_provider, id=self.i_provider.GetId())
        self.Bind(wx.EVT_MENU, self.on_supply, id=self.i_supply.GetId())
        self.Bind(wx.EVT_MENU, self.on_color, id=self.i_color.GetId())
        self.Bind(wx.EVT_MENU, self.on_size, id=self.i_size.GetId())
        self.Bind(wx.EVT_MENU, self.on_typepro, id=self.i_typepro.GetId())
        self.Bind(wx.EVT_MENU, self.on_unitmt, id=self.i_unitmt.GetId())
        self.Bind(wx.EVT_MENU, self.on_warehouse, id=self.i_warehouse.GetId())
        self.Bind(wx.EVT_MENU, self.on_closed, id=self.i_exit.GetId())

    def on_department(self, evt):
        self.clframe = department.DepartmentFrame(self)
        self.clframe.Show(True)

    def on_employee(self, evt):
        self.clframe = employee.EmployeeFrame(self)
        self.clframe.Show(True)

    def on_position(self, evt):
        self.clframe = position.PositionFrame(self)
        self.clframe.Show(True)

    def on_profile(self, evt):
        self.clframe = profile.ProfileFrame(self)
        self.clframe.Show(True)

    def on_section(self, evt):
        self.clframe = section.SectionFrame(self)
        self.clframe.Show(True)

    def on_client(self, evt):
        self.clframe = client.ClientFrame(self)
        self.clframe.Show(True)

    def on_sale(self, evt):
        self.clframe = sale.SalesFrame(self)
        self.clframe.Show(True)

    def on_tax(self, evt):
        self.clframe = tax.TaxFrame(self)
        self.clframe.Show(True)

    def on_provider(self, evt):
        self.clframe = provider.ProviderFrame(self)
        self.clframe.Show(True)

    def on_supply(self, evt):
        self.clframe = supply.SupplyFrame(self)
        self.clframe.Show(True)

    def on_color(self, evt):
        self.clframe = color.ColorFrame(self)
        self.clframe.Show(True)

    def on_line(self, evt):
        self.clframe = line.LineFrame(self)
        self.clframe.Show(True)

    def on_material(self, evt):
        self.clframe = material.MaterialFrame(self)
        self.clframe.Show(True)

    def on_office(self, evt):
        self.clframe = office.OfficeFrame(self)
        self.clframe.Show(True)

    def on_size(self, evt):
        self.clframe = size.SizeFrame(self)
        self.clframe.Show(True)

    def on_subline(self, evt):
        self.clframe = subline.SublineFrame(self)
        self.clframe.Show(True)

    def on_typepro(self, evt):
        self.clframe = typepro.TypeFrame(self)
        self.clframe.Show(True)

    def on_unitmt(self, evt):
        self.clframe = unitmt.UnitFrame(self)
        self.clframe.Show(True)

    def on_warehouse(self, evt):
        self.clframe = warehouse.WarehouseFrame(self)
        self.clframe.Show(True)

    def on_closed(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
