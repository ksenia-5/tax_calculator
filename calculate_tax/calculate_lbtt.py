def calculate_ads_1(price, additional_dwelling = False, threshold = 40000, rate = 0.06):
    
    '''
    Function calculates additional dwelling supplement (ADS)
    takes user values purchase price :int and additional_dwelling :bool,
    tax authority data tax-free threshold :int and rate :float,
    returns ads_payble :float 
    '''

    ads_payable = 0

    if additional_dwelling and price >= threshold:
        ads_payble = price*rate
    
    return ads_payable



def calculate_lbtt_1(price, first_time_buyer = False):
    '''
    Function calculates LBTT payable
    takes user values purchase price :int and first_time_buyer :bool,
    tax authority data bands list of :int and rates list of :float,

    First time buyer relief raises the tax free threshold to 175000, 
    reducing tax by up to £600
    '''
    
    band_0 = 145000 # tax free allowance
    band_1 = 250000
    band_2 = 325000
    band_3 = 750000

    tax = 0
    
    if first_time_buyer:
        band_0 = 175000

    match price:

        case num if band_0 < num <= band_1:
            tax += 0.02 * (price - band_0)

        case num if band_1 < num <= band_2:
            tax += 0.02 * (band_1 - band_0)
            tax += 0.05 * (price - band_1)

        case num if band_2 < num <= band_3:
            tax += 0.02*(band_1 - band_0)
            tax += 0.05*(band_2 - band_1)
            tax += 0.10*(price - band_2)

        case num if num > band_3:
            tax += 0.02 * (band_1 - band_0)
            tax += 0.05 * (band_2 - band_1)
            tax += 0.10 * (band_3 - band_2)
            tax += 0.12 * (price - band_3)
        
    # return tax
    return tax


def calculate_residential_tax(price, first_time_buyer = False, additional_dwelling = False, ads_threshold = 40000, ads_rate = 0.06):
    '''
    Function calculates total tax due on residential property purchase.
    Takes user data - price :int, first_time_buyer and additional_dwelling :bool
    and tax authority data ads_threshold :int and ads_rate :float,
    prints summary and returns total tax due.
    '''
    
    lbtt_payable = calculate_lbtt_1(price, first_time_buyer)
    ads_payable = calculate_ads_1(price, additional_dwelling, ads_threshold, ads_rate)
    
    total = lbtt_payable + ads_payable
    
    print(f"LBTT due: {lbtt_payable}, ADS due: {ads_payable}... Total tax payable = £{total}")
    
    return total
