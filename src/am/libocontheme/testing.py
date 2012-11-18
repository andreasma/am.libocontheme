from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import am.libocontheme


AM_LIBOCONTHEME = PloneWithPackageLayer(
    zcml_package=am.libocontheme,
    zcml_filename='testing.zcml',
    gs_profile_id='am.libocontheme:testing',
    name="AM_LIBOCONTHEME")

AM_LIBOCONTHEME_INTEGRATION = IntegrationTesting(
    bases=(AM_LIBOCONTHEME, ),
    name="AM_LIBOCONTHEME_INTEGRATION")

AM_LIBOCONTHEME_FUNCTIONAL = FunctionalTesting(
    bases=(AM_LIBOCONTHEME, ),
    name="AM_LIBOCONTHEME_FUNCTIONAL")
