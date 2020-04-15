#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


# In[2]:


wiki_url = "https://en.wikipedia.org/wiki/Genome"
wiki_data = urlopen(wiki_url)
wiki_html = wiki_data.read()
wiki_data.close()

page_soup = soup(wiki_html, "html.parser")


# In[3]:


print(page_soup)


# In[4]:


genome_table = page_soup.findAll("table", {"class": "wikitable sortable"})
print(genome_table)


# In[5]:


genome_table = genome_table[0]
headers = genome_table.findAll("th", {})
print(headers)


# In[7]:


header_titles = []
for header in headers:
    header_titles.append(header.text[:-1])
print(header_titles)


# In[9]:


all_rows = genome_table.findAll("tr", {})
print(all_rows)


# In[10]:


data = all_rows[1:]
print(data)


# In[11]:


""" first_row = data[0]
first_row_data = first_row('td', {})
print(first_row_data) """


# In[12]:

"""
data_texts = []
for data_text in first_row_data:
    data_texts.append(data_text.text[:-1])
print(data_texts) """


# In[13]:


table_rows = []
for row in data:
    row_data = row.findAll("td", {})
    table_row = []
    for data_point in row_data:
        table_row.append(data_point.text[:-1])
    table_rows.append(table_row)
print(table_rows)


# In[20]:


filename = "genome_table.csv"
f = open(filename, "w")
header_string = ""
for title in header_titles:
    header_string += title + ","
header_string = header_string[:-1]
header_string += "\n"
f.write(header_string)

for row in table_rows:
    row_string = ""
    for column in row:
        column_string = column.replace(",", "")
        row_string += column_string + ","
    row_string = row_string[:-1]
    row_string += "\n"
    f.write(row_string)


# In[21]:
# Read local file

filename = "Genome - Wikipedia.html"
f = open(filename)
new_soup = soup(f, "html.parser")
print(new_soup.h1)
