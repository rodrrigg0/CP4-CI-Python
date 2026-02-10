from es_primo import es_primo

def test_2_es_primo():
    assert es_primo(2) is True

def test_4_no_es_primo():
    assert es_primo(4) is False

def test_9_no_es_primo():
    assert es_primo(9) is False

def test_13_es_primo():
    assert es_primo(13) is True

def test_menores_que_2_no_son_primos():
    assert es_primo(0) is False
    assert es_primo(1) is False
    assert es_primo(-5) is False
