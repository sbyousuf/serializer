import pandas as pd
import re
def price(df,name):
    def extract_int_part(value):
        # استفاده از regex برای استخراج بخش عددی
        match = re.search(r'\d+', str(value))
        if match:
            return int(match.group())
        return None

    df['int_part'] = df["review_count"].apply(extract_int_part)
    #average_prices = df.groupby('city')['int_part'].median().rese_index()
    #average_prices_sorted = average_prices.sort_values(by='int_part', ascending=False)
    df.to_csv(f'result\{name}.csv', index=False)