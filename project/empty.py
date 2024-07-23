def calculate_empty_percentage(df, column_name):
    null_or_empty_count = df[column_name].isna().sum() + (df[column_name] == 0).sum()
    total_count = len(df)
    percentage_empty_or_null = (null_or_empty_count / total_count) * 100
    return percentage_empty_or_null

import re

def extract_int_part(value):
    # استفاده از regex برای استخراج بخش عددی
    match = re.search(r'\d+', str(value))
    if match:
        return int(match.group())
    return None

def calculate_below_ten_percentage(df, column_name):

    # استخراج بخش عددی از هر مقدار
    df['int_part'] = df[column_name].apply(extract_int_part)
    
    # شمارش مقادیر کمتر از ۱۰
    below_ten_count = df['int_part'].dropna().apply(lambda x: x < 10).sum()
    
    # محاسبه درصد
    total_count = df['int_part'].count()
    percentage_below_ten = (below_ten_count / total_count) * 100

    return percentage_below_ten