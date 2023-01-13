import pytest

@pytest.mark.parametrize("n",[2,4,6])
def test_even_number(n):
    assert not n%2, f"{n} nie jest liczbą parzystą"
    
@pytest.mark.parametrize(["n","expected_output"],[(1,3),(2,6)])
def test_cube(n,expected_output):
    assert n*3 == expected_output, "zły wynik mnożenia przez 3"
    
test_even_number(12)
test_cube(3,9)

@pytest.fixture
def input_dict():
    return {"mwar":101,"ma":5}

def test_fixture(input_dict):
    assert input_dict["ma"] == 5, f"błąd słownika: {input_dict}"
    
test_fixture({"mwar":101,"ma":5})
