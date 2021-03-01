# -*- coding: utf-8 -*-


import wx
import wx.xrc


# Class EmployeeFrame


class EmployeeFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Empleado",
            pos=wx.DefaultPosition,
            size=wx.Size(420, 860),
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

        self.txtCedula = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Cédula:",
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
        fgSizer1.Add(self.cedula, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtName = wx.StaticText(
            self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
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

        self.txtlastname = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Apellido",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtlastname.Wrap(-1)
        fgSizer1.Add(self.txtlastname, 0, wx.ALL, 5)

        self.lastname = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(280, 20),
            wx.TE_LEFT,
        )
        self.lastname.SetMaxLength(0)
        self.lastname.Enable(False)

        fgSizer1.Add(self.lastname, 0, wx.ALL, 5)

        self.txtGender = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Género:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtGender.Wrap(-1)
        fgSizer1.Add(self.txtGender, 0, wx.ALL, 5)

        self.gender = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(20, 20),
            wx.TE_RIGHT,
        )
        self.gender.SetMaxLength(0)
        self.gender.Enable(False)

        fgSizer1.Add(self.gender, 0, wx.ALL, 5)

        self.txtNationality = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Nacionalidad:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtNationality.Wrap(-1)
        fgSizer1.Add(self.txtNationality, 0, wx.ALL, 5)

        self.nationality = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.TE_RIGHT,
        )
        self.nationality.SetMaxLength(0)
        self.nationality.Enable(False)

        fgSizer1.Add(self.nationality, 0, wx.ALL, 5)

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

        self.txtBirthdate = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Fecha Nac.:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtBirthdate.Wrap(-1)
        fgSizer1.Add(self.txtBirthdate, 0, wx.ALL, 5)

        self.birthdate = wx.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.Size(100, 20),
            wx.DP_DEFAULT,
        )
        self.birthdate.Enable(False)

        fgSizer1.Add(self.birthdate, 0, wx.ALL, 5)

        self.txtMarital = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Esdado Civil:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtMarital.Wrap(-1)
        fgSizer1.Add(self.txtMarital, 0, wx.ALL, 5)

        self.marital = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(20, 20),
            wx.TE_RIGHT,
        )
        self.marital.SetMaxLength(0)
        self.marital.Enable(False)

        fgSizer1.Add(self.marital, 0, wx.ALL, 5)

        self.txtSons = wx.StaticText(
            self, wx.ID_ANY, u"Hijos:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtSons.Wrap(-1)
        fgSizer1.Add(self.txtSons, 0, wx.ALL, 5)

        self.sons = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(20, 20),
            wx.TE_RIGHT,
        )
        self.sons.SetMaxLength(0)
        self.sons.Enable(False)

        fgSizer1.Add(self.sons, 0, wx.ALL, 5)

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

        self.txtSection = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Sección:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtSection.Wrap(-1)
        fgSizer1.Add(self.txtSection, 0, wx.ALL, 5)

        sectionChoices = []
        self.section = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(180, 20),
            sectionChoices,
            0,
        )
        self.section.Enable(False)

        fgSizer1.Add(self.section, 0, wx.ALL, 5)

        self.txtPosition = wx.StaticText(
            self, wx.ID_ANY, u"Cargo:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtPosition.Wrap(-1)
        fgSizer1.Add(self.txtPosition, 0, wx.ALL, 5)

        positionChoices = []
        self.position = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(180, 20),
            positionChoices,
            0,
        )
        self.position.Enable(False)

        fgSizer1.Add(self.position, 0, wx.ALL, 5)

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

        self.txtLogin = wx.StaticText(
            self, wx.ID_ANY, u"Login:", wx.DefaultPosition, wx.Size(80, 15), wx.ALIGN_LEFT
        )
        self.txtLogin.Wrap(-1)
        fgSizer1.Add(self.txtLogin, 0, wx.ALL, 5)

        self.Login = wx.CheckBox(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(15, 15),
            wx.ALIGN_RIGHT,
        )
        self.Login.Enable(False)

        fgSizer1.Add(self.Login, 0, wx.ALL, 5)

        self.txtPassword = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Contraseña:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtPassword.Wrap(-1)
        fgSizer1.Add(self.txtPassword, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.password = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(180, 20),
            wx.TE_PASSWORD,
        )
        self.password.SetMaxLength(0)
        self.password.Enable(False)

        fgSizer1.Add(self.password, 0, wx.ALL, 5)

        self.txtProfile = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Perfil:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtProfile.Wrap(-1)
        fgSizer1.Add(self.txtProfile, 0, wx.ALL, 5)

        profileChoices = []
        self.profile = wx.ComboBox(
            self,
            wx.ID_ANY,
            u"Combo!",
            wx.DefaultPosition,
            wx.Size(180, 20),
            profileChoices,
            0,
        )
        self.profile.Enable(False)

        fgSizer1.Add(self.profile, 0, wx.ALL, 5)

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

        self.txtEmployee = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Operador:",
            wx.DefaultPosition,
            wx.Size(80, 15),
            wx.ALIGN_LEFT,
        )
        self.txtEmployee.Wrap(-1)
        fgSizer1.Add(self.txtEmployee, 0, wx.ALL, 5)

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

        fgSizer1.Add(self.employee, 0, wx.ALL, 5)

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

    def on_closed(self, evt):
        self.Destroy()
        evt.Skip()

    def __del__(self):
        pass
