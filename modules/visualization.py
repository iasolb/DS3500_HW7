"""
Visualization Module for NLP Tasks
"""


class NatLanGraphs:
    def __init__(self):
        pass

    def text_to_word_sankey(self, data):
        """
        (Specific) Text-to-Word Sankey diagram. Given the loaded texts and either a
        set of user-defined words OR the set of words drawn from the k most
        common words of each text file, generate a Sankey diagram from text name
        to word, where the thickness of the connection represents the wordcount of
        that word in the specified text
        """
        pass

    def subplots(self, data):
        """
        (Flexible) Any type of visualization containing sub-plots, one sub-plot for
        each text file. For example, an array of word clouds, one for each text file
        would satisfy this requirement, although I’m not a huge fan of word clouds
        """
        pass

    def plot_comparison(self, data):
        """
        (Flexible) Any type of comparative visualization that overlays information
        from each text file onto a single plot.
        """
        pass
