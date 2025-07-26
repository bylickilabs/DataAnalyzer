# 📊 Data Insights Analyzer

> **Data Insights Analyzer** is a multilingual, production-grade command-line tool for analyzing structured datasets using **pandas**. 
  - It supports CSV and Excel files, provides detailed statistical summaries, and enables correlation and null-value inspection 
    - all in your preferred language (currently English and German).

<br>

---

<br>

## 🚀 Features

- ✅ CSV and Excel file support
- ✅ Multilingual interface (`en`, `de`)
- ✅ Data shape and column overview
- ✅ Descriptive statistics (mean, std, min, max, etc.)
- ✅ Null value summary
- ✅ Correlation matrix (Pearson)
- ✅ Modular and extendable architecture

<br>

---

<br>

## 📂 Project Structure

```
data_insights_analyzer/
├── main.py                   # Entry point
├── modules/
│   ├── analysis.py           # Core analysis logic
│   └── language.py           # Language loader
├── i18n/
│   ├── en.json               # English translations
│   └── de.json               # German translations
```

<br>

---

<br>

## 🛠️ Requirements

- Python 3.8+
- pandas

Install with:

```yarn
pip install pandas
```

<br>

---

<br>

## 🧑‍💻 Usage

```yarn
python main.py --file data.csv --lang en
```

Parameters:

| Option     | Description                            |
|------------|----------------------------------------|
| `--file`   | Path to `.csv` or `.xlsx` data file    |
| `--lang`   | Language code: `en` (English), `de` (German) |

<br>

---

<br>

## 🌍 Language Support

Language files are stored in `i18n/` and are easy to extend (add `fr.json`, `es.json`, etc.).

<br>

---

<br>

## 📘 License

MIT License – free to use, modify and distribute.
[LICENSE](LICENSE)

<br>

---

<br>

## 👨‍💻 Author

**BYLICKILABS** – Secure Data & Software Engineering  
