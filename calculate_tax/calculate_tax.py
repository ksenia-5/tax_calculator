'''
The main difference here is that information on bands, rates, 
first time buyer relief, and additional dwelling supplement 
is passed as arguments to the function.

The function can process a different number of bands, looping through bands
to calculate tax payble at different rates for each band.
'''

residential_band_rates = {
    'bands' : [145000,250000,325000,750000],
    'rates' : [0.02, 0.05, 0.1, 0.12],
    'first_time_relief' : 175000,
    }

non_residential_band_rates = {
    'bands' : [15000,250000],
    'rates' : [0.0, 0.05],
    'first_time_relief' : 175000,
    'ads_band' : {'threshold' : 40000, 'rate' : 0.06}
    }


ads_band_rate = {
    'threshold' : 40000, 'rate' : 0.06
    }


def calculate_lbtt(price, first_time_buyer = False, band_rates = residential_band_rates):

    '''
    Function calculates LBTT payable and the additional dwelling supplement (ADS), 
    if  the buyer will have two homes at the end of the transaction.

    If the buyer is a first time buyer, first time buyer relief raises the tax free threshold to 175000, 
    reducing tax by up to £600
    '''

    # Unpack tax rate data
    bands = band_rates['bands']
    rates = band_rates['rates']
    first_time_relief = band_rates['first_time_relief']

    if first_time_buyer:
        bands[0] = first_time_relief
    
    tax = 0

    for i in range(len(bands) - 1):
        lower_edge = bands[i]
        upper_edge = bands[i + 1]
        if price > lower_edge:
            taxable = min([price, upper_edge]) - lower_edge
            tax += taxable * rates[i]
    
    # if purchase price is in the top band, apply top band rate to the amount above band boundary
    if price > bands[-1]:
        tax += (price - bands[-1] ) * rates[-1]
        
    return tax




def calculate_ads(price, additional_dwelling = False, ads_band = ads_band_rate):
    
    '''
    Function calculates additional dwelling supplement (ADS)
    takes user values purchase price :int and additional_dwelling :bool,
    tax authority data tax-free threshold :int and rate :float,
    returns ads_payble :float 
    '''

    ads_payable = 0

    if additional_dwelling and price >= ads_band['threshold']:
        ads_payable = price * ads_band['rate']
    
    return ads_payable



def calculate_tax(price, first_time_buyer = False, additional_dwelling = False, band_rates = residential_band_rates, ads_rate = ads_band_rate):
    '''
    Function calculates total tax due on residential property purchase.
    Takes user data - price :int, first_time_buyer and additional_dwelling :bool
    and tax authority data ads_threshold :int and ads_rate :float,
    prints summary and returns total tax due.
    '''
    
    lbtt_payable = calculate_lbtt(price, first_time_buyer, band_rates)
    ads_payable = calculate_ads(price, additional_dwelling, ads_rate)
    
    total_tax = lbtt_payable + ads_payable
    
    print(f"LBTT due: {lbtt_payable}, ADS due: {ads_payable}... Total tax payable = £{total_tax}")
    
    return total_tax
