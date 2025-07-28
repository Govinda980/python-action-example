import pandas as pd


def read_csv_file():
    df = pd.read_csv('data.csv')
    df1 = pd.read_json('data.json')
    print(df.to_string())
    print(pd.options.display.max_rows)
    df.to_excel('output.xlsx')
    print("head\n", df.head(10))  # default 5 row
    print("tail\n", df.tail(10))
    print(df.info())


def cleaning_empty_data():
    df = pd.read_csv('data_clean.csv')
    df.dropna(inplace=True)  # remove null value
    df.fillna(2023, inplace=True)  # replace with 2023 with null val
    df['Calories'].fillna(2023, inplace=True)  # specific column
    x = df['Calories'].mean()  # with mean value
    df['Calories'].fillna(x, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])  # making  correct format
    df.loc[7, 'Duration'] = 45  # fixing wrong data
    print(df.to_string())


def correcting_df_data():
    df = pd.read_csv('data_clean.csv')
    for x in df.index:
        if df.loc[x, 'Duration'] > 120:
            df.loc[x, 'Duration'] = 120


def removing_row():
    df = pd.read_csv('data_clean.csv')
    for x in df.index:
        if df.loc[x, 'Duration'] > 120:
            df.drop(x, inplace=True)
    df.drop_duplicates(inplace=True)  # remove duplicate row
    # print(df.duplicated())  # to check duplicate
    df.to_csv('test_by_op.csv')


if __name__ == '__main__':
    # read_csv_file()
    # cleaning_empty_data()
    # correcting_df_data()
    removing_row()
