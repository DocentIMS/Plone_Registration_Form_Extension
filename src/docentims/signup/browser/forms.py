from z3c.form import button

from plone.app.users.browser.register import RegistrationForm
from Products.CMFCore.utils import getToolByName
from docentims.signup import _

from AccessControl import getSecurityManager
from Products.CMFCore.permissions import ManagePortal

from Products.statusmessages.interfaces import IStatusMessage
from zExceptions import Forbidden


class DocentimsRegistrationForm(RegistrationForm):

    @button.buttonAndHandler(
        _(u'label_register', default=u'Register'), name='register'
    )
    def action_join(self, action):

        data, errors = self.extractData()

        # extra password validation
        self.validate_registration(action, data)

        if action.form.widgets.errors:
            self.status = self.formErrorsMessage
            return

        self.handle_join_success(data)

        portal_groups = getToolByName(self.context, 'portal_groups')
        user_id = data['user_id']
        is_zope_manager = getSecurityManager().checkPermission(
            ManagePortal, self.context)

        try:
            # Add user to the selected group
            if 'signup_groups' in data.keys():
                groupname = data['signup_groups']
                group = portal_groups.getGroupById(groupname)
                if 'Manager' in group.getRoles() and not is_zope_manager:
                    raise Forbidden
                portal_groups.addPrincipalToGroup(user_id, groupname,
                                                  self.request)
        except (AttributeError, ValueError), err:
            IStatusMessage(self.request).addStatusMessage(err, type="error")
            return

        self._finishedRegister = True

        # XXX Return somewhere else, depending on what
        # handle_join_success returns?
        came_from = self.request.form.get('came_from')
        if came_from:
            utool = getToolByName(self.context, 'portal_url')
            if utool.isURLInPortal(came_from):
                self.request.response.redirect(came_from)
                return ''
