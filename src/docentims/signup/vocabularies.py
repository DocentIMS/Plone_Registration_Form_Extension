from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary

from AccessControl import getSecurityManager
from Products.CMFCore.permissions import ManagePortal
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import normalizeString
from Products.CMFPlone.utils import safe_unicode
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.site.hooks import getSite

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from docentims.signup.controlpanel.interface import ISettings

NO_GROUPS = ['Managers', 'Site Administrators']


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
                    if val.replace(' ', ''):
                        terms.append(
                            SimpleVocabulary.createTerm(
                                val, val.encode('utf-8'), val))
        return SimpleVocabulary(terms)

GetAssociated = Associated()


class GroupIds(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        site = getSite()
        groups_tool = getToolByName(site, 'portal_groups')
        is_zope_manager = getSecurityManager().checkPermission(
            ManagePortal, context)
        groups = groups_tool.listGroups()

        # Get group id, title tuples for each, omitting virtual group
        # 'AuthenticatedUsers' and NO_GROUPS
        terms = []
        for g in groups:
            if g.id == 'AuthenticatedUsers':
                continue
            if 'Manager' in g.getRoles() and not is_zope_manager:
                continue

            if g.id in NO_GROUPS:
                continue

            group_title = safe_unicode(g.getGroupTitleOrName())
            if group_title != g.id:
                title = u'%s (%s)' % (group_title, g.id)
            else:
                title = group_title
            terms.append(SimpleTerm(g.id, g.id, title))

        # Sort by title
        terms.sort(key=lambda x: normalizeString(x.title))
        return SimpleVocabulary(terms)

GetGroupIds = GroupIds()


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


class SignUpSkills(object):

    implements(IVocabularyFactory)

    def __call__(self, context=None):
        registry = queryUtility(IRegistry)
        terms = []

        if registry is not None:
            settings = registry.forInterface(ISettings)
            lst = settings.signup_skills
            if lst:
                for val in sorted(list(set(lst))):
                    if val.replace(' ', ''):
                        terms.append(
                            SimpleVocabulary.createTerm(
                                val, val.encode('utf-8'), val))
        return SimpleVocabulary(terms)

GetSignUpSkills = SignUpSkills()
