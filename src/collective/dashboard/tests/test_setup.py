import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.dashboard.testing import \
    COLLECTIVE_DASHBOARD_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_DASHBOARD_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.dashboard'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_browserlayer_available(self):
        from plone.browserlayer import utils
        from collective.dashboard.interfaces import \
            ICollectiveDashboardLayer
        self.assertTrue(
            ICollectiveDashboardLayer in utils.registered_layers()
        )

    def test_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertTrue(
            '++resource++collective.dashboard.stylesheets/jquery.gridster.css' in stylesheets_ids
        )

    def test_js_registered(self):
        jsreg = getattr(self.portal, 'portal_javascripts')
        script_ids = jsreg.getResourceIds()
        self.assertTrue(
            '++resource++collective.dashboard.javascripts/jquery.collision.js'
            in script_ids
        )
        self.assertTrue(
            '++resource++collective.dashboard.javascripts/jquery.coords.js'
            in script_ids
        )
        self.assertTrue(
            '++resource++collective.dashboard.javascripts/jquery.draggable.js'
            in script_ids
        )
        self.assertTrue(
            '++resource++collective.dashboard.javascripts/jquery.gridster.extras.js'
            in script_ids
        )
        self.assertTrue(
            '++resource++collective.dashboard.javascripts/jquery.gridster.js'
            in script_ids
        )
