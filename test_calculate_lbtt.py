import pytest
from calculate_tax.calculate_lbtt import calculate_residential_tax, calculate_lbtt_1, calculate_ads_1

def test_lbtt_band_1():
    assert calculate_residential_tax(120000) == 0

def test_lbtt_band_2():
    assert calculate_residential_tax(209000) == 1280

def test_lbtt_band_3():
    assert calculate_residential_tax(300000) == 4600

def test_lbtt_band_4():
    assert calculate_residential_tax(686000) == 41950   

def test_lbtt_band_5():
    assert calculate_residential_tax(3700000) == 402350
