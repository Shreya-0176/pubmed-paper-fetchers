import argparse  # Import the argparse module to handle command-line arguments
from fetch_papers import fetch_pubmed_papers, fetch_paper_details  # Correct import statement
import logging
logging.basicConfig(level=logging.DEBUG)  # Enable debug logging


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Fetch research papers based on a query.")
    
    # Add arguments to the parser
    parser.add_argument('query', type=str, help="Query to search for papers on PubMed.")
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug information.")
    parser.add_argument('-f', '--file', type=str, help="Save results to the specified file.")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Fetch the papers based on the query (this function is in fetch_papers.py)
    paper_ids = fetch_pubmed_papers(args.query)  # Fetch paper IDs based on the query
    papers = fetch_paper_details(paper_ids)  # Fetch detailed paper information

    # If user provided a filename, save the results to that file
    if args.file:
        save_papers_to_csv(papers, args.file)
    else:
        # If no file is provided, print the results to the console
        for paper in papers:
            print(paper)

def save_papers_to_csv(papers, filename):
    import csv  # Import the csv module to write to a CSV file

    # Get the keys (column names) from the first paper dictionary (assuming papers are in dictionary form)
    keys = papers[0].keys() if papers else []

    # Open the file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()  # Write the header (column names)
        writer.writerows(papers)  # Write the data rows
    print(f"Results saved to {filename}")
# Later in the code, print debug information
logging.debug("This is a debug message.")


# Entry point of the script
if __name__ == '__main__':
    main()
