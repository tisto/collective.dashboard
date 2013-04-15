from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivedashboardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.dashboard
        xmlconfig.file(
            'configure.zcml',
            collective.dashboard,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.dashboard:default')

COLLECTIVE_DASHBOARD_FIXTURE = CollectivedashboardLayer()
COLLECTIVE_DASHBOARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DASHBOARD_FIXTURE,),
    name="CollectivedashboardLayer:Integration"
)
COLLECTIVE_DASHBOARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DASHBOARD_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivedashboardLayer:Functional"
)
