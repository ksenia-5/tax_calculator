import pytest
from calculate_tax.calculate_tax import calculate_tax

# Scotland rates
bands = [145000,250000,325000,750000]
rates = [0.02, 0.05, 0.1, 0.12]

def test_lbtt_band_1():
    assert calculate_tax(120000, bands, rates) == (0, 0)

def test_lbtt_band_2():
    assert calculate_tax(209000, bands, rates) == (1280, 0)

def test_lbtt_band_3():
    assert calculate_tax(300000, bands, rates) == (4600, 0)

def test_lbtt_band_4():
    assert calculate_tax(686000, bands, rates) == (41950, 0)

def test_lbtt_band_5():
    assert calculate_tax(3700000, bands, rates) == (402350, 0)


# England rates
# bands = [250000, 925000,1500000]
# rates = [0.05, 0.1, 0.12]
# first_time_relief = 425000

