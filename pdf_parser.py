"""
Custom parser for PDF files
"""

from collections import Counter
import string


def pdf_parser(filename):
    """
    Custom parser for PDF files.
    Extracts text from PDF and processes it.

    Args:
        filename: Path to the PDF file

    Returns:
        Dictionary with wordcount and numwords
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
