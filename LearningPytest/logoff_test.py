import pytest
@pytest.mark.sanity
def testLogin():
    print("Logged off successfully!")
@pytest.mark.skip
def testCalculation():
    assert 2 + 2 == 4

@pytest.mark.xfail
def testCalculationTwo():
    assert 2 + 2 == 9