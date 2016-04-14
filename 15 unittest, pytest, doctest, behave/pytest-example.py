import pytest
import behave

@pytest.fixture(scope="module")
def obj():
    class MathObject:
        def __init__(self):
            self.value = 5
    return MathObject()

def test_1(obj):
    obj.value += 1
    assert obj.value == 6

def test_2(obj):
    obj.value += 1
    assert obj.value == 7