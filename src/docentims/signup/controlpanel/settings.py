from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from docentims.signup.controlpanel.interface import ISettings
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from docentims.signup import _

class SettingsEditForm(RegistryEditForm):

    schema = ISettings
    label = _(u"Docent IMS Site Registration Settings")

    def updateFields(self):
        super(SettingsEditForm, self).updateFields()
        self.fields['signup_groups'].widgetFactory = CheckBoxFieldWidget

    def updateWidgets(self):
        super(SettingsEditForm, self).updateWidgets()



class SettingsControlPanel(ControlPanelFormWrapper):
    form = SettingsEditForm


