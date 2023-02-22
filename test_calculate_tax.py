import pytest
from calculate_tax.calculate_tax import calculate_tax, calculate_ads, calculate_lbtt

# Scotland rates
# bands = [145000,250000,325000,750000]
# rates = [0.02, 0.05, 0.1, 0.12]

def test_calculate_ads():
    assert calculate_ads(15000, additional_dwelling = True) == 0

def test_calculate_ads_2():
    assert calculate_ads(40000, additional_dwelling = True) == 2400

def test_calculate_ads_3():
    assert calculate_ads(703000, additional_dwelling = True) == 42180



# No first time buyer relief, no ADS

def test_calculate_tax_band_0():
    assert calculate_tax(120000) == 0

def test_calculate_tax_band_1():
    assert calculate_tax(180000) == 700

def test_calculate_tax_band_2():
    assert calculate_tax(312000) == 5200

def test_calculate_tax_band_3():
    assert calculate_tax(703000) == 43650

def test_calculate_tax_band_4():
    assert calculate_tax(1500000) == 138350



# ADS, no first time buyer relief

def test_calculate_tax_band_0_ads():
    assert calculate_tax(120000, additional_dwelling = True) == 7200

def test_calculate_tax_band_1_ads():
    assert calculate_tax(312000, additional_dwelling = True) == 23920

def test_calculate_tax_band_2_ads():
    assert calculate_tax(703000, additional_dwelling = True) == 85830

def test_calculate_tax_band_3_ads():
    assert calculate_tax(1500000, additional_dwelling = True) == 228350



# First time buyer

def test_calculate_tax_first_time_band_0():
    assert calculate_tax(175000, first_time_buyer = True, additional_dwelling = False) == 0

def test_calculate_tax_first_time_band_2():
    assert calculate_tax(312000, first_time_buyer = True, additional_dwelling = False) == 4600

def test_calculate_tax_first_time_band_3():
    assert calculate_tax(800000, first_time_buyer = True, additional_dwelling = False) == 53750