import os
from dotenv import load_dotenv
import requests 

load_dotenv()
cle = os.getenv("ALPHA_VANTAGE_KEY")

# IMPORT RATES ------------------------------------------------------------------------------------------
try: 
    response = requests.get("https://api.frankfurter.dev/v1/latest?from=EUR&to=CHF,USD,GBP,JPY,HKD")
    data_rates = response.json()

except requests.exceptions.RequestException:
    print('\n=== Converter not available ===\n')
    exit()

# API MARKET ------------------------------------------------------------------------------------------
try:
    url_lvmh = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MC.PA&apikey={cle}"
    url_kering = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=KER.PA&apikey={cle}"
    response_lvmh_market= requests.get(url_lvmh)
    response_ker_market = requests.get(url_kering)
    data_lvmh = response_lvmh_market.json()
    data_ker = response_ker_market.json()

except requests.exceptions.RequestException:
    print('\n=== Market datas not available ===\n')
    exit()

# if server available, run converter
if response.status_code == 200:

    print('\n================================')
    print('Share prices today:')

    if "Global Quote" not in data_lvmh or "Global Quote" not in data_ker:
        print("\nMarket datas not available (quota reached or unknown symbol)\n")
    else:
        # extract LVMH market value from data
        lvmh_symbol = data_lvmh["Global Quote"]
        lvmh_today_price = lvmh_symbol["05. price"]
        float_lvmh_price = float(lvmh_today_price)
        print(f'\tLVMH : {float_lvmh_price:.2f} EUR')

        # extract LVMH market value from data
        ker_symbol = data_ker["Global Quote"]
        ker_today_price = ker_symbol["05. price"]
        float_ker_price = float(ker_today_price)
        print(f'\tKER : {float_ker_price:.2f} EUR')


    # extract rates from dictionary data_rates extract form api.frakfurter
    rates = data_rates['rates']
    rates['EUR'] = 1
    date = data_rates['date']

    # create a function to convert amount with associate rate of choosen currency
    def convert(amount, currency, rates):
        '''Create a function to calculate a watch price between EUR, CHF, GBP, USD, JPY and HKD'''
        rate = rates[currency]
        return amount * rate

    chf = rates['CHF']
    gbp = rates['GBP']
    usd = rates['USD']
    jpy = rates['JPY']
    hkd = rates['HKD']
    
    print('================================')
    print(f'Today ({date}) rates are:')
    print(f'\t1 EUR : {chf:.3f} CHF \n\t1 EUR : {gbp:.3f} GBP \n\t1 EUR : {usd:.3f} USD')
    print(f'\t1 EUR : {jpy:.3f} JPY \n\t1 EUR : {hkd:.3f} HKD')
    print('================================')

    prompt = 'Please insert watch price: '
    prompt2 = 'What currency was used to pay for the watch (currency supported EUR, CHF, GBP, USD, JPY and HKD): '
    prompt3 = 'Want to convert in which currency: '


    while True: 
        price = input(prompt)
        # To be able to quit at every questions 
        if price == 'quit':
            break

        try:
            price = float(price)    
        except ValueError:
            print('\n--- Please enter a valid value ---\n')
            continue
        
        if price > 0:
            # Add currency of the payment
            pay_currency = input(prompt2)
            pay_currency = pay_currency.upper()
            # To be able to quit at every questions
            if pay_currency == 'QUIT':
                break
            


            elif pay_currency in rates.keys():
                # find pay_currency rate and transforme price paid in EUR 
                rate_pay = rates[pay_currency]
                price_in_eur = price / rate_pay

                # Choose currency for the output
                currency2 = input(prompt3) 
                currency2 = currency2.upper()
                # To be able to quit at every questions
                if currency2 == 'QUIT':
                    break
                
                elif currency2 in rates.keys():
                    print(f'\n---------- {price:.2f} {pay_currency} ----------')
                    convert_price = convert(price_in_eur, currency2, rates)
                    print(f'  Watch price: {convert_price:.2f} {currency2}')
                    print('---------------------------------')
                else:
                    print('\n--- Currency not supported ---\n')

            else: 
                print('\n--- Currency not supported ---\n')

        else:
            print('\n--- Please enter a valid value ---\n')
            continue

elif response.status_code != 200:
    print('\n=== Server error ===\n')







