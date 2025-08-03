import requests
from bs4 import BeautifulSoup

def fetch_pubmed_data(query, max_results=10):
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    search_res = requests.get(esearch_url, params=params).json()
    ids = search_res.get("esearchresult", {}).get("idlist", [])

    if not ids:
        return []

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }

    fetch_res = requests.get(efetch_url, params=fetch_params)
    soup = BeautifulSoup(fetch_res.content, "lxml")

    articles = []

    for article in soup.find_all("pubmedarticle"):
        pmid = article.pmid.get_text()
        title = article.find("articletitle").get_text() if article.find("articletitle") else "N/A"
        pub_date_tag = article.find("pubdate")
        pub_date = pub_date_tag.get_text(strip=True) if pub_date_tag else "N/A"

        authors_info = []
        for author in article.find_all("author"):
            name = author.find("lastname")
            affiliation = author.find("affiliation")
            email = None
            if affiliation and "@" in affiliation.get_text():
                email = affiliation.get_text().split()[-1]
            authors_info.append({
                "name": name.get_text() if name else "N/A",
                "affiliation": affiliation.get_text() if affiliation else "N/A",
                "email": email
            })

        articles.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Authors": authors_info
        })

    return articles
