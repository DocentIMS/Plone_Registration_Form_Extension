# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

DEFAULT_PROFILE = 'profile-docentims.signup:default'

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'docentims.signup:uninstall',
        ]

def post_install(context):
    """Post install script"""
    if context.readDataFile('docentimssignup_default.txt') is None:
        return

def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('docentimssignup_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
