"""
Visualization Module for NLP Tasks
"""

import numpy as np
import matplotlib.pyplot as plt

class NatLanGraphs:

    def __init__(self):
        pass

    def text_to_word_sankey(self, parser, word_list=None, k=5):
        """
        (Specific) Text-to-Word Sankey diagram.
        Calls the parser's wordcount_sankey method
        """
        parser.wordcount_sankey(word_list=word_list, k=k)

    def word_frequency_bars(self, parser, top_n=10):
        """
        (Flexible) subplots showing top words for each doc
        One bar chart per doc
        """
        wordcounts = parser.data["wordcount"]
        num_docs = len(wordcounts)

        # Calculate grid size
        cols = int(np.ceil(np.sqrt(num_docs)))
        rows = int(np.ceil(num_docs / cols))

        fig, axes = plt.subplots(rows, cols, figsize=(5*cols, 4*rows))


        # Make axes a list if there is only one subplot
        if num_docs == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        # Plot each document
        for index, (label, counter) in enumerate(wordcounts.items()):
            top_words = counter.most_common(top_n)
            words = [word for word, count in top_words]
            count = [count for word, count in top_words]

            axes[index].barh(words, count)
            axes[index].set_title(label)
            axes[index].set_xlabel("Frequency")
            axes[index].invert_yaxis()

        # Hide extra subplots
        for index in range(num_docs, len(axes)):
            axes[index].set_visible(False)

        plt.suptitle(f'Top {top_n} Most Frequent Words Across Climate Change Reports (1970s-2023)')
        plt.tight_layout()
        plt.show()
        plt.show()

    def compare_word_counts(self, parser, words=None, top_k=10):
        """
        (Flexible) overlay comparison of word frequencies across all texts
        """
        wordcounts = parser.data["wordcount"]

        # Get words to compare
        if words is None:
            all_words = set()
            for label, counter in wordcounts.items():
                top = [word for word, count in counter.most_common(top_k)]
                all_words.update(top)
            words = list(all_words)[:top_k]

        # Get data
        labels = list(wordcounts.keys())
        x = np.arange(len(words))
        width = 0.8 / len(labels)

        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot bars for each doc
        for index, label in enumerate(labels):
            counts = [wordcounts[label].get(word, 0) for word in words]
            offset = (index - len(labels)/2) * width + width / 2
            ax.bar(x + offset, counts, width, label=label)

        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('Evolution of Climate Terminology: Word Frequency Comparison Across Decades')
        ax.set_xticks(x)
        ax.set_xticklabels(words, rotation=45, ha='right')
        ax.legend(title='Report', bbox_to_anchor=(1.05, 1), loc='upper left')


        plt.tight_layout()
        plt.show()


