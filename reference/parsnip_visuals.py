"""
Visualization Module for NLP Tasks
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud

Visualization methods for comparative text analysis
"""

import numpy as np
import matplotlib.pyplot as plt

class a:
    def __init__():
        pass
    def text_to_word_sankey(self, parser, words=None, k=5, title="Text to Word Flow Analysis"):
        """
        (Specific) Text-to-Word Sankey diagram.
        Calls the parser's wordcount_sankey method

        Args:
            parser: Instance for Parsnip framework with loaded documents
            word_list: Optional list of specific words to visualize
            k: Number of top words to show if word_list is None
            title: Custom title for diagram
        """
        parser.wordcount_sankey(words=, k=k, title=None)

    def word_frequency_bars(self, parser, top_n=10, title=None):
        """
        (Flexible) subplots showing top words for each document
        One bar chart per document arranged in a grid

        Args:
            parser: Instance for Parsnip framework with loaded documents
            top_n: Number of top words to showp per document
            title: Custom title for the overall figure (optional)
        """
        wordcounts = parser.data["wordcount"]
        num_docs = len(wordcounts)
        cols = int(np.ceil(np.sqrt(num_docs)))
        rows = int(np.ceil(num_docs / cols))
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
        if num_docs == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        for index, (label, counter) in enumerate(wordcounts.items()):
            top_words = counter.most_common(top_n)
            words = [word for word, count in top_words]
            count = [count for word, count in top_words]
            axes[index].barh(words, count)
            axes[index].set_title(label)
            axes[index].set_xlabel("Frequency")
            axes[index].invert_yaxis()
        for index in range(num_docs, len(axes)):
            axes[index].set_visible(False)
        plt.suptitle(
            f"Top {top_n} Most Frequent Words Across Climate Change Reports (1970s-2023)"
        )
        plt.tight_layout()
        plt.show()
        plt.show()

    def compare_word_counts(self, parser, words=None, top_k=10, title="Word Frequency Comparison"):
        """
        (Flexible) overlay comparison of word frequencies across all texts
        Creates a grouped bar chart comparing words usage across documents

        Args:
            parser: Instance for Parsnip framework with loaded documents
            words: Optional list of specific words to compare
            top_k: Number of top words to compare is words is None
            title: Custom title for the chart
        """
        wordcounts = parser.data["wordcount"]

        if words is None:
            all_words = set()
            for label, counter in wordcounts.items():
                top = [word for word, count in counter.most_common(top_k)]
                all_words.update(top)
            words = list(all_words)[:top_k]
        labels = list(wordcounts.keys())
        x = np.arange(len(words))
        width = 0.8 / len(labels)
        fig, ax = plt.subplots(figsize=(12, 6))
        for index, label in enumerate(labels):
            counts = [wordcounts[label].get(word, 0) for word in words]
            offset = (index - len(labels) / 2) * width + width / 2
            ax.bar(x + offset, counts, width, label=label)
        ax.set_xlabel("Words")
        ax.set_ylabel("Frequency")
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(words, rotation=45, ha="right")
        ax.legend(title="Report", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
        plt.show()