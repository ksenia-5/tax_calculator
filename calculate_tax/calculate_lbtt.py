def calculate_lbtt(price, first_time_buyer = False, additional_dwelling = False):
    '''
    Function calculates LBTT payable and the additional dwelling supplement (ADS), 
    if  the buyer will have two homes at the end of the transaction.

    If the buyer is a first time buyer, first time buyer relief raises the tax free threshold to 175000, 
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

    # if buying a second home, additional dwelling supplement (ADS) applies 
    ads_payable = 0
    ads_threshold = 40000
    ads_tax_rate = 0.06 
    if additional_dwelling:
        if price >= ads_threshold:
            ads_payable = price * ads_tax_rate
        
    # return (tax, ads_payable, tax+ads_payable)
    return (tax, ads_payable)

# tax_sub, ads_sub, total = calculate_tax(225000, first_time_buyer = False, additional_dwelling = True)
# print("LBTT: {:.2f}, ADS: {:.2f}, Total: {:.2f}".format(*calculate_lbtt(225000, first_time_buyer = False, additional_dwelling = True)))