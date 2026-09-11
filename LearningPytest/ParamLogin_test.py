import pytest

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)

@pytest.mark.parametrize("a, b, final", [(2, 7, 9), (2, 2, 4), (3, 4, 9)])
def testAdd(a, b, final):
    assert a + b == final
    