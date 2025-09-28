import pytest 
from calculator import add

@pytest.mark.parametrize("a,b,expected",[
    (1,2,3),
    (-1,2,1),
    (100,200,300),
    (-5,10,5)
])
def test_add_param(a,b,expected):
    assert add(a,b) == expected