# Imports
import pandas as pd
import numpy as np


def clean_raw_data():

    # Loading the data from CSV into pandas dataframe
    tempIncomeStatement = pd.read_csv (r'../client/data/income_statement.csv', sep=',')
    tempCashFlow = pd.read_csv (r'../client/data/cash_flow.csv', sep=',')
    tempBalanceSheet = pd.read_csv (r'../client/data/balance-sheet.csv', sep=',')
    tempEarnings = pd.read_csv (r'../client/data/EARNINGS.csv', sep=',')
    tempMonthly = pd.read_csv (r'../client/data/monthly-data.csv', sep=',')
    TickerSymbols = pd.read_csv (r'../client/data/nasdaq_screener_sorted_values.csv', sep=',')

    # renaming Balance sheet column "fiscalDateEnding" to "timestamp" to match column name on both dataframes
    tempIncomeStatement = tempIncomeStatement.rename(columns={"fiscalDateEnding": "timestamp"})
    tempCashFlow = tempCashFlow.rename(columns={"fiscalDateEnding": "timestamp"})
    tempBalanceSheet = tempBalanceSheet.rename(columns={"fiscalDateEnding": "timestamp"})
    tempEarnings = tempEarnings.rename(columns={"fiscalDateEnding": "timestamp"})

    # Merging all 4 frames into one

    # Daily dates does not overlap on both dataframes, CompanyMonthly has the last trading day (not including weekends)
    # While CompanyBalanceSheet always has the last day of the month (including weekends)
    # We need to cut out the daily date for both dataframes["timestamp"], to be able to merge them properly.
    # Slicing the timestamp in CompanyMonthly, removing the days
    sliceMonthly = tempMonthly["timestamp"].str.slice(0, -3)
    tempMonthly["timestamp"] = sliceMonthly

    # Slicing the timestamp in Income Statement, removing the days
    sliceIncomestatement = tempIncomeStatement["timestamp"].str.slice(0, -3)
    tempIncomeStatement["timestamp"] = sliceIncomestatement

    # Slicing the timestamp in Cash Flow, removing the days
    sliceCashFlow = tempCashFlow["timestamp"].str.slice(0, -3)
    tempCashFlow["timestamp"] = sliceCashFlow

    # Slicing the timestamp in CompanyBalanceSheet, removing the days
    sliceBalanceSheet = tempBalanceSheet["timestamp"].str.slice(0, -3)
    tempBalanceSheet["timestamp"] = sliceBalanceSheet

    # Slicing the timestamp in Earnings, removing the days
    sliceEarnings = tempEarnings["timestamp"].str.slice(0, -3)
    tempEarnings["timestamp"] = sliceEarnings

    # for each company we want to make adjustments needed for each companies
    # features and then we will merge them into one df
    TickerSymbols = TickerSymbols[~TickerSymbols['Symbol'].isin(['RIVN'])]
    final_df = pd.DataFrame()

    for tickerSymbol in TickerSymbols["Symbol"]:

        # filter all dataframes for each tickersymbol (stock)
        CompanyIncomeStatement = tempIncomeStatement.loc[tempIncomeStatement["symbol"] == tickerSymbol]
        CompanyCashFlow = tempCashFlow.loc[tempCashFlow["symbol"] == tickerSymbol]
        CompanyBalanceSheet = tempBalanceSheet.loc[tempBalanceSheet["symbol"] == tickerSymbol]
        CompanyEarnings = tempEarnings.loc[tempEarnings["symbol"] == tickerSymbol]
        CompanyMonthly = tempMonthly.loc[tempMonthly["Symbol"] == tickerSymbol]

        # Removing symbol for all Company dataframes
        CompanyIncomeStatement.drop(["reportedCurrency", 'symbol'], axis=1, inplace=True)
        CompanyCashFlow.drop(["reportedCurrency", 'symbol'], axis=1, inplace=True)
        CompanyBalanceSheet.drop(["reportedCurrency", 'symbol'], axis=1, inplace=True)
        CompanyEarnings.drop(['symbol', 'reportedDate'], axis=1, inplace=True)
        #CompanyMonthly.drop(['Symbol'], axis=1, inplace=True)

        # Cutting out unnecessary data from the CompanyMonthly
        # We only need price data in CompanyMonthly within the daterange of the 20 rows on CompanyBalanceSheet data
        # every row is 3 months in CompanyBalanceSheet. Every row in CompanyMonthly is 1 month, 3x20 = 60.
        # !!!! NOt using 3m labels anymore, but keeping the code, it doesn't make a difference.
        idx = (CompanyMonthly.index[0] + 60)
        CompanyMonthly = CompanyMonthly.loc[:idx]

        # calculating 1 month labels
        CompanyMonthly["1m"] = CompanyMonthly["close"].pct_change(periods=-1).shift(periods=1)
        cat = ["timestamp", "1m"]

        # merge all df into a temp df
        temp_df = pd.merge(CompanyIncomeStatement, CompanyCashFlow, how="outer", on="timestamp")
        temp_df = pd.merge(temp_df, CompanyBalanceSheet, how="outer", on="timestamp")
        temp_df = pd.merge(temp_df, CompanyEarnings, how="outer", on="timestamp")

        # merging the rows from balance sheet and monthly on timestamp.
        merged_df = pd.merge(temp_df, CompanyMonthly, how="outer", on="timestamp")

        # removing the rows over 20
        merged_df = merged_df.loc[:19]

        # calculate how much the increase is in percentage, interval of 3 months
        # also offsetting by 1, to get the labels on the correct row.
        #merged_df["3m"] = merged_df["close"].pct_change(periods = -1).shift(periods = 1)

        # Removing the first row, because we do not have a label for it, 3 months have not passed yet
        # for us to get the end price of the 3 month cycle
        #merged_df.drop(index=merged_df.index[0], axis=0, inplace=True)

        # Also dropping columns that we do not need, symbol, Symbol, open, high, low, close, volume etc.
        merged_df.drop(['open', 'high', 'low', 'volume', "close"], axis=1, inplace=True)

        # replacing all "None" strings with NaN data type
        merged_df = merged_df.replace('None', np.nan)

        for col in merged_df.columns:
            if col != "Symbol":        
                if col != "timestamp":
                    if col != "1m":
                        merged_df[col] = merged_df[col].astype("float")
                        merged_df[col] = merged_df[col].replace(-np.inf, np.nan)
                        merged_df[col] = merged_df[col].replace(np.inf, np.nan)
                        merged_df[col] = merged_df[col].replace(np.nan, merged_df[col].mean())
                        merged_df[col] = merged_df[col].pct_change(periods=-1).shift(periods=0)
        print(merged_df[cat].head(21))

        # adding it to the final dataframe
        # print(str(col) + " Percentage difference: ")
        # print(merged_df.head(10))

        # merged_df.drop(index=merged_df.index[-1], axis=0, inplace=True)
        final_df = pd.concat([final_df, merged_df], axis=0)

    # Randomly shuffles the rows, better for training the model later
    # Also resetting the Index for the dataframe
