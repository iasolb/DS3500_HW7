"""
NPL Framework - Core Module
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud
Group Name: The Parseltongues (Harry Potter reference :) )

Extensible framework for natural language processing and text analysis.
Supports custom parsers and multiple visualization types.
"""

from collections import Counter, defaultdict
import plotly.graph_objects as go
import string
import json
import matplotlib.pyplot as plt
import numpy as np


class Parsnip:
    """
    Extensible framework for natural language processing and text analysis.
    Supports custom parsers and multiple visualization types.
    """

    def __init__(self):
        """Constructor to initialize state"""
        self.data = defaultdict(dict)
        self.stop_words = []

    # === Data Init

    def load_stop_words(self, filepath: str):
        """
        Load stop words from file

        Args:
            filepath (str): Path to file containing stop words (one per line)
        """
        with open(filepath, "r") as file:
            dirty = file.readlines()
            self.stop_words = [word.replace("\n", "") for word in dirty]

    def load_text(self, filename, label=None, parser=None):
        """
        Register a text document with the framework.
        Extract and store data to be used later in our visualizations.

        Args:
            filename (str): Path to the file to load
            label: Optional label for identifying the text in visualizations
            parser: Optional custom parser function. If None, use_default_parser
        """
        if parser is None:
            results = self.default_parser(filename)
        else:
            results = parser(filename)

        # Use filename for the label if none is provided
        if label is None:
            label = filename

        # Store the results for that ONE document into self.data
        for k, v in results.items():
            self.data[k][label] = v

        # Remove stop words from wordcount
        if self.stop_words and "wordcount" in results:
            filtered = Counter()
            for word, count in results["wordcount"].items():
                if word not in self.stop_words:
                    filtered[word] = count
            self.data["wordcount"][label] = filtered

    # ==== Native Parsers

    @staticmethod
    def default_parser(filename):
        """
        Default parser for processing plain text file (txt)

        Args:
            filename (str): Path to plain text file

        Returns:
            Dictionary containing wordcount and numwords
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

    def pdf_parser(self, filename):
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

        with open(filename, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

        # Clean the text: lowercase and remove punctuation
        text = text.lower()
        text = "".join(char for char in text if char.isalpha() or char.isspace())
        words = text.split()

        wordcount = Counter(words)
        numwords = len(words)

        results = {
            "wordcount": wordcount,
            "numwords": numwords,
        }

        print(f"Parsed {filename}: {numwords} words")
        return results

    def csv_parser(self, filename, text_column="text"):
        """
        Custom parser for CSV files
        Extracts and analyzes text from a specified column
        """

        import csv

        text_data = []

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if text_column in row:
                    text_data.append(row[text_column])

                elif not text_data:
                    for col_name in [
                        "text",
                        "content",
                        "body",
                        "message",
                        "description",
                    ]:
                        if col_name in row:
                            text_data.append(row[col_name])
                            break

        text = " ".join(text_data)

        # Clean the text: lowercase and remove punctuation
        text = text.lower()
        text = "".join(char for char in text if char.isalpha() or char.isspace())
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


    def json_parser(self, filename, text_key="text"):
        """
        Custom parser for JSON files
        Expects JSON with a text field

        Args:
            filename (str): Path to JSON file
            text_key (str): Key in JSON containing text (default: "text")

        Returns:
            Dictionary containing wordcount and numwords
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                raw = json.load(f)
                text = raw[text_key]

                # Clean the text: lowercase and remove punctuation
                text = text.lower()
                text = "".join(char for char in text if char.isalpha() or char.isspace())
                words = text.split()

                wordcount = Counter(words)
                numwords = len(words)

                results = {
                    "wordcount": wordcount,
                    "numwords": numwords,
                }

                print(f"Parsed {filename}: {numwords} words")
                return results
        except KeyError:
            print(f"Error: JSON file {filename} does not contain '{text_key}' field")
            return {"wordcount": Counter(), "numwords": 0}
        except json.JSONDecodeError:
            print(f"Error: {filename} is not valid JSON")
            return {"wordcount": Counter(), "numwords": 0}
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            return {"wordcount": Counter(), "numwords": 0}

    # ==== Visualization

    def word_frequency_bars(self, word_list=None, top_n=10, title=None):
        """
        Create a grid of horizontal bar charts showing top N most frequent words for each document.

        Args:
            word_list: Optional list of specific words to display. If None, shows top_n words
            top_n: Number of top words to display for each document (default: 10)
            title: Custom title for the overall figure (default: generic title based on top_n)
        """
        wordcounts = self.data["wordcount"]
        num_docs = len(wordcounts)
        cols = int(np.ceil(np.sqrt(num_docs)))
        rows = int(np.ceil(num_docs / cols))
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
        if num_docs == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        for index, (label, counter) in enumerate(wordcounts.items()):
            # If word_list is provided, use it; otherwise get top_n words
            if word_list is not None:

                # Filter to only words that exist in this document's counter
                words = [word for word in word_list if word in counter]
                count = [counter[word] for word in words]
            else:
                top_words = counter.most_common(top_n)
                words = [word for word, count in top_words]
                count = [count for word, count in top_words]

            axes[index].barh(words, count)
            axes[index].set_title(label)
            axes[index].set_xlabel("Frequency")
            axes[index].invert_yaxis()
        for index in range(num_docs, len(axes)):
            axes[index].set_visible(False)

        # Use custom title if provided, otherwise use default
        if title is None:
            title = f"Top {top_n} Most Frequent Words Across Documents"
        plt.suptitle(title)
        plt.tight_layout()
        plt.show()

    def wordcount_sankey(self, word_list=None, k=5, title="Text to Word Flow Analysis"):
        """
        Create a Sankey diagram mapping texts to words

        Args:
            word_list: Optional list of  specific words to show
            k: Number of top words to use from each text if word_list is None
            title: Title for the Sankey diagram (default: 'Text to Word Flow Analysis')
        """

        # Get words to show
        if word_list is None:
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

        fig.update_layout(title=title)
        fig.show()

    def compare_word_counts(self, word_list=None, top_k=10, title="Word Frequency Comparison"):
        """
        Overlay comparison of word frequencies across all texts.
        Creates a grouped bar chart comparing word usage across documents.

        Args:
            word_list: Optional list of specific words to compare
            top_k: Number of top words to compare if word_list is None
            title: Custom title for the chart (default: "Word Frequency Comparison")
        """
        wordcounts = self.data["wordcount"]

        if word_list is None:
            # Combine all counters to get overall top words
            combined_counter = Counter()
            for label, counter in wordcounts.items():
                combined_counter.update(counter)

            # Get the top_k most common words from the combined corpus
            word_list = [word for word, count in combined_counter.most_common(top_k)]

        labels = list(wordcounts.keys())
        x = np.arange(len(word_list))
        width = 0.8 / len(labels)
        fig, ax = plt.subplots(figsize=(12, 6))

        for index, label in enumerate(labels):
            counts = [wordcounts[label].get(word, 0) for word in word_list]
            offset = (index - len(labels) / 2) * width + width / 2
            ax.bar(x + offset, counts, width, label=label)

        ax.set_xlabel("Words")
        ax.set_ylabel("Frequency")
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(word_list, rotation=45, ha="right")
        ax.legend(title="Documents", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
        plt.show()

    def word_trend_over_time(self, word_list=None, top_k=5, title="Word Frequency Trends Over Time"):
        """
        Track how specific words change in frequency across documents.
        Best used with temporally ordered documents.

        Args:
            word_list: Optional list of specific words to track. If None, uses top_k most common words
            top_k: Number of top words to track if word_list is None (default: 5)
            title: Custom title for the chart
        """
        wordcounts = self.data["wordcount"]
        labels = list(wordcounts.keys())

        # If word_list not provided, get top words from combined corpus
        if word_list is None:
            combined_counter = Counter()
            for counter in wordcounts.values():
                combined_counter.update(counter)
            word_list = [word for word, count in combined_counter.most_common(top_k)]

        plt.figure(figsize=(12, 6))

        for word in word_list:
            frequencies = [wordcounts[label].get(word, 0) for label in labels]
            plt.plot(range(len(labels)), frequencies, marker='o', linewidth=2,
                     markersize=6, label=word)

        plt.xlabel("Timeline", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.title(title, fontsize=14)
        plt.xticks(range(len(labels)), labels, rotation=45, ha="right")
        plt.legend(loc="best", fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
