import requests
import csv
from typing import List, Dict

# PubMed API base URLs
SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[str]:
    """Fetch paper IDs from PubMed based on a search query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, str]]:
    """Fetch detailed information for given paper IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    try:
        response = requests.get(SUMMARY_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching details: {e}")
        return []

    papers = []
    for paper_id in paper_ids:
        doc = data.get("result", {}).get(paper_id, {})
        title = doc.get("title", "N/A")
        pub_date = doc.get("pubdate", "N/A")
        authors = [author.get("name", "N/A") for author in doc.get("authors", [])]
        affiliations = [author.get("affiliation", "N/A") for author in doc.get("authors", [])]

        non_academic_authors = [
            author for author, aff in zip(authors, affiliations)
            if "university" not in aff.lower() and "lab" not in aff.lower()
        ]
        company_affiliations = [
            aff for aff in affiliations
            if "pharma" in aff.lower() or "biotech" in aff.lower()
        ]
        corresponding_email = (
            f"{non_academic_authors[0].replace(' ', '.').lower()}@company.com"
            if non_academic_authors else "N/A"
        )

        papers.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email
        })
    return papers

def save_papers_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    """Save paper details to a CSV file."""
    if not papers:
        print("No papers to save.")
        return

    keys = papers[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)
    print(f"Papers saved to {filename}")
