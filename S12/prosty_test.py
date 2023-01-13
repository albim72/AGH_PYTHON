import time

def compute(x):
    response = exp_api_cell()
    return response + x

def exp_api_cell():
    time.sleep(3)
    return 255

def test_compute():
    expected = 256
    actual = compute(1)
    assert expected==actual

test_compute()
