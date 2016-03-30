from zope.schema.vocabulary import SimpleVocabulary

from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
# from newihoppers.content import MessageFactory as _

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from docentims.signup.controlpanel.interface import ISettings


class Associated(object):

    implements(IVocabularyFactory)

    def __call__(self, context=None):
        registry = queryUtility(IRegistry)
        terms = []

        if registry is not None:
            settings = registry.forInterface(ISettings)
            lst = settings.associated
            if lst:
                for val in sorted(list(set(lst))):
                    terms.append(
                        SimpleVocabulary.createTerm(
                            val, val.encode('utf-8'), val))
        return SimpleVocabulary(terms)

GetAssociated = Associated()

class SignUpGroups(object):

    implements(IVocabularyFactory)

    def __call__(self, context=None):
        registry = queryUtility(IRegistry)
        terms = []

        if registry is not None:
            settings = registry.forInterface(ISettings)
            lst = settings.signup_groups
            if lst:
                for val in sorted(list(set(lst))):
                    terms.append(
                        SimpleVocabulary.createTerm(
                            val, val.encode('utf-8'), val))
        return SimpleVocabulary(terms)

GetSignUpGroups = SignUpGroups()


