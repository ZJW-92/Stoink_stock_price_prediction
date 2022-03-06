from django.shortcuts import render
import pandas as pd
from tensorflow.keras.models import load_model
from .models import AiModel, DataSet


# Not working
def train(request):
   return render(request, "admin/base.html")


# Not working
def eval(request):
   return render(request, "admin/base.html")


def stock(request):
   return render(request, 'front/stock.html')


def manualPredict(request):
   if request.method == 'GET':
      # Get all the values from input form
      var1 = (float(request.GET['Inputone']))
      var2 = (float(request.GET['Inputtwo']))
      var3 = (float(request.GET['Inputthree']))
      var4 = (float(request.GET['Inputfour']))
      var5 = (float(request.GET['Inputfive']))
      # coverting data into dataframe (from dict)
      df = pd.DataFrame({'1': var1, '2': var2, '3': var3, '4': var4, '5': var5}, index=[0])

      # Load the model and predicting
      temp = AiModel.objects.get(deployed=True)
      model = load_model(temp.get_titleversion() + ".h5")

      # make prediction
      prediction = str(model.predict(df))
      prediction_in_percentage = float(prediction[2:12]) * 100
   else:
      prediction_in_percentage = "error something wrong with posting the data"
   return render(request, 'front/stock.html', {'prediction': '%.4f%%'% prediction_in_percentage})


