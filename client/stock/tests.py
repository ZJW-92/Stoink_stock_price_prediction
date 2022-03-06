
from django.test import TestCase, Client
from django.urls import reverse
from h5py._hl import dataset
from tensorflow.python.keras.backend import tile
from stock.models import AiModel, DataSet
import stock.admin as admin
import pandas as pd
from os.path import exists
import unittest

class AiModelTestCase(TestCase):
    def setUp(self):
        
        # create dataset
        testDataset = DataSet.objects.create(title='testData.csv')

        # Create AiModel
        AiModel.objects.create(title='UnitModel', deployed=True, dataset=testDataset)

    def test_train_model_saves_file(self):
        testModel = AiModel.objects.get(id=1)

        # Simulate data uploaded to admin page and train a model
        df = pd.read_csv(filepath_or_buffer='data/testData.csv')
        testModel.dataset.putframe(df)
        testModel.train_model()

        # Assert if the file was created
        file_exists = exists((testModel.get_titleversion() + ".h5"))
        self.assertTrue(file_exists, msg='File does not exist')

# Create your tests here.
class Column(TestCase):
    def test_columns_topfivefeats(self):
        df = pd.read_csv(r'../client/data/topFiveFeats.csv', sep=',')
        expected = ["timestamp", "symbol", "1m", "reportedEPS", "totalNonCurrentAssets", "depreciation",
                    "proceedsFromRepaymentsOfShortTermDebt", "currentAccountsPayable"]
        self.assertTrue(set(expected) <= set(df.columns))