#    final_df = final_df.sample(frac=1).reset_index(drop=True)

    # Filling out the remaining NaNs and inf with mean value of the column
    for col in final_df.columns:
        if col != "Symbol":        
            if col != "timestamp":
                if col != "1m":
                    final_df[col] = final_df[col].replace(-np.inf, np.nan)
                    final_df[col] = final_df[col].replace(np.inf, np.nan)
                    final_df[col] = final_df[col].replace(np.nan, final_df[col].mean())

    # deleting columns with more than 1 % nan values
    m = len(final_df)
    for col in final_df.columns:
        if col != "Symbol":                    
            if col != "timestamp":
                if col != "1m":
                    percentageNan = ((final_df[col].isnull().sum()/m)*100)
                    print(str(col) + " has " + str(percentageNan))

                    if ((final_df[col].isnull().sum()/m)*100) >= 1:
                        final_df.drop(col, axis=1, inplace=True)
                        print(str(col) + " has been dropped.")

    # Again filling out with the mean
    for col in final_df.columns:
        if col != "Symbol":        
            if col != "timestamp":
                if col != "1m":
                    final_df[col] = final_df[col].replace(np.inf, final_df[col].mean())

    # Dropping rows with 1m NaN values
    final_df = final_df[final_df['1m'].notna()]

    # Copying dataframe
    feature_corr = final_df.copy().corr()

    # Correlation calculation
    sortedDesc = feature_corr["1m"].sort_values(ascending=False)

    # Extracting the top 5 features + 1 label = 6 columns
    cols_extract = sortedDesc[0: 6].keys()

    # Export to CSV file
    df_to_export = final_df[cols_extract]
    df_to_export["symbol"] = final_df["Symbol"]
    df_to_export["timestamp"] = final_df["timestamp"]
    print(df_to_export)
    df_to_export.to_csv(r'../client/data/topFiveFeats.csv', sep= ",", index = False)

# Dummycode, REMOVE!
for i in range(1):
    clean_raw_data()

