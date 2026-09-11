import pytest

@pytest.fixture(autouse=True) #Default scope is function /scope = "session"/ scope = "function"
def setUp():
    print("Open the browser")

    yield

    print("Close the browser")