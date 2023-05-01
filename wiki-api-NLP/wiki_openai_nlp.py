# -*- coding: utf-8 -*-
"""Wiki-openAI-NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WoigAzGRVLgSkona6-xLM7lI0GdWFvlC
"""

pip install openai

import openai

openai.api_key="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"

pip install wikipedia-api

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page('2022 FIFA World Cup')

    page_py

"""How To Check If Wiki Page Exists"""

page_py =wiki_wiki.page('2022 FIFA World Cup')
print("page - Exist: %s" % page_py.exists())

page_missing =wiki_wiki.page('Osanda Lelum')
print("page- exists : %s" % page_missing.exists())

"""How to get Page Summary"""

wiki_wiki = wikipediaapi.Wikipedia('en')
 print("Page - Title : %s" % page_py.title)
 print("Page - summary : %s" page_py.summary[0:60])

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Python (programming language)')

print("Page - Title : %s" % page_py.title)
print("Page - summary : %s" % page_py.summary[0:60])

SECTIONS_TO_IGNORE =[
    "See also",
    "Photos"

]

def get_sections(
          section: wikipediaapi.WikipediaPageSection,
          parent_title: list[str],
          sections_to_ignore: set[str] = SECTIONS_TO_IGNORE,
      ) -> list[tuple[list[str],str]]:
 
  """Gather sections and subsections data."""

  sect_title = section.title 
  title = parent_title
  title.extend([sect_title])
  results = []
  
  if sect_title not in sections_to_ignore:
    sect_text = section.text   
    string_section = ( title , sect_text)
    results.extend([string_section])
    if len(section.sections)>1:
      for subsection in section.sections:
        get_sections(subsection, title, sections_to_ignore)     
  return results

def get_pages (
            page: wikipediaapi.WikipediaPage,
            sections_to_ignore: set[str] = SECTIONS_TO_IGNORE,
        )-> list[tuple[list[str],str]]:

    """Gather the page information: title and summary, and then go deep in sections inforamtion."""

    parent_title = page.title
    print(f"parent_title = {parent_title} ")

    summary = page.summary
    string_parent = ([parent_title], summary)
    results=[string_parent]

    if len(page.sections) > 0:
      for section in page.sections:
        results.extend(get_sections(section,[parent_title]))

    return results

wiki =wikipediaapi.Wikipedia('en')
CATEGORY_TITLE = "Category:2022 FIFA World Cup"

cat=wiki.page(CATEGORY_TITLE)

print("Name",cat.categorymembers)

articles = [w for w in cat.categorymembers.values() if w.ns == wikipediaapi.Namespace.MAIN]

wiki_corpus=[]
for page in articles:
  wiki_corpus.extend(get_pages(page))
wiki_corpus[:5]