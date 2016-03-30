from zope import schema
from zope.interface import Interface
from docentims.signup import _

class ISettings(Interface):
    """ Define settings data structure """

    signup_groups = schema.List(
        title=_(u"Groups"),
        description=_(u"Groups which will be shown on the regitration form."),
        required=False,
        value_type=schema.Choice(vocabulary='plone.app.users.group_ids')
    )

    associated = schema.List(
        title=_(u"Associated with"),
        description=_(u"List of 'associatedwith' items"),
        value_type=schema.TextLine(),
        required=False,
    )

