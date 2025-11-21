"""
November 21, 2025

Parser File for processing text-based data sources

"""

from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd


class ParserName:

    def __init__(self):
        """Constructor to initialize state"""

        self.grapher = None
        self.data = defaultdict(
            dict
        )  # Where all the data extracted from the loaded documents is stored

        self.stop_words = None

    @staticmethod
    def default_parser(filename):
        """For processing plain text files (.txt)"""
        results = {
            "wordcount": Counter("to be or not to be".split(" ")),
            "numwords": rnd.randrange(10, 50),
        }

        print("Parsed ", filename, ": ", results)
        return results

    def load_text(self, filename, label=None, parser=None):
        """Register a text document with the framework.
        Extract and store data to be used later in our visualizations."""
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

    def load_stop_words(self, filepath: str):
        with open(filepath, "r") as file:
            dirty = file.readlines()
            self.stop_words = [word.replace("\n", "") for word in dirty]

    def compare_num_words(self):
        """A very simplistic visualization that creates
        a bar chart comparing num words for each text file
        For HW7, I expect much more interesting visualizations"""

        numwords = self.data["numwords"]
        for label, nw in numwords.items():
            plt.bar(label, nw)
        plt.show()