class TestMethods(unittest.TestCase):

  def test_single_stock_prediction(self):
    client = Client()
    response = client.post('/predict', {'stock_title': 'AAPL'})

    self.assertEqual(response.status_code, 200, msg="Wrong status code returned")
    self.assertEqual(response.context['stock_title'], 'Apple Inc. Common Stock', msg="Wrong stock name returned")
    
    response = client.post('/predict', {'stock_title': 'MRVL'})
    self.assertEqual(response.status_code, 200, msg="Wrong status code returned")
    self.assertEqual(response.context['stock_title'], 'Marvell Technology Inc. Common Stock', msg="Wrong stock name returned")

  def test_single_stock_not_empty(self):
   stock = ['']
   # error message in case if test case got failed
   message = "single stock is empty"
   self.assertIsNotNone(stock, message)

  def test_manual_predict_not_empty(self):
    def manualPredict(request):
      if request.method == 'GET':
       var1 = (float(request.GET['Inputone']))
       var2 = (float(request.GET['Inputtwo']))
       var3 = (float(request.GET['Inputthree']))
       var4 = (float(request.GET['Inputfour']))
       var5 = (float(request.GET['Inputfive']))
      manual_predict = [var1,var2,var3,var4,var5]
    # error message in case if test case got failed
      message = "manual predict is empty"
      self.assertIsNotNone(manual_predict, message)

  def test_all_stocks_not_empty(self):
   allstocks = ["AAPL", "MSFT", "GOOG", "GOOGL", 'AMZN',
                'TSLA', 'FB', 'NVDA', 'TSM', 'JPM', 'V', 'JNJ', 'UNH', 'HD', 'ADI', 'BAC', 'WMT', 'BABA', 'ASML', 'PG',
                'MA', 'ADBE', 'NFLX', 'NTES', 'CRM', 'PFE', 'DIS', 'NKE', 'XOM', 'NVO', 'ORCL', 'TM', 'TMO', 'LLY',
                'CMCSA','KO', 'PYPL', 'AVGO', 'ACN', 'COST', 'ABT', 'PEP', 'DHR', 'CVX', 'CSCO', 'VZ', 'MRK', 'ABBV',
                'SHOP', 'QCOM', 'INTC', 'WFC', 'MCD', 'AMD', 'NVS', 'UPS', 'INTU', 'TXN', 'AZN', 'T',
                'SE', 'MS', 'NEE', 'LOW', 'LIN', 'SAP', 'ANET', 'MDT', 'SONY', 'SCHW', 'UNP', 'HON',
                'RY', 'TMUS', 'PM', 'BLK', 'AMAT', 'CHTR', 'AXP', 'NOW', 'JD', 'UL', 'TD', 'BA',
                'BMY', 'SBUX', 'C', 'BHP', 'HDB', 'RTX', 'GS', 'TTE', 'ISRG', 'BBL', 'SNY',
                'EL', 'CVS', 'TGT', 'DEO', 'HSBC', 'SNOW', 'ABNB', 'AMT', 'AMGN', 'DE', 'SPGI', 'PLD',
                'RIVN', 'TEAM', 'GE', 'CAT', 'SQ', 'ZTS', 'PDD', 'ANTM', 'GSK', 'BX', 'MMM', 'BUD', 'MRNA',
                'ADP', 'INFY', 'SYK', 'RIO', 'BKNG', 'COP', 'LMT', 'BAM', 'GM', 'CNI', 'BP', 'LRCX',
                'SHW', 'MDLZ', 'COIN', 'USB', 'TJX', 'MU', 'IBM', 'PNC', 'UBER', 'SNAP', 'GILD',
                'MMC', 'EQNR', 'CB', 'PTR', 'TFC', 'MO', 'CME', 'ENB', 'BTI', 'CCI',
                'BNS', 'CSX', 'F', 'DASH', 'RBLX', 'ICE', 'ZM', 'DUK', 'ITW', 'HCA', 'LCID',
                'WDAY', 'MCO', 'EW', 'CI', 'BDX', 'MELI', 'EQIX', 'MUFG', 'ADSK', 'BMO', 'ABB', 'IBN',
                'WM', 'REGN', 'ETN', 'NET', 'FIS', 'NSC', 'APD', 'ECL', 'FISV', 'BNTX', 'SO', 'RACE', 'CL',
                'AON', 'FDX', 'COF', 'DXCM', 'PBR', 'KLAC', 'STLA', 'NIO', 'UBS', 'CRWD', 'MRVL']
   # error message in case if test case got failed
   message = "all stock list is empty"
   self.assertIsNotNone(allstocks, message)

  def test_all_stocks_length(self):
   allstocks = ["AAPL", "MSFT", "GOOG", "GOOGL", 'AMZN',
                'TSLA', 'FB', 'NVDA', 'TSM', 'JPM', 'V', 'JNJ', 'UNH', 'HD', 'ADI', 'BAC', 'WMT', 'BABA', 'ASML', 'PG',
                'MA', 'ADBE', 'NFLX', 'NTES', 'CRM', 'PFE', 'DIS', 'NKE', 'XOM', 'NVO', 'ORCL', 'TM', 'TMO', 'LLY',
                'CMCSA','KO', 'PYPL', 'AVGO', 'ACN', 'COST', 'ABT', 'PEP', 'DHR', 'CVX', 'CSCO', 'VZ', 'MRK', 'ABBV',
                'SHOP', 'QCOM', 'INTC', 'WFC', 'MCD', 'AMD', 'NVS', 'UPS', 'INTU', 'TXN', 'AZN', 'T',
                'SE', 'MS', 'NEE', 'LOW', 'LIN', 'SAP', 'ANET', 'MDT', 'SONY', 'SCHW', 'UNP', 'HON',
                'RY', 'TMUS', 'PM', 'BLK', 'AMAT', 'CHTR', 'AXP', 'NOW', 'JD', 'UL', 'TD', 'BA',
                'BMY', 'SBUX', 'C', 'BHP', 'HDB', 'RTX', 'GS', 'TTE', 'ISRG', 'BBL', 'SNY',
                'EL', 'CVS', 'TGT', 'DEO', 'HSBC', 'SNOW', 'ABNB', 'AMT', 'AMGN', 'DE', 'SPGI', 'PLD',
                'RIVN', 'TEAM', 'GE', 'CAT', 'SQ', 'ZTS', 'PDD', 'ANTM', 'GSK', 'BX', 'MMM', 'BUD', 'MRNA',
                'ADP', 'INFY', 'SYK', 'RIO', 'BKNG', 'COP', 'LMT', 'BAM', 'GM', 'CNI', 'BP', 'LRCX',
                'SHW', 'MDLZ', 'COIN', 'USB', 'TJX', 'MU', 'IBM', 'PNC', 'UBER', 'SNAP', 'GILD',
                'MMC', 'EQNR', 'CB', 'PTR', 'TFC', 'MO', 'CME', 'ENB', 'BTI', 'CCI',
                'BNS', 'CSX', 'F', 'DASH', 'RBLX', 'ICE', 'ZM', 'DUK', 'ITW', 'HCA', 'LCID',
                'WDAY', 'MCO', 'EW', 'CI', 'BDX', 'MELI', 'EQIX', 'MUFG', 'ADSK', 'BMO', 'ABB', 'IBN',
                'WM', 'REGN', 'ETN', 'NET', 'FIS', 'NSC', 'APD', 'ECL', 'FISV', 'BNTX', 'SO', 'RACE', 'CL',
                'AON', 'FDX', 'COF', 'DXCM', 'PBR', 'KLAC', 'STLA', 'NIO', 'UBS', 'CRWD', 'MRVL']
   assert len(allstocks) == 200, "length of all stock list should be 200"
   # error message in case if test case got failed
   message = "all stock length is not 200"
   self.assertTrue(len(allstocks), message)

  if __name__ == '__main__':
       unittest.main()
