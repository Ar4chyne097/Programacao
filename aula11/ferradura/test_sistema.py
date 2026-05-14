from functions import sistema

def test_Windows():
    assert sistema("nt") == "Windows"
    assert sistema("posix") == "Linux"

def test_ERRO():
    assert sistema("bdjkasdjsb") == "ERRO! Intentálo otra vez"