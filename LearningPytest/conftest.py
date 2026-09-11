import pytest

@pytest.fixture(autouse=True) #Default scope is function /scope = "session"/ scope = "function"
def setUp(browser):
    if browser == "chrome":
        print("Chrome opened")
    elif browser == "firefox":
        print("firefox opened")
    print("Open the browser")

    yield

    print("Close the browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse= True)
def browser(request):
    return request.config.getoption("--browser")