# SEOBS
# Overview
This script processes and analyzes data extracted from .tar files containing website snapshots and metadata. The script performs the following tasks:

# Extraction: Extracts contents from .tar files.
# Text and HTML Analysis: Analyzes the text and HTML content, extracting key elements like titles, headings, images, paragraphs, and list items.
# Text Metrics Calculation: Calculates various text metrics such as word counts, Functional Word Ratio (FWR), and Type-Token Ratio (TTR).
# Data Aggregation: Collects the analyzed data and writes it to a CSV file.
Directory Structure
# base_directory: The directory containing the .tar files and the extracted data. Each query is represented by a subdirectory.
# csv_file: The CSV file where the aggregated data is saved.
Key Functions
File Operations
# extract_tar_files(directory): Extracts all .tar files in the specified directory.
Text Processing
# count_FUNC_words(text): Counts words in the text excluding functional words.
# calculate_fwr(text, functional_words): Calculates the Functional Word Ratio (FWR).
# calculate_ttr(text): Calculates the Type-Token Ratio (TTR).
HTML Content Extraction
# read_dom_html(hit_dir): Reads the dom.html file from a directory.
# extract_html_title_word_count(dom_html): Extracts the title word count from the HTML.
# count_images_in_html(dom_html): Counts the number of image tags in the HTML.
# extract_headings_text(dom_html): Extracts text from all heading tags.
# extract_paragraph_text(dom_html): Extracts text from all paragraph tags.
# extract_list_items_text(dom_html): Extracts text from all list item tags.
# count_words_in_headings(dom_html, heading_level): Counts words in specific heading tags.
Data Aggregation
The main loop iterates through each query directory, processes the data, and writes the results to a CSV file.

# CSV Output
# The script generates a CSV file named all_queries_domains_with_ranks_and_snapshots.csv with the following columns:

# Query: The search query.
# Domain: The domain of the website.
# Rank: The rank of the domain in search results.
# Title: The title of the webpage.
# Title Word Count: The number of words in the title.
# Image Count: The number of images on the page.
# h1 Word Count: Word count for <h1> tags.
# h2 Word Count: Word count for <h2> tags.
# h3 Word Count: Word count for <h3> tags.
# h4 Word Count: Word count for <h4> tags.
# h5 Word Count: Word count for <h5> tags.
# h6 Word Count: Word count for <h6> tags.
# Total h Word Count: Total word count for all heading tags.
# FUNC Word Count: Count of non-functional words in headings.
# FWR: Functional Word Ratio for headings.
# TTR: Type-Token Ratio for headings.
# Paragraph FUNC Word Count: Count of non-functional words in paragraphs.
# Paragraph FWR: Functional Word Ratio for paragraphs.
# Paragraph TTR: Type-Token Ratio for paragraphs.
# List Item FUNC Word Count: Count of non-functional words in list items.
# List Item FWR: Functional Word Ratio for list items.
# List Item TTR: Type-Token Ratio for list items.
Notes
Ensure that the BeautifulSoup library is installed for HTML parsing.
The script handles errors gracefully and logs any issues encountered during the extraction or processing steps.
Make sure the directory paths are correctly set according to your file structure.
Usage
Setup: Place the script in the desired directory and set the paths accordingly.
Run: Execute the script to start the extraction and analysis process.
Output: The final CSV file will be generated in the specified location.
Search Engine Observatory Visualization
This HTML page provides a visual representation of the ranking of domains for different queries on Google over three different dates. It allows users to analyze and observe changes in search results over time.

# Key Features
# Query Selection: Choose a query from the dropdown list to display the top domains for that specific date.
# Domain Comparison: Compare domains across different dates to identify common domains and new entries.
# How to Use
# Select Query: Choose a query from the dropdown list under each chart to see the corresponding domain rankings.
# Compare Domains: Click the "Compare Domains" button to see common and new domains across the selected dates.
Technical Details
The page uses D3.js for rendering the bar charts.
The charts and data are dynamically updated based on user interactions.
The data is sourced from CSV files corresponding to different dates.
Notes
The visual representation includes color coding for better differentiation of domains.
The charts are designed to be responsive and adjust to various screen sizes.
CSS Styling
The page includes styling for the body, chart containers, chart titles, and navigation elements. Key style elements include:

Body: A light gray background with a monospace font.
# Chart Containers: White background with rounded corners and light shadow for depth.
# Navigation: A top navigation bar with links to different sections of the observatory.
JavaScript
The script includes functions for:

# Creating Charts: Setting up SVG elements, scales, and axes for the bar charts.
# Updating Charts: Updating the charts based on the selected query and sort options.
# Comparing Domains: Identifying and displaying common and unique domains across different datasets.
Data
The data for the charts is loaded from three CSV files, each representing a snapshot of domain rankings for a specific date.

This README provides a comprehensive overview of both the data processing script and the visualization page. 
For further customization or troubleshooting, refer to the individual function implementations within the respective files.
