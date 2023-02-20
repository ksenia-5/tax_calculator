'''
The main difference here is that information on bands, rates, 
first time buyer relief, and additional dwelling supplement 
is passed as arguments to the function.

The function can process a different number of bands, looping through bands
to calculate tax payble at different rates for each band.
'''

def calculate_tax(price, bands, rates, first_time_relief = 175000, first_time_buyer = False,  additional_dwelling = False, ads_band = [40000, 0.06]):
    '''
    Function calculates LBTT payable and the additional dwelling supplement (ADS), 
    if  the buyer will have two homes at the end of the transaction.

    If the buyer is a first time buyer, first time buyer relief raises the tax free threshold to 175000, 
    reducing tax by up to £600
    '''
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

    # if buying a second home, additional dwelling supplement (ADS) applies 
    ads= 0

    if additional_dwelling:
        if price >= ads_band[0]:
            ads = price * ads_band[1]
        
    return (tax, ads)
