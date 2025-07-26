import pandas as pd

def run_analysis(df, lang):
    print(f"📊 {lang['shape']}: {df.shape}")
    print(f"📈 {lang['columns']}: {list(df.columns)}\n")

    print(f"{lang['basic_stats']}:")
    print(df.describe(include='all').transpose())

    print(f"\n{lang['nulls']}:")
    print(df.isnull().sum())

    print(f"\n{lang['correlation_matrix']}:")
    print(df.corr(numeric_only=True))
