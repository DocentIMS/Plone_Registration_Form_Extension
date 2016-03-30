from zope.interface import Interface

from zope import schema
from z3c.form import field
from zope.component import adapts

from plone.supermodel import model
from plone.z3cform.fieldsets import extensible
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.userdatapanel import UserDataPanel

from docentims.signup.interfaces import IDocentimsSignupLayer
from docentims.signup import _
from docentims.signup.browser.forms import DocentimsRegistrationForm


class IEnhancedUserDataSchema(model.Schema):
    associated = schema.Choice(
        title=_(u'docentims_signup_associated_title',
                default=u'Associated with'),
        description=_(u'', default=u""),
        required=False,
        vocabulary = 'docentims.signup.vocabularies.associated_with',
        )

    signup_groups = schema.Choice(
        title=_(u'docentims_signup_groups_title', default=u'I am'),
        description=_(u'', default=u""),
        required=False,
        vocabulary = 'docentims.signup.vocabularies.signup_groups',
        )


class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IDocentimsSignupLayer, UserDataPanel)
    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)


class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IDocentimsSignupLayer, DocentimsRegistrationForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)


class EnhancedUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IEnhancedUserDataSchema

