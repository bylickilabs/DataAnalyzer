import pandas as pd
import os
import argparse
from modules.language import load_language
from modules.analysis import run_analysis

def main():
    parser = argparse.ArgumentParser(description="Data Insights Analyzer")
    parser.add_argument("--file", required=True, help="Path to CSV or Excel file")
    parser.add_argument("--lang", default="en", help="Language code (en/de)")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("❌ File not found.")
        return

    lang = load_language(args.lang)
    print(f"🔍 {lang['welcome']}")

    try:
        if args.file.endswith(".csv"):
            df = pd.read_csv(args.file)
        elif args.file.endswith(".xlsx"):
            df = pd.read_excel(args.file)
        else:
            print(lang['unsupported_format'])
            return

        run_analysis(df, lang)
    except Exception as e:
        print(f"{lang['error_occurred']}: {e}")

if __name__ == "__main__":
    main()
