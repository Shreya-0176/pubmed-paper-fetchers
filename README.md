# PubMed Paper Fetcher

A Python program to fetch research papers from PubMed based on a user-specified query. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Features
- Fetches research papers using the PubMed API.
- Supports PubMed's full query syntax for flexible searching.
- Identifies non-academic authors affiliated with pharmaceutical/biotech companies.
- Outputs results as a CSV file or prints them to the console.
- Supports command-line options for debugging and file output.
- Comprehensive error handling for invalid queries and API failures.
- Uses typed Python and modular code organization for clarity and performance.

## Installation

Clone the repository:
```bash
git clone https://github.com/Shreya-0176/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

Install dependencies using Poetry:
```bash
poetry install
```

## Usage

Basic usage:
```bash
python cli.py "malaria detection"
```

Save results to a CSV file:
```bash
python cli.py "cancer research" --file cancer_papers.csv
```

Enable debug mode:
```bash
python cli.py "artificial intelligence in healthcare" --debug
```

Display help:
```bash
python cli.py --help
```

## Development

To add new features or fix bugs:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Code Organization
- The project is structured into two parts: a core module for paper fetching and a CLI wrapper.
- The `fetcher` module handles the core functionality, including API calls and data processing.
- The `cli.py` script provides the command-line interface to interact with the core module.

## Testing and Debugging
- Use the `--debug` flag to enable detailed logs during execution.
- Check logs for information on API responses and processing steps.

## Credits
- Uses the PubMed API for fetching research papers.
- Managed with Poetry for dependency management.
- Developed with guidance from large language models and Python best practices.

## License
MIT License

