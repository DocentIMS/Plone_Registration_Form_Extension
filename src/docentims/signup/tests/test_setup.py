# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from docentims.signup.testing import DOCENTIMS_SIGNUP_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that docentims.signup is properly installed."""

    layer = DOCENTIMS_SIGNUP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if docentims.signup is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'docentims.signup'))

    def test_browserlayer(self):
        """Test that IDocentimsSignupLayer is registered."""
        from docentims.signup.interfaces import (
            IDocentimsSignupLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocentimsSignupLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DOCENTIMS_SIGNUP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['docentims.signup'])

    def test_product_uninstalled(self):
        """Test if docentims.signup is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'docentims.signup'))

    def test_browserlayer_removed(self):
        """Test that IDocentimsSignupLayer is removed."""
        from docentims.signup.interfaces import IDocentimsSignupLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocentimsSignupLayer, utils.registered_layers())
