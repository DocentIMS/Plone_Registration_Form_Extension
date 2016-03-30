# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import docentims.signup


class DocentimsSignupLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=docentims.signup)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'docentims.signup:default')


DOCENTIMS_SIGNUP_FIXTURE = DocentimsSignupLayer()


DOCENTIMS_SIGNUP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DOCENTIMS_SIGNUP_FIXTURE,),
    name='DocentimsSignupLayer:IntegrationTesting'
)


DOCENTIMS_SIGNUP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DOCENTIMS_SIGNUP_FIXTURE,),
    name='DocentimsSignupLayer:FunctionalTesting'
)


DOCENTIMS_SIGNUP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DOCENTIMS_SIGNUP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DocentimsSignupLayer:AcceptanceTesting'
)
