
# PubMed Paper Fetcher 📝

A Python program to fetch research papers from PubMed based on a user-specified query. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

---

## ✨ Features
- Fetches research papers using the **PubMed API**.
- Supports **full query syntax** for flexible searching.
- Identifies **non-academic authors** affiliated with pharmaceutical/biotech companies.
- Outputs results as a **CSV file** or prints them to the console.
- Supports **command-line options** for debugging and file output.
- Comprehensive **error handling** for invalid queries and API failures.
- Uses **typed Python** and modular code organization for clarity and performance.

---

## 🛠️ Installation

Clone the repository:
```bash
git clone https://github.com/Shreya-0176/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

Install dependencies using **Poetry**:
```bash
poetry install
```

Activate the virtual environment:
```bash
poetry shell
```

---

## 🚀 Usage

Basic usage:
```bash
python -m pubmed_paper_fetcher.cli "malaria detection"
```

Save results to a CSV file:
```bash
python -m pubmed_paper_fetcher.cli "cancer research" --file cancer_papers.csv
```

Enable debug mode:
```bash
python -m pubmed_paper_fetcher.cli "artificial intelligence in healthcare" --debug
```

Display help:
```bash
python -m pubmed_paper_fetcher.cli --help
```

---

## 🗃️ Code Organization

```
pubmed-paper-fetcher/
├── pubmed_paper_fetcher/
│   ├── __init__.py          # Initializes the package
│   ├── cli.py               # Command-line interface
│   ├── fetch_papers.py      # Core module for fetching papers
├── poetry.lock              # Dependency lock file
├── pyproject.toml           # Poetry configuration file
├── README.md                # Project documentation
```

- The project is structured into two parts:
  - **Core Module:** Handles API calls and data processing.
  - **CLI Wrapper:** Provides a user-friendly command-line interface.

---

## 🧪 Testing and Debugging

Enable detailed logs during execution using the `--debug` flag:
```bash
python -m pubmed_paper_fetcher.cli "machine learning" --debug
```

Check logs for information on API responses and processing steps.

---

## 📝 Development

To add new features or fix bugs:
1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes.**
4. **Commit your changes:**
   ```bash
   git commit -m "Add new feature"
   ```
5. **Push to your branch:**
   ```bash
   git push origin feature-branch
   ```
6. **Submit a pull request.**

---

## 🏆 Credits
- Uses the **PubMed API** for fetching research papers.
- Managed with **Poetry** for dependency management.
- Developed with guidance from **large language models** and Python best practices.

---

## 📜 License
This project is licensed under the **MIT License**.

---
