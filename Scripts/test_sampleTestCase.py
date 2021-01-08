from Resources import capabilities
from ApplicationFeature import google
import pytest
import Framework.WebDriverMethods
import Framework.CommonFunctions

com = Framework.CommonFunctions.Common()
brow = com.readJSONConfig()

@pytest.mark.parametrize("details", brow['browsers'])
def test_validateSettings(details):
    driver = capabilities.setup(details)
    ss = google.Settings(driver)
    ss.googleFeature()
    res = Framework.WebDriverMethods.WebDM(driver)
    res.quit_driver()