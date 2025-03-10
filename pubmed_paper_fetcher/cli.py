import argparse  # To handle command-line arguments
import logging  # For logging debug and info messages
from pubmed_paper_fetcher.fetch_papers import fetch_pubmed_papers, fetch_paper_details, save_papers_to_csv
import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("Please provide a search term.")
        sys.exit(1)
    search_term = " ".join(args)
    print(f"Searching for papers on: {search_term}")
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Fetch research papers based on a query.")

    # Add arguments to the parser
    parser.add_argument('query', type=str, help="Query to search for papers on PubMed.")
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug information.")
    parser.add_argument('-f', '--file', type=str, help="Save results to the specified file.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Configure logging level based on the debug flag
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    # Log the query being fetched
    logging.info(f"Fetching papers for query: {args.query}")

    # Fetch the papers based on the query
    paper_ids = fetch_pubmed_papers(args.query)
    papers = fetch_paper_details(paper_ids)

    # If user provided a filename, save the results to that file
    if args.file:
        save_papers_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    elif args.debug:
    # Print debug information
        print("Debug mode enabled:")
        for paper in papers:
            print(f"DEBUG: {paper}")
    else:
    # Print the results to the console
        for paper in papers:
            print(paper)


# Entry point of the script
if __name__ == '__main__':
    main()
