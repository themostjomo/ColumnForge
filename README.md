<div align="center">

```
                                          
      _|    _|_|    _|      _|    _|_|    
      _|  _|    _|  _|_|  _|_|  _|    _|  
      _|  _|    _|  _|  _|  _|  _|    _|  
_|    _|  _|    _|  _|      _|  _|    _|  
  _|_|      _|_|    _|      _|    _|_|    
                                          
```

# 🔥 ColumnForge

### Batch-split spreadsheet columns into clean `.txt` files — one folder, one command.

![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-required-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-success?style=for-the-badge)
![Made by](https://img.shields.io/badge/made%20by-JOMO-FF6B6B?style=for-the-badge)

**Made by [JOMO](https://github.com/themostjomo) · [@themostjomo](https://github.com/themostjomo)**

</div>

---

## ⚡ What it does

Point **ColumnForge** at a folder full of `.xlsx` files. For *every* spreadsheet inside, it instantly creates a matching `output-<filename>/` folder containing one `.txt` file per column — named after the column header, one value per line.

No clicking through Excel. No manual copy-pasting. One command, batch-processed.

```
📂 spreadsheets/
├── bitcoin.xlsx
├── eth.xlsx
└── sol.xlsx
```

⬇️ run ColumnForge ⬇️

```
📂 spreadsheets/
├── bitcoin.xlsx
├── eth.xlsx
├── sol.xlsx
├── 📁 output-bitcoin/
│   ├── Date.txt
│   ├── Price.txt
│   └── Volume.txt
├── 📁 output-eth/
│   ├── Date.txt
│   ├── Price.txt
│   └── Volume.txt
└── 📁 output-sol/
    ├── Date.txt
    ├── Price.txt
    └── Volume.txt
```

---

## 🚀 Quick start

### 1. Clone it
```bash
git clone https://github.com/themostjomo/columnforge.git
cd columnforge
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> 💡 **macOS / Homebrew users:** if you hit an `externally-managed-environment` error, use a virtual environment instead:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> ```

### 3. Run it on a folder of spreadsheets
```bash
python columnforge.py /path/to/your/spreadsheets
```

That's it. 🎉

---

## 🛠️ Usage

```bash
python columnforge.py <folder> [--sheet SHEET_NAME] [--version]
```

| Argument     | Required | Description                                              |
|--------------|:--------:|-----------------------------------------------------------|
| `folder`     |    ✅    | Folder containing one or more `.xlsx` files               |
| `--sheet`    |    ❌    | Sheet name or index to read (default: first sheet)        |
| `--version`  |    ❌    | Print the current ColumnForge version                     |

### Examples

```bash
# Process every spreadsheet in the current folder
python columnforge.py .

# Process a specific folder
python columnforge.py ~/Desktop/crypto-data

# Use a specific sheet across all files
python columnforge.py ~/Desktop/crypto-data --sheet "Sheet2"
```

---

## ✨ Features

- 📦 **Batch by default** — drop in 1 or 100 spreadsheets, same command
- 🗂️ **Auto-organized output** — each spreadsheet gets its own clean output folder
- 🧹 **Safe filenames** — illegal characters in column headers get sanitized automatically
- 🔁 **Duplicate-proof** — repeated column names get `_1`, `_2`, etc. instead of overwriting
- 🛡️ **Fault-tolerant** — one bad file won't stop the whole batch
- 🚫 **Ignores Excel lock files** — skips `~$file.xlsx` temp files automatically

---

## 📋 Requirements

- Python 3.9+
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

---

## 📄 License

Released under the [MIT License](LICENSE).

---

<div align="center">

### 🐍 Built with Python by **JOMO**

[![GitHub](https://img.shields.io/badge/GitHub-@themostjomo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/themostjomo)

</div>
