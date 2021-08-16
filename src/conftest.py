@pytest.fixture
def driver():
    # Initialize ChromeDriver
    driver = Driver()
    yield driver
    # For cleanup, quit the driver
    driver.quit()
