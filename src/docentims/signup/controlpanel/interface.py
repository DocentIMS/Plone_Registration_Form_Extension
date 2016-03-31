from zope import schema
from zope.interface import Interface
from docentims.signup import _

class ISettings(Interface):
    """ Define settings data structure """

    signup_groups = schema.List(
        title=_(u"Groups"),
        description=_(u"Groups which will be shown on the regitration form."),
        required=False,
        value_type=schema.Choice(
            vocabulary='docentims.signup.vocabularies.group_ids')
    )

    associated = schema.List(
        title=_(u"Associated with"),
        description=_(u"List of 'I Am Associated With' items"),
        value_type=schema.TextLine(),
        required=False,
    )

    signup_skills = schema.List(
        title=_(u"Skills"),
        description=_(u"List of 'Skills I can offer' items"),
        value_type=schema.TextLine(),
        required=False,
    )


