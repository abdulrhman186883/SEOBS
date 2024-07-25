# SEOBS

# Overview
This script processes and analyzes data extracted from .tar files containing website snapshots and metadata. The script performs the following tasks:

Extraction: Extracts contents from .tar files.
Text and HTML Analysis: Analyzes the text and HTML content, extracting key elements like titles, headings, images, paragraphs, and list items.
Text Metrics Calculation: Calculates various text metrics such as word counts, Functional Word Ratio (FWR), and Type-Token Ratio (TTR).
Data Aggregation: Collects the analyzed data and writes it to a CSV file.
Directory Structure
base_directory: The directory containing the .tar files and the extracted data. Each query is represented by a subdirectory.
csv_file: The CSV file where the aggregated data is saved.
Key Functions
File Operations

extract_tar_files(directory): Extracts all .tar files in the specified directory.
Text Processing

count_FUNC_words(text): Counts words in the text excluding functional words.
calculate_fwr(text, functional_words): Calculates the Functional Word Ratio (FWR).
calculate_ttr(text): Calculates the Type-Token Ratio (TTR).
HTML Content Extraction

read_dom_html(hit_dir): Reads the dom.html file from a directory.
extract_html_title_word_count(dom_html): Extracts the title word count from the HTML.
count_images_in_html(dom_html): Counts the number of image tags in the HTML.
extract_headings_text(dom_html): Extracts text from all heading tags.
extract_paragraph_text(dom_html): Extracts text from all paragraph tags.
extract_list_items_text(dom_html): Extracts text from all list item tags.
count_words_in_headings(dom_html, heading_level): Counts words in specific heading tags.
Data Aggregation

The main loop iterates through each query directory, processes the data, and writes the results to a CSV file.
CSV Output
The script generates a CSV file named all_queries_domains_with_ranks_and_snapshots.csv with the following columns:

# Query: The search query.
Domain: The domain of the website.
Rank: The rank of the domain in search results.
Title: The title of the webpage.
Title Word Count: The number of words in the title.
Image Count: The number of images on the page.
h1 Word Count: Word count for <h1> tags.
h2 Word Count: Word count for <h2> tags.
h3 Word Count: Word count for <h3> tags.
h4 Word Count: Word count for <h4> tags.
h5 Word Count: Word count for <h5> tags.
h6 Word Count: Word count for <h6> tags.
Total h Word Count: Total word count for all heading tags.
FUNC Word Count: Count of non-functional words in headings.
FWR: Functional Word Ratio for headings.
TTR: Type-Token Ratio for headings.
Paragraph FUNC Word Count: Count of non-functional words in paragraphs.
Paragraph FWR: Functional Word Ratio for paragraphs.
Paragraph TTR: Type-Token Ratio for paragraphs.
List Item FUNC Word Count: Count of non-functional words in list items.
List Item FWR: Functional Word Ratio for list items.
List Item TTR: Type-Token Ratio for list items.
Notes
Ensure that the BeautifulSoup library is installed for HTML parsing.
The script handles errors gracefully and logs any issues encountered during the extraction or processing steps.
Make sure the directory paths are correctly set according to your file structure.
Usage
Setup: Place the script in the desired directory and set the paths accordingly.
Run: Execute the script to start the extraction and analysis process.
Output: The final CSV file will be generated in the specified location.
This README provides a detailed overview of the script's functionality and usage. For further customization or error handling, refer to the script's individual function implementations.
