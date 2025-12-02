"""
NPL Framework - Core Module
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud

Extensible framework for natural language processing and text analysis.
Supports custom parsers and multiple visualization types.
"""

from collections import Counter, defaultdict
import plotly.graph_objects as go
import string


class Parsnip:
    """
    Extensible framework for natural language processing and text analysis.
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

        Args:
            filepath (str): Path to file containing stop words (one per line)
        """
        with open(filepath, "r") as file:
            dirty = file.readlines()
            self.stop_words = [word.replace("\n", "") for word in dirty]

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

        fig.update_layout(title=title)
        fig.show()
