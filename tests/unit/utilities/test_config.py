from hamcrest import assert_that, equal_to
from uitestcore.utilities.config_handler import parse_config_data


class MockContext:
    def __init__(self, maximize_browser=None, logging_flag=None):
        self.maximize_browser = maximize_browser
        self.logging_flag = logging_flag
        self.browser = ""


class MockConfig:
    def __init__(self, userdata=None):
        self.userdata = userdata


def test_parse_config_data_false_values():
    userdata = {
        "logging_flag": "false",
        "maximize_browser_flag": "false",
    }
    context = MockContext()
    context.config = MockConfig(userdata)

    parse_config_data(context)

    assert_that(context.logging_flag, equal_to(False), "Logging flag should be false")
    assert_that(context.maximize_browser, equal_to(False), "Maximize browser should be false")


def test_parse_config_data_true_values():
    userdata = {
        "logging_flag": "true",
        "maximize_browser_flag": "true",
    }
    context = MockContext()
    context.config = MockConfig(userdata)

    parse_config_data(context)

    assert_that(context.logging_flag, equal_to(True), "Logging flag should be true")
    assert_that(context.maximize_browser, equal_to(True), "Maximize browser should be true")


def test_parse_config_data_sets_browser_type():
    userdata = {
        "browser": "chrome"
    }
    context = MockContext()
    context.config = MockConfig(userdata)

    parse_config_data(context)

    assert_that(context.browser, equal_to("chrome"), "Expected browser type was not found")