def predict(request):
   if request.method == 'POST':
      stock_value = request.POST['stock_title']
      if (stock_value == 'AAPL'):
         stock_name = "Apple Inc. Common Stock"
      elif (stock_value == 'MSFT'):
         stock_name = "Microsoft Corporation Common Stock"
      elif (stock_value == 'GOOG'):
         stock_name = "Alphabet Inc. Class C Capital Stock"
      elif (stock_value == 'GOOGL'):
         stock_name = "Alphabet Inc. Class A Common Stock"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'HD'):
         stock_name = "Home Depot Inc. (The) Common Stock"
      elif (stock_value == 'ADI'):
         stock_name = "Analog Devices Inc. Common Stock"
      elif (stock_value == 'BAC'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'WMT'):
         stock_name = "Walmart Inc. Common Stock"
      elif (stock_value == 'BABA'):
         stock_name = "Alibaba Group Holding Limited American Depositary Shares each representing eight Ordinary share"
      elif (stock_value == 'ASML'):
         stock_name = "ASML Holding N.V. New York Registry Shares"
      elif (stock_value == 'PG'):
         stock_name = "Procter & Gamble Company (The) Common Stock"
      elif (stock_value == 'MA'):
         stock_name = "Mastercard Incorporated Common Stock"
      elif (stock_value == 'ADBE'):
         stock_name = "Adobe Inc. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'AMZN'):
         stock_name = "Amazon.com Inc. Common Stock"
      elif (stock_value == 'TSLA'):
         stock_name = "Tesla Inc. Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'TSM'):
         stock_name = "Taiwan Semiconductor Manufacturing Company Ltd."
      elif (stock_value == 'JPM'):
         stock_name = "JP Morgan Chase & Co. Common Stock"
      elif (stock_value == 'V'):
         stock_name = "Visa Inc."
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'HD'):
         stock_name = "Home Depot Inc. (The) Common Stock"
      elif (stock_value == 'ADI'):
         stock_name = "Analog Devices Inc. Common Stock"
      elif (stock_value == 'BAC'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'WMT'):
         stock_name = "Walmart Inc. Common Stock"
      elif (stock_value == 'BABA'):
         stock_name = "Alibaba Group Holding Limited American Depositary Shares each representing eight Ordinary share"
      elif (stock_value == 'ASML'):
         stock_name = "ASML Holding N.V. New York Registry Shares"
      elif (stock_value == 'PG'):
         stock_name = "Procter & Gamble Company (The) Common Stock"
      elif (stock_value == 'MA'):
         stock_name = "Mastercard Incorporated Common Stock"
      elif (stock_value == 'ADBE'):
         stock_name = "Adobe Inc. Common Stock"
      elif (stock_value == 'NFLX'):
         stock_name = "Netflix Inc. Common Stock"
      elif (stock_value == 'NTES'):
         stock_name = "NetEase Inc. American Depositary Shares"
      elif (stock_value == 'CRM'):
         stock_name = "Salesforce.com Inc Common Stock"
      elif (stock_value == 'PFE'):
         stock_name = "Pfizer Inc. Common Stock"
      elif (stock_value == 'DIS'):
         stock_name = "Walt Disney Company (The) Common Stock"
      elif (stock_value == 'FB'):
         stock_name = "Meta Platforms Inc. Class A Common Stock"
      elif (stock_value == 'NVDA'):
         stock_name = "NVIDIA Corporation Common Stock"
      elif (stock_value == 'NKE'):
         stock_name = "Nike Inc. Common Stock"
      elif (stock_value == 'XOM'):
         stock_name = "Exxon Mobil Corporation Common Stock"
      elif (stock_value == 'NVO'):
         stock_name = "Novo Nordisk A/S Common Stock"
      elif (stock_value == 'JNJ'):
         stock_name = "Johnson & Johnson Common Stock"
      elif (stock_value == 'UNH'):
         stock_name = "UnitedHealth Group Incorporated Common Stock (DE)"
      elif (stock_value == 'ORCL'):
         stock_name = "Oracle Corporation Common Stock"
      elif (stock_value == 'TM'):
         stock_name = "Toyota Motor Corporation Common Stock"
      elif (stock_value == 'TMO'):
         stock_name = "Thermo Fisher Scientific Inc Common Stock"
      elif (stock_value == 'LLY'):
         stock_name = "Eli Lilly and Company Common Stock"
      elif (stock_value == 'CMCSA'):
         stock_name = "Comcast Corporation Class A Common Stock"
      elif (stock_value == 'KO'):
         stock_name = "Coca-Cola Company (The) Common Stock"
      elif (stock_value == 'PYPL'):
         stock_name = "PayPal Holdings Inc. Common Stock"
      elif (stock_value == 'AVGO'):
         stock_name = "Broadcom Inc. Common Stock"
      elif (stock_value == 'ACN'):
         stock_name = "Accenture plc Class A Ordinary Shares (Ireland)"
      elif (stock_value == 'COST'):
         stock_name = "Costco Wholesale Corporation Common Stock"
      elif (stock_value == 'ABT'):
         stock_name = "Abbott Laboratories Common Stock"
      elif (stock_value == 'PEP'):
         stock_name = "PepsiCo Inc. Common Stock"
      elif (stock_value == 'DHR'):
         stock_name = "Danaher Corporation Common Stock"
      elif (stock_value == 'CVX'):
         stock_name = "Chevron Corporation Common Stock"
      elif (stock_value == 'CSCO'):
         stock_name = "Cisco Systems Inc. Common Stock (DE)"
      elif (stock_value == 'VZ'):
         stock_name = "Verizon Communications Inc. Common Stock"
      elif (stock_value == 'MRK'):
         stock_name = "Merck & Company Inc. Common Stock (new)"
      elif (stock_value == 'ABBV'):
         stock_name = "AbbVie Inc. Common Stock"
      elif (stock_value == 'SHOP'):
         stock_name = "Shopify Inc. Class A Subordinate Voting Shares"
      elif (stock_value == 'QCOM'):
         stock_name = "QUALCOMM Incorporated Common Stock"
      elif (stock_value == 'INTC'):
         stock_name = "Intel Corporation Common Stock"
      elif (stock_value == 'WFC'):
         stock_name = "Wells Fargo & Company Common Stock"
      elif (stock_value == 'MCD'):
         stock_name = "McDonald's Corporation Common Stock"
      elif (stock_value == 'AMD'):
         stock_name = "Advanced Micro Devices Inc. Common Stock"
      elif (stock_value == 'NVS'):
         stock_name = "Novartis AG Common Stock"
      elif (stock_value == 'UPS'):
         stock_name = "United Parcel Service Inc. Common Stock"
      elif (stock_value == 'INTU'):
         stock_name = "Intuit Inc. Common Stock"
      elif (stock_value == 'TXN'):
         stock_name = "AstraZeneca PLC American Depositary Shares"
      elif (stock_value == 'T'):
         stock_name = "AT&T Inc."
      elif (stock_value == 'SE'):
         stock_name = "Sea Limited American Depositary Shares each representing one Class A Ordinary Share"
      elif (stock_value == 'MS'):
         stock_name = "Morgan Stanley Common Stock"
      elif (stock_value == 'NEE'):
         stock_name = "NextEra Energy Inc. Common Stock"
      elif (stock_value == 'LOW'):
         stock_name = "Lowe's Companies Inc. Common Stock"
      elif (stock_value == 'LIN'):
         stock_name = "Linde plc Ordinary Share"
      elif (stock_value == 'SAP'):
         stock_name = "SAP  SE ADS"
      elif (stock_value == 'ANET'):
         stock_name = "Arista Networks Inc. Common Stock"
      elif (stock_value == 'MDT'):
         stock_name = "Medtronic plc. Ordinary Shares"
      elif (stock_value == 'SONY'):
         stock_name = "Sony Group Corporation American Depositary Shares"
      elif (stock_value == 'SCHW'):
         stock_name = "Charles Schwab Corporation (The) Common Stock"
      elif (stock_value == 'UNP'):
         stock_name = "Union Pacific Corporation Common Stock"
      elif (stock_value == 'HON'):
         stock_name = "Honeywell International Inc. Common Stock"
      elif (stock_value == 'RY'):
         stock_name = "Royal Bank Of Canada Common Stock"
      elif (stock_value == 'TMUS'):
         stock_name = "T-Mobile US Inc. Common Stock"
      elif (stock_value == 'PM'):
         stock_name = "Philip Morris International Inc Common Stock"
      elif (stock_value == 'BLK'):
         stock_name = "BlackRock Inc. Common Stock"
      elif (stock_value == 'AMAT'):
         stock_name = "Applied Materials Inc. Common Stock"
      elif (stock_value == 'CHTR'):
         stock_name = "Charter Communications Inc. Class A Common Stock New"
      elif (stock_value == 'AXP'):
         stock_name = "American Express Company Common Stock"
      elif (stock_value == 'NOW'):
         stock_name = "ServiceNow Inc. Common Stock"
      elif (stock_value == 'JD'):
         stock_name = "JD.com Inc. American Depositary Shares"
      elif (stock_value == 'UL'):
         stock_name = "Unilever PLC Common Stock"
      elif (stock_value == 'TD'):
         stock_name = "Toronto Dominion Bank (The) Common Stock"
      elif (stock_value == 'BA'):
         stock_name = "Boeing Company (The) Common Stock"
      elif (stock_value == 'BMY'):
         stock_name = "Bristol-Myers Squibb Company Common Stock"
      elif (stock_value == 'SBUX'):
         stock_name = "Starbucks Corporation Common Stock"
      elif (stock_value == 'C'):
         stock_name = "Citigroup Inc. Common Stock"
      elif (stock_value == 'BHP'):
         stock_name = "BHP Group Limited American Depositary Shares (Each representing two Ordinary Shares)"
      elif (stock_value == 'HDB'):
         stock_name = "HDFC Bank Limited Common Stock"
      elif (stock_value == 'RTX'):
         stock_name = "Raytheon Technologies Corporation Common Stock"
      elif (stock_value == 'GS'):
         stock_name = "Goldman Sachs Group Inc. (The) Common Stock"
      elif (stock_value == 'TTE'):
         stock_name = "TotalEnergies SE"
      elif (stock_value == 'ISRG'):
         stock_name = "Intuitive Surgical Inc. Common Stock"
      elif (stock_value == 'BBL'):
         stock_name = "Sanofi ADS"
      elif (stock_value == 'EL'):
         stock_name = "Estee Lauder Companies Inc. (The) Common Stock"
      elif (stock_value == 'CVS'):
         stock_name = "CVS Health Corporation Common Stock"
      elif (stock_value == 'TGT'):
         stock_name = "Target Corporation Common Stock"
      elif (stock_value == 'DEO'):
         stock_name = "Diageo plc Common Stock"
      elif (stock_value == 'HSBC'):
         stock_name = "HSBC Holdings plc. Common Stock"
      elif (stock_value == 'SNOW'):
         stock_name = "Snowflake Inc. Class A Common Stock"
      elif (stock_value == 'ABNB'):
         stock_name = "Airbnb Inc. Class A Common Stock"
      elif (stock_value == 'AMT'):
         stock_name = "American Tower Corporation (REIT) Common Stock"
      elif (stock_value == 'AMGN'):
         stock_name = "Amgen Inc. Common Stock"
      elif (stock_value == 'DE'):
         stock_name = "Deere & Company Common Stock"
      elif (stock_value == 'SPGI'):
         stock_name = "S&P Global Inc. Common Stock"
      elif (stock_value == 'PLD'):
         stock_name = "Prologis Inc. Common Stock"
      elif (stock_value == 'RIVN'):
         stock_name = "Rivian Automotive Inc. Class A Common Stock"
      elif (stock_value == 'TEAM'):
         stock_name = "Atlassian Corporation Plc Class A Ordinary Shares"
      elif (stock_value == 'GE'):
         stock_name = "General Electric Company Common Stock"
      elif (stock_value == 'CAT'):
         stock_name = "Caterpillar Inc. Common Stock"
      elif (stock_value == 'SQ'):
         stock_name = "Square Inc. Class A Common Stock"
      elif (stock_value == 'ZTS'):
         stock_name = "Zoetis Inc. Class A Common Stock"
      elif (stock_value == 'PDD'):
         stock_name = "Pinduoduo Inc. American Depositary Shares"
      elif (stock_value == 'GSK'):
         stock_name = "GlaxoSmithKline PLC Common Stock"
      elif (stock_value == 'BX'):
         stock_name = "Blackstone Inc. Common Stock"
      elif (stock_value == 'MMM'):
         stock_name = "3M Company Common Stock"
      elif (stock_value == 'BUD'):
         stock_name = "Anheuser-Busch Inbev SA Sponsored ADR (Belgium)"
      elif (stock_value == 'MRNA'):
         stock_name = "Moderna Inc. Common Stock"
      elif (stock_value == 'ADP'):
         stock_name = "Automatic Data Processing Inc. Common Stock"
      elif (stock_value == 'INFY'):
         stock_name = "Infosys Limited American Depositary Shares"
      elif (stock_value == 'SYK'):
         stock_name = "Stryker Corporation Common Stock"
      elif (stock_value == 'RIO'):
         stock_name = "Rio Tinto Plc Common Stock"
      elif (stock_value == 'BKNG'):
         stock_name = "Booking Holdings Inc. Common Stock"
      elif (stock_value == 'COP'):
         stock_name = "ConocoPhillips Common Stock"
      elif (stock_value == 'LMT'):
         stock_name = "Lockheed Martin Corporation Common Stock"
      elif (stock_value == 'BAM'):
         stock_name = "Brookfield Asset Management Inc. Common Stock"
      elif (stock_value == 'GM'):
         stock_name = "General Motors Company Common Stock"
      elif (stock_value == 'CNI'):
         stock_name = "Canadian National Railway Company Common Stock"
      elif (stock_value == 'BP'):
         stock_name = "BP p.l.c. Common Stock"
      elif (stock_value == 'LRCX'):
         stock_name = "Lam Research Corporation Common Stock"
      elif (stock_value == 'SHW'):
         stock_name = "Sherwin-Williams Company (The) Common Stock"
      elif (stock_value == 'MDLZ'):
         stock_name = "Mondelez International Inc. Class A Common Stock"
      elif (stock_value == 'COIN'):
         stock_name = "Coinbase Global Inc. Class A Common Stock"
      elif (stock_value == 'USB'):
         stock_name = "U.S. Bancorp Common Stock"
      elif (stock_value == 'TJX'):
         stock_name = "TJX Companies Inc. (The) Common Stock"
      elif (stock_value == 'MU'):
         stock_name = "Micron Technology Inc. Common Stock"
      elif (stock_value == 'IBM'):
         stock_name = "International Business Machines Corporation Common Stock"
      elif (stock_value == 'PNC'):
         stock_name = "PNC Financial Services Group Inc. (The) Common Stock"
      elif (stock_value == 'UBER'):
         stock_name = "Uber Technologies Inc. Common Stock"
      elif (stock_value == 'SNAP'):
         stock_name = "Snap Inc. Class A Common Stock"
      elif (stock_value == 'GILD'):
         stock_name = "Gilead Sciences Inc. Common Stock"
      elif (stock_value == 'MMC'):
         stock_name = "Marsh & McLennan Companies Inc. Common Stock"
      elif (stock_value == 'EQNR'):
         stock_name = "Equinor ASA"
      elif (stock_value == 'CB'):
         stock_name = "Chubb Limited  Common Stock"
      elif (stock_value == 'PTR'):
         stock_name = "PetroChina Company Limited Common Stock"
      elif (stock_value == 'TFC'):
         stock_name = "Truist Financial Corporation Common Stock"
      elif (stock_value == 'MO'):
         stock_name = "Altria Group Inc."
      elif (stock_value == 'CME'):
         stock_name = "CME Group Inc. Class A Common Stock"
      elif (stock_value == 'ENB'):
         stock_name = "Enbridge Inc Common Stock"
      elif (stock_value == 'BTI'):
         stock_name = "British American Tobacco  Industries p.l.c. Common Stock ADR"
      elif (stock_value == 'CCI'):
         stock_name = "Crown Castle International Corp. (REIT) Common Stock"
      elif (stock_value == 'BNS'):
         stock_name = "Bank Nova Scotia Halifax Pfd 3 Ordinary Shares"
      elif (stock_value == 'CSX'):
         stock_name = "CSX Corporation Common Stock"
      elif (stock_value == 'F'):
         stock_name = "Ford Motor Company Common Stock"
      elif (stock_value == 'DASH'):
         stock_name = "DoorDash Inc. Class A Common Stock"
      elif (stock_value == 'RBLX'):
         stock_name = "Roblox Corporation Class A Common Stock"
      elif (stock_value == 'ICE'):
         stock_name = "Intercontinental Exchange Inc. Common Stock"
      elif (stock_value == 'ZM'):
         stock_name = "Zoom Video Communications Inc. Class A Common Stock"
      elif (stock_value == 'DUK'):
         stock_name = "Duke Energy Corporation (Holding Company) Common Stock"
      elif (stock_value == 'ITW'):
         stock_name = "Illinois Tool Works Inc. Common Stock"
      elif (stock_value == 'HCA'):
         stock_name = "HCA Healthcare Inc. Common Stock"
      elif (stock_value == 'LCID'):
         stock_name = "Lucid Group Inc. Common Stock"
      elif (stock_value == 'WDAY'):
         stock_name = "Workday Inc. Class A Common Stock"
      elif (stock_value == 'MCO'):
         stock_name = "Moody's Corporation Common Stock"
      elif (stock_value == 'EW'):
         stock_name = "Edwards Lifesciences Corporation Common Stock"
      elif (stock_value == 'CI'):
         stock_name = "Cigna Corporation Common Stock"
      elif (stock_value == 'BDX'):
         stock_name = "Becton Dickinson and Company Common Stock"
      elif (stock_value == 'MELI'):
         stock_name = "MercadoLibre Inc. Common Stock"
      elif (stock_value == 'EQIX'):
         stock_name = "Equinix Inc. Common Stock REIT"
      elif (stock_value == 'MUFG'):
         stock_name = "Mitsubishi UFJ Financial Group Inc. Common Stock"
      elif (stock_value == 'ADSK'):
         stock_name = "Autodesk Inc. Common Stock"
      elif (stock_value == 'BMO'):
         stock_name = "Bank Of Montreal Common Stock"
      elif (stock_value == 'ABB'):
         stock_name = "ABB Ltd Common Stock"
      elif (stock_value == 'IBN'):
         stock_name = "ICICI Bank Limited Common Stock"
      elif (stock_value == 'WM'):
         stock_name = "Waste Management Inc. Common Stock"
      elif (stock_value == 'REGN'):
         stock_name = "Regeneron Pharmaceuticals Inc. Common Stock"
      elif (stock_value == 'ETN'):
         stock_name = "Eaton Corporation PLC Ordinary Shares"
      elif (stock_value == 'NET'):
         stock_name = "Cloudflare Inc. Class A Common Stock"
      elif (stock_value == 'FIS'):
         stock_name = "Fidelity National Information Services Inc. Common Stock"
      elif (stock_value == 'NSC'):
         stock_name = "Norfolk Southern Corporation Common Stock"
      elif (stock_value == 'APD'):
         stock_name = "Air Products and Chemicals Inc. Common Stock"
      elif (stock_value == 'ECL'):
         stock_name = "Ecolab Inc. Common Stock"
      elif (stock_value == 'FISV'):
         stock_name = "Fiserv Inc. Common Stock"
      elif (stock_value == 'BNTX'):
         stock_name = "BioNTech SE American Depositary Share"
      elif (stock_value == 'SO'):
         stock_name = "Southern Company (The) Common Stock"
      elif (stock_value == 'RACE'):
         stock_name = "Ferrari N.V. Common Shares"
      elif (stock_value == 'CL'):
         stock_name = "Colgate-Palmolive Company Common Stock"
      elif (stock_value == 'AON'):
         stock_name = "Aon plc Class A Ordinary Shares (Ireland)"
      elif (stock_value == 'FDX'):
         stock_name = "FedEx Corporation Common Stock"
      elif (stock_value == 'COF'):
         stock_name = "Capital One Financial Corporation Common Stock"
      elif (stock_value == 'DXCM'):
         stock_name = "DexCom Inc. Common Stock"
      elif (stock_value == 'PBR'):
         stock_name = "Petroleo Brasileiro S.A.- Petrobras Common Stock"
      elif (stock_value == 'KLAC'):
         stock_name = "KLA Corporation Common Stock"
      elif (stock_value == 'STLA'):
         stock_name = "Stellantis N.V. Common Shares"
      elif (stock_value == 'NIO'):
         stock_name = "NIO Inc. American depositary shares each  representing one Class A ordinary share"
      elif (stock_value == 'UBS'):
         stock_name = "UBS Group AG Registered Ordinary Shares"
      elif (stock_value == 'CRWD'):
         stock_name = "CrowdStrike Holdings Inc. Class A Common Stock"
      elif (stock_value == 'MRVL'):
         stock_name = "Marvell Technology Inc. Common Stock"
      stock = stock_value

   # query a DataSet model,
   temp = DataSet.objects.get(title="topFiveFeats.csv")

   # extracting the JSON data into a dataframe
   extracted_df = temp.loadframe()

   # Sort & filter dataframe
   extracted_df['timestamp'] = pd.to_datetime(extracted_df['timestamp'])
   extracted_df.sort_values(by='timestamp', ascending=False, inplace=True)
   single = extracted_df.loc[(extracted_df["symbol"]==f"{stock}")]
   grouped = single.groupby(by=['symbol'], as_index=False).first()

   # Slice dataframe
   grouped.drop('1m', axis=1, inplace=True)
   grouped.drop('timestamp', axis=1, inplace=True)
   grouped.drop('symbol', axis=1, inplace=True)

   # Load the model and predicting
   temp = AiModel.objects.get(deployed=True)
   model = load_model(temp.get_titleversion() + ".h5")

   predictions = str(model.predict(grouped))
   predictions_in_percentage = float(predictions[2:12]) *100

   return render(request, 'front/prediction.html',{'stock_title': stock_name, 'predictions': '%.4f%%'% predictions_in_percentage})


