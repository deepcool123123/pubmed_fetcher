import click
from pubmed_fetcher.fetcher import fetch_pubmed_data
from pubmed_fetcher.filters import filter_non_academic_authors
from pubmed_fetcher.utils import export_to_csv

@click.command()
@click.argument('query')
def main(query):
    """Fetch PubMed papers for a query and filter non-academic authors."""
    print(f"🔍 Searching PubMed for: {query}")
    papers = fetch_pubmed_data(query)

    print(f"🧪 Total papers fetched: {len(papers)}")
    filtered = [filter_non_academic_authors(p) for p in papers]
    filtered = [p for p in filtered if p]

    print(f"🏢 Non-academic papers found: {len(filtered)}")
    for paper in filtered:
        print(paper)

    export_to_csv(filtered)
    print("✅ Results saved to output.csv")
