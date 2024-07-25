import os
import tarfile
import json
import csv
from bs4 import BeautifulSoup

# Directory containing .tar files
directory = r'C:\Users\zikaa\Desktop\SEO\new code\tar 24.6.2024'

# List all files in the directory
files = os.listdir(directory)

# Filter only .tar files
tar_files = [file for file in files if file.endswith('.tar')]

# Extract all .tar files
for tar_filename in tar_files:
    try:
        with tarfile.open(os.path.join(directory, tar_filename), 'r') as tar:
            tar.extractall(path=directory)
    except PermissionError as e:
        print(f"PermissionError while extracting {tar_filename}: {e}")
    except Exception as e:
        print(f"Error while extracting {tar_filename}: {e}")

ENGLISH_FUNC_WORDS = set([
    'the', 'is', 'in', 'at', 'which', 'on', 'and', 'a', 'to', 'of',
    'it', 'that', 'for', 'you', 'with', 'as', 'have', 'be', 'this',
    'by', 'not', 'or', 'are', 'from', 'but', 'an', 'if', 'will',
    'can', 'all', 'has', 'we', 'do', 'their', 'one', 'about', 'would',
    'there', 'been', 'when', 'who', 'they', 'more', 'no', 'up', 'out',
    'so', 'said', 'what', 'which', 'its', 'than', 'into', 'them', 'some',
    'could', 'other', 'then', 'only', 'new', 'these', 'two', 'may', 'first',
    'any', 'like', 'now', 'my', 'such', 'because', 'how', 'our', 'over',
    'also', 'after', 'even', 'most', 'many', 'those', 'here', 'where', 'why'
])

def count_FUNC_words(text):
    words = [word.strip() for word in text.split()]
    words = [word for word in words if word.lower() not in ENGLISH_FUNC_WORDS]
    word_count = len(words)
    return word_count

def calculate_fwr(text, functional_words):
    words = [word.strip() for word in text.split()]
    total_words = len(words)
    func_words_count = sum(1 for word in words if word.lower() in functional_words)
    fwr = func_words_count / total_words if total_words > 0 else 0
    return fwr

def calculate_ttr(text):
    words = [word.strip() for word in text.split()]
    token_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    ttr = unique_word_count / token_count if token_count > 0 else 0
    return ttr

def get_query_text(query_dir):
    query_file = os.path.join(query_dir, 'query.txt')
    if os.path.exists(query_file):
        with open(query_file, 'r') as f:
            query_text = f.read().strip()
            return query_text
    return None

