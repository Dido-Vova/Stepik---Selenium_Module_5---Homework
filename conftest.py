import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):

    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser: Chrome or Firefox")

    parser.addoption('--language', type=str, default='en-gb', action='store' f'')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    site_language = request.config.getoption("language")
    language_choices = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr',
                        'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk',
                        'zh-cn', 'en']
    browser = None
    if site_language in language_choices:
        if browser_name == "Chrome":
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == "Firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", site_language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    else:
        raise pytest.UsageError(f'Set the site language from the list: {language_choices}')
    yield browser
    print("\nquit browser..")
    # sleep(5)
    browser.quit()