def filter_non_academic_authors(paper):
    company_keywords = ["Inc", "Ltd", "LLC", "Corp", "Biotech", "Pharma", "Technologies", "Labs", "Company"]
    non_academic_authors = []

    for author in paper["Authors"]:
        affiliation = author.get("affiliation", "")
        if any(keyword in affiliation for keyword in company_keywords):
            non_academic_authors.append(author)

    if not non_academic_authors:
        return None

    return {
        "PubmedID": paper["PubmedID"],
        "Title": paper["Title"],
        "Publication Date": paper["Publication Date"],
        "Non-academic Author(s)": ", ".join([a["name"] for a in non_academic_authors]),
        "Company Affiliation(s)": "; ".join([a["affiliation"] for a in non_academic_authors]),
        "Corresponding Author Email": non_academic_authors[0].get("email", "N/A")
    }
