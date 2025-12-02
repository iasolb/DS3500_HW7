"""
Custom Parsers for NLP Frameworks
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud

Domain-specific parsers for different file types
"""

from nltk.sem.chat80 import items
from collections import Counter
import string

def pdf_parser(filename):
    """
    Custom parser for PDF files.
    Extracts text from PDF and processes it.
    """
    try:
        import PyPDF2
    except ImportError:
        print("PyPDF2 not installed. Installing...")
        import subprocess

        subprocess.check_call(["pip", "install", "PyPDF2"])
        import PyPDF2

    # Read PDF
    with open(filename, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        # Extract text from all pages
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Clean the text: lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count words
    wordcount = Counter(words)
    numwords = len(words)

    results = {
        "wordcount": wordcount,
        "numwords": numwords,
    }

    print(f"Parsed {filename}: {numwords} words")
    return results

def json_parser(filename):
    """
    Custom parser for JSON files
    Expects JSON with eitehr a 'text' or 'content' field containing the text to analyze
    """
    import json

    # Read JSON file
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Extract text - look for common field names
    if isinstance(data, dict):
        text = data.get("text", data.get("content", data.get("body", '')))
    elif isinstance(data, list):
        # If it is a list of objects, concatenate all text fields
        text = ''.json([
            items.get("text", items.get("content", items.get("body", '')))
            for item in data if isinstance(item, dict)
        ])
    else:
        text = str(data)

    # Clean the text: lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count words
    wordcount = Counter(words)
    numwords = len(words)

    results = {
        "wordcount": wordcount,
        "numwords": numwords,
    }

    print(f"Parsed {filename}: {numwords} words")
    return results

def csv_parser(filename, text_column='text'):
    """
    Custom parser for CSV files
    Extracts and analyzes text from a specified column
    """

    import csv

    text_data = []

    # Read CSV file
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Extract text from specified column
        for row in reader:
            if text_column in row:
                text_data.append(row[text_column])

            # If specified column does not exist, try to find any text-like column
            elif not text_data:
                # Try column names
                for col_name in ['text', 'content', 'body', 'message', 'description']:
                    if col_name in row:
                        text_data.append(row[col_name])
                        break

    # Combine all text
    text = ' '.join(text_data)

    # Clean the text: lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count words
    wordcount = Counter(words)
    numwords = len(words)

    results = {
        "wordcount": wordcount,
        "numwords": numwords,
    }

    print(f"Parsed {filename}: {numwords} words")
    return results