def read_dom_html(hit_dir):
    dom_html_file = os.path.join(hit_dir, 'snapshot', 'dom.html')
    if os.path.exists(dom_html_file):
        with open(dom_html_file, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def extract_html_title_word_count(dom_html):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        title_tag = soup.title
        if title_tag and title_tag.string:
            title_text = title_tag.string.strip()
            word_count = len(title_text.split())
            return word_count
    return 0

def count_images_in_html(dom_html):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        img_tags = soup.find_all('img')
        return len(img_tags)
    return 0

def extract_headings_text(dom_html):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        headings_text = ' '.join([heading.get_text(strip=True) for heading in headings])
        return headings_text
    return ''

def extract_paragraph_text(dom_html):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraph_text = ' '.join([paragraph.get_text(strip=True) for paragraph in paragraphs])
        return paragraph_text
    return ''

def extract_list_items_text(dom_html):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        list_items = soup.find_all('li')
        list_items_text = ' '.join([li.get_text(strip=True) for li in list_items])
        return list_items_text
    return ''

def count_words_in_headings(dom_html, heading_level):
    if dom_html:
        soup = BeautifulSoup(dom_html, 'html.parser')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        total_word_count = 0
        for heading in headings:
            if heading.name == heading_level:
                heading_text = heading.get_text(strip=True)
                word_count = len(heading_text.split())
                total_word_count += word_count
        return total_word_count
    return 0

base_directory = r'C:\Users\zikaa\Desktop\SEO\new code\tar 24.6.2024'
queries = os.listdir(base_directory)

# CSV file to store all data
csv_file = "all_queries_domains_with_ranks_and_snapshots.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Query', 'Domain', 'Rank', 'Title', 'Title Word Count', 'Image Count', 'h1 Word Count', 'h2 Word Count', 'h3 Word Count', 'h4 Word Count', 'h5 Word Count', 'h6 Word Count', 'Total h Word Count', 'FUNC Word Count', 'FWR', 'TTR', 'Paragraph FUNC Word Count', 'Paragraph FWR', 'Paragraph TTR', 'List Item FUNC Word Count', 'List Item FWR', 'List Item TTR'])

    for query in queries:
        query_dir = os.path.join(base_directory, query)
        if os.path.isdir(query_dir):
            query_text = get_query_text(query_dir)
            if query_text:
                main_domains = []

                def extract_domains_from_config(config_file, rank):
                    try:
                        with open(config_file) as f:
                            config_data = json.load(f)
                            url = config_data.get('url')
                            if url:
                                snapshot = read_dom_html(os.path.dirname(config_file))
                                title = extract_html_title_word_count(snapshot)
                                main_domains.append((url, rank, snapshot, title))
                    except PermissionError as e:
                        print(f"PermissionError while reading {config_file}: {e}")
                    except Exception as e:
                        print(f"Error while reading {config_file}: {e}")

                hits = os.listdir(query_dir)
                for i, hit in enumerate(hits):
                    hit_dir = os.path.join(query_dir, hit)
                    if os.path.isdir(hit_dir):
                        config_file = os.path.join(hit_dir, 'config.json')
                        if os.path.exists(config_file):
                            extract_domains_from_config(config_file, i+1)

                main_domains = list(set(main_domains))
                main_domains.sort(key=lambda  x: x[1])

                for domain, rank, snapshot, title in main_domains:
                    try:
                        title_word_count = extract_html_title_word_count(snapshot)
                        image_count = count_images_in_html(snapshot)
                        h1_word_count = count_words_in_headings(snapshot, 'h1')
                        h2_word_count = count_words_in_headings(snapshot, 'h2')
                        h3_word_count = count_words_in_headings(snapshot, 'h3')
                        h4_word_count = count_words_in_headings(snapshot, 'h4')
                        h5_word_count = count_words_in_headings(snapshot, 'h5')
                        h6_word_count = count_words_in_headings(snapshot, 'h6')
                        total_h_word_count = h1_word_count + h2_word_count + h3_word_count + h4_word_count + h5_word_count + h6_word_count
                        
                        # Extract the actual text content from headings, paragraphs, and list items
                        headings_text = extract_headings_text(snapshot)
                        paragraph_text = extract_paragraph_text(snapshot)
                        list_items_text = extract_list_items_text(snapshot)
                        
                        # Calculate FUNC Word Count, FWR, and TTR for the actual headings text
                        func_word_count = count_FUNC_words(headings_text)
                        fwr = calculate_fwr(headings_text, ENGLISH_FUNC_WORDS)
                        ttr = calculate_ttr(headings_text)
                        
                        # Calculate FUNC Word Count, FWR, and TTR for paragraphs
                        paragraph_func_word_count = count_FUNC_words(paragraph_text)
                        paragraph_fwr = calculate_fwr(paragraph_text, ENGLISH_FUNC_WORDS)
                        paragraph_ttr = calculate_ttr(paragraph_text)
                        
                        # Calculate FUNC Word Count, FWR, and TTR for list items
                        list_items_func_word_count = count_FUNC_words(list_items_text)
                        list_items_fwr = calculate_fwr(list_items_text, ENGLISH_FUNC_WORDS)
                        list_items_ttr = calculate_ttr(list_items_text)
                        
                        writer.writerow([query_text, domain, rank, title, title_word_count, image_count, h1_word_count, h2_word_count, h3_word_count, h4_word_count, h5_word_count, h6_word_count, total_h_word_count, func_word_count, fwr, ttr, paragraph_func_word_count, paragraph_fwr, paragraph_ttr, list_items_func_word_count, list_items_fwr, list_items_ttr])
                    except PermissionError as e:
                        print(f"PermissionError while processing domain {domain} in query {query_text}: {e}")
                    except Exception as e:
                        print(f"Error while processing domain {domain} in query {query_text}: {e}")
                
                print(f"Data for query '{query_text}' has been added to the CSV file.")
            else:
                print(f"Query text not found for query '{query}'.")

print(f"CSV file '{csv_file}' has been created successfully with data from all queries.")
