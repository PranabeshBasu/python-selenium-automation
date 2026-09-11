import pytest
def testLogin():
    print("Logged in successfully!")
@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4