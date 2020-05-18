import pandas as pd
import re



def convert():

    df = pd.read_excel('data.xlsx')
    df=df[df['Product Code'].str.contains("PROD").notnull()]



    return df.to_html(classes="table table-hover table-bordered results", index=False)


if __name__ == "__main__":
    app.run()

