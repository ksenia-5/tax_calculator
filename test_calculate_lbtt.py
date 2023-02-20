import pytest
from calculate_tax.calculate_lbtt import calculate_lbtt

def test_lbtt_band_1():
    assert calculate_lbtt(120000) == (0, 0)

def test_lbtt_band_2():
    assert calculate_lbtt(209000) == (1280, 0)

def test_lbtt_band_3():
    assert calculate_lbtt(300000) == (4600, 0)

def test_lbtt_band_4():
    assert calculate_lbtt(686000) == (41950, 0)    

def test_lbtt_band_5():
    assert calculate_lbtt(3700000) == (402350, 0)
