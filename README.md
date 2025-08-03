Installation Steps
1.Install Python
Verify Python is Installed(python --version).
check pip is installed.
2.Run the Poetry Installer
python -m pip install poetry
Verify Poetry is Installed(poetry --version).


Folder Structure Creation
1.Create a New Project Folder
mkdir pubmed-fetcher
cd pubmed-fetcher
2.create a new Poetry project:
poetry new pubmed_fetcher --src
cd pubmed_fetcher
3.Install Required Libraries
poetry add requests click pandas
poetry add beautifulsoup4
pip install lxml

Steps to run the script
poetry run get-papers-list "cancer AND immunotherapy"







