import json
import csv
import requests
import config
import pandas as pd
import time
import io

# Get the balance_sheet data with an API key
def get_fundamental_data(symbol, func):
    # Add the API key to the config.py file before running the code below
    url = f'https://www.alphavantage.co/query?function={func}&symbol={symbol}&apikey={config.API_KEY}'
    print(url)
    r = requests.get(url)
    data = r.json()

    with open('../data/temp.json', 'w') as f:
        json.dump(data, f)

# Get data in .csv format and append to a file
def get_monthly_data_csv(symbol, func):
    # Add the API key to the config.py file before running the code below
    url = f'https://www.alphavantage.co/query?function={func}&symbol={symbol}&datatype=csv&apikey={config.API_KEY}'
    print(url)
    r = requests.get(url).content

    data = pd.read_csv(io.StringIO(r.decode('utf-8')), error_bad_lines=False, low_memory=False)

    data['Symbol'] = symbol
    data.to_csv("../data/monthly-data.csv", mode='a', index=False, header=False, sep=',', encoding="utf-8")    

# Use Pandas library json_normalize to write json data to a csv file
def write_to_csv(name):
    with open('../data/temp.json') as data_file:  
        data = json.load(data_file)

    df = pd.json_normalize(data, record_path=['quarterlyEarnings'], meta=['symbol'])
    df.to_csv(f"../data/{name}.csv", mode='a', index=False, header=False, sep=',', encoding="utf-8") # write to csv file

# Sort values in a .csv file
def sort_values():
    df = pd.read_csv('../data/nasdaq_screener_1637250291945.csv')
    df.sort_values(by=['Market Cap'], axis=0, ascending=[False], inplace=True, ignore_index=True)
    df2 = df.head(200)
    df2.to_csv('../data/nasdaq_screener_sorted_values.csv', index=False)

# Warning! This will deplete a lot of your API requests
# Loading data into csv file
def load_dataset():
    df = pd.read_csv('../data/nasdaq_screener_sorted_values.csv')
    count = 0
    # Set the limit of records 
    df_lim = df.head(200)
    for symbol in df_lim['Symbol']:
        
        # Get the monthly data
        # get_monthly_data_csv(symbol)

        # Get and convert the balance sheet
        get_fundamental_data(symbol, func='EARNINGS')
        write_to_csv(name='EARNINGS')
        count = count + 1
        print("{}{}".format('count = ', count))
        # Add a timout to prevent exceeding the API call limit (5 requests/min)
        time.sleep(15)


# Write json data to a csv file
def write_to_csv_func(symbol):
    # Opening JSON file and loading the data
    # into the variable data
    with open(f'../data/{symbol}.json') as json_file:
        data = json.load(json_file)
    
    # Retreive dictionary from json data
    qreps = data['quarterlyReports']
    
    # Open file for writing
    data_file = open(f'../data/{symbol}.csv', 'w', newline='')
    
    # create csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    count = 0

    header = {...}
    for rep in qreps:
        if count == 0:
            header = rep.keys()

            print('Headers of the file columns created:')
            print(header)
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(rep.values())

    # Close file
    data_file.close()

def write_to_csv_monthly():
    # Opening JSON file and loading the data
    # into the variable data
    with open(f'../data/temp.json') as json_file:
        data = json.load(json_file)
    
    # Retreive dictionary from json data
    dates = data['Monthly Time Series']
    company = data['Meta Data']['2. Symbol']
    # print('-------------------------------------------------------------------------------------------')
    # print(dates)
    # print('-------------------------------------------------------------------------------------------')
    # print(company)
    
    # Open file for writing
    data_file = open('../data/monthly-data.csv', 'w', newline='')
    
    # create csv writer object
    fieldnames = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    csv_writer = csv.DictWriter(data_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow(data)


    
    # Counter variable used for writing
    count = 0

    header = {...}
    for values in data.items():
        print(values)
        print('-----------------------------------------------------------------------')
        print(values[1])
        if count == True:
            header = values

            print('Headers of the file columns created:')
            print(header)
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerows(values[1])

    # Close file
    data_file.close()





