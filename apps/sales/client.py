# -*- coding: utf-8 -*-


import wx
import wx.xrc


# Class ClientFrame


class ClientFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Cliente",
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

        self.txtRuc = wx.StaticText(
            self,
            wx.ID_ANY,
            u"R.U.C.:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtRuc.Wrap(-1)
        fgSizer1.Add(self.txtRuc, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ruc = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.ruc.SetMaxLength(0)
        fgSizer1.Add(self.ruc, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtName = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Razón Social:",
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

        self.txtCedula = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Cedula:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtCedula.Wrap(-1)
        fgSizer1.Add(self.txtCedula, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.cedula = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.cedula.SetMaxLength(0)
        self.cedula.Enable(False)

        fgSizer1.Add(self.cedula, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtAddress = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Dirección:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtAddress.Wrap(-1)
        fgSizer1.Add(self.txtAddress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.address = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(280, 20),
            wx.TE_LEFT,
        )
        self.address.SetMaxLength(0)
        self.address.Enable(False)

        fgSizer1.Add(self.address, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtMail = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Correo:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtMail.Wrap(-1)
        fgSizer1.Add(self.txtMail, 0, wx.ALL, 5)

        self.mail = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(280, 20),
            wx.TE_LEFT,
        )
        self.mail.SetMaxLength(0)
        self.mail.Enable(False)

        fgSizer1.Add(self.mail, 0, wx.ALL, 5)

        self.txtPhone = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Telefono:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtPhone.Wrap(-1)
        fgSizer1.Add(self.txtPhone, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.phone = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.phone.SetMaxLength(0)
        self.phone.Enable(False)

        fgSizer1.Add(self.phone, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtMobile = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Celular:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtMobile.Wrap(-1)
        fgSizer1.Add(self.txtMobile, 0, wx.ALL, 5)

        self.mobile = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.mobile.SetMaxLength(0)
        self.mobile.Enable(False)

        fgSizer1.Add(self.mobile, 0, wx.ALL, 5)

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

        self.txtActivate = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Activado:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtActivate.Wrap(-1)
        fgSizer1.Add(self.txtActivate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.activate = wx.CheckBox(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(15, 15),
            wx.ALIGN_RIGHT,
        )
        self.activate.Enable(False)

        fgSizer1.Add(self.activate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtEmployee = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Empleado",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtEmployee.Wrap(-1)
        fgSizer1.Add(self.txtEmployee, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.employee = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(180, 20),
            wx.TE_RIGHT,
        )
        self.employee.SetMaxLength(0)
        self.employee.Enable(False)

        fgSizer1.Add(self.employee, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

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