def allstocks(request):
   if request.method == 'POST':
      allstocks = ["AAPL","MSFT","GOOG","GOOGL",'AMZN',
'TSLA','FB','NVDA','TSM','JPM','V','JNJ','UNH','HD','ADI','BAC','WMT','BABA','ASML','PG',
'MA','ADBE','NFLX','NTES','CRM','PFE','DIS','NKE','XOM','NVO', 'ORCL','TM','TMO','LLY','CMCSA',
'KO','PYPL', 'AVGO','ACN','COST', 'ABT', 'PEP','DHR','CVX', 'CSCO','VZ', 'MRK', 'ABBV',
'SHOP', 'QCOM', 'INTC', 'WFC', 'MCD','AMD','NVS','UPS','INTU','TXN', 'AZN', 'T',
 'SE','MS','NEE','LOW','LIN', 'SAP',  'ANET',  'MDT', 'SONY', 'SCHW', 'UNP', 'HON',
 'RY','TMUS', 'PM',  'BLK', 'AMAT', 'CHTR','AXP','NOW', 'JD', 'UL', 'TD',  'BA',
  'BMY', 'SBUX', 'C', 'BHP', 'HDB', 'RTX', 'GS', 'TTE', 'ISRG', 'BBL', 'SNY',
 'EL','CVS','TGT','DEO','HSBC',  'SNOW', 'ABNB','AMT',  'AMGN', 'DE', 'SPGI', 'PLD',
'RIVN','TEAM','GE','CAT','SQ', 'ZTS', 'PDD', 'ANTM', 'GSK', 'BX', 'MMM', 'BUD','MRNA',
  'ADP',  'INFY', 'SYK','RIO', 'BKNG', 'COP', 'LMT','BAM','GM','CNI', 'BP','LRCX',
   'SHW','MDLZ','COIN','USB','TJX','MU','IBM','PNC','UBER','SNAP','GILD',
   'MMC','EQNR','CB', 'PTR', 'TFC', 'MO', 'CME','ENB','BTI','CCI',
   'BNS','CSX', 'F', 'DASH', 'RBLX','ICE', 'ZM', 'DUK', 'ITW', 'HCA', 'LCID',
   'WDAY','MCO','EW','CI','BDX', 'MELI', 'EQIX','MUFG','ADSK','BMO','ABB','IBN',
   'WM','REGN','ETN','NET','FIS', 'NSC','APD', 'ECL', 'FISV', 'BNTX', 'SO', 'RACE','CL',
   'AON','FDX', 'COF', 'DXCM', 'PBR', 'KLAC', 'STLA','NIO','UBS','CRWD','MRVL']


   # query a DataSet model,
   temp = DataSet.objects.get(title="topFiveFeats.csv")

   # extracting the JSON data into a dataframe
   extracted_df = temp.loadframe()

   # Sort & filter dataframe
   extracted_df['timestamp'] = pd.to_datetime(extracted_df['timestamp'])
   extracted_df.sort_values(by='timestamp', ascending=False, inplace=True)
   grouped = extracted_df.groupby(by=['symbol'], as_index=False).first()

   # Slice dataframe
   grouped.drop('1m', axis=1, inplace=True)
   grouped.drop('timestamp', axis=1, inplace=True)
   grouped.drop('symbol', axis=1, inplace=True)
   
   # Load the model and predicting
   temp = AiModel.objects.get(deployed=True)
   model = load_model(temp.get_titleversion() + ".h5")

   print(grouped)

   for i in range (0,len(allstocks)):
     predictions = str(model.predict(grouped))
     predictions_in_percentage = float(predictions[2:12]) * 100
     return render(request, 'front/allstocks.html',{ 'allstocks': allstocks,'predictions': '%.4f%%'% predictions_in_percentage})


