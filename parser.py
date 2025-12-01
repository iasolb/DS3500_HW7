"""
November 21, 2025

Parser File for processing text-based data sources

"""

from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import string
import plotly.graph_objects as go


class Parsnip:
    """
    Extensible framework for natural langauge processing and text analysis.
    Supports custom parsers and multiple visualization types.
    """

    def __init__(self):
        """Constructor to initialize state"""
        self.data = defaultdict(
            dict
        )  # Where all the data extracted from the loaded documents is stored
        self.stop_words = []

    def load_stop_words(self, filepath: str):
        """
        Load stop words from file
        """
        with open(filepath, "r") as file:
            dirty = file.readlines()
            self.stop_words = [word.replace("\n", "") for word in dirty]

    @staticmethod
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

    @staticmethod
    def default_parser(filename):
        """
        For processing plain text file (txt)
        """
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

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

    def load_text(self, filename, label=None, parser=None):
        """
        Register a text document with the framework.
        Extract and store data to be used later in our visualizations.
        """
        if parser is None:
            results = self.default_parser(filename)
        else:
            results = parser(filename)

        # Use filename for the label if none is provided
        if label is None:
            label = filename

        # Store the results for that ONE document into self.data
        # For example, document A:  numwords=10,  document B: numwords=20
        # For A, the results are: {numwords:10}, for B: {numwords:20}
        # This gets stored as: {numwords: {A:10, B:20}}

        for k, v in results.items():
            self.data[k][label] = v

        # Remove stop words from wordcount
        if self.stop_words and "wordcount" in results:
            filtered = Counter()
            for word, count in results["wordcount"].items():
                if word not in self.stop_words:
                    filtered[word] = count
            self.data["wordcount"][label] = filtered

    # Don't thing we need this
    #    def compare_num_words(self):
    #        """A very simplistic visualization that creates
    #        a bar chart comparing num words for each text file
    #        For HW7, I expect much more interesting visualizations"""
    #
    #        numwords = self.data["numwords"]
    #        for label, nw in numwords.items():
    #            plt.bar(label, nw)
    #       plt.show()

    def wordcount_sankey(self, word_list=None, k=5):
        """
        Create a Sankey diagram mapping texts to words
        word_list: optional list of words to show, or uses top k words
        k: number of top words to use from each text if word_list is None
        """

        # Get words to show
        if word_list is None:
            # Get the k top words from all sources combined
            all_words = set()
            for label, counter in self.data["wordcount"].items():
                top_k = [word for word, count in counter.most_common(k)]
                all_words.update(top_k)
            word_list = list(all_words)

        # Build Sankey
        labels = list(self.data["wordcount"].keys())
        nodes = labels + word_list

        # Create links
        sources = []
        targets = []
        values = []

        for i, label in enumerate(labels):
            counter = self.data["wordcount"][label]
            for word in word_list:
                count = counter.get(word, 0)
                if count > 0:
                    sources.append(i)
                    targets.append(len(labels) + word_list.index(word))
                    values.append(count)

        # Create fig
        fig = go.Figure(
            go.Sankey(
                node=dict(label=nodes),
                link=dict(source=sources, target=targets, value=values),
            )
        )

        fig.update_layout(title="Climate Change Reports: Word Frequency Flow Analysis")
        fig.show()
