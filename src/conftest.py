@pytest.fixture
def driver(auth, download_dir):
    # Initialize ChromeDriver
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument("--window-size=1920, 1080")
    chrome_options.add_argument('--headless')
    prefs = {'download.default_directory': download_dir}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = Chrome(options=chrome_options)
    # add auth session to drivers attrs
    driver.auth_session = auth
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()
