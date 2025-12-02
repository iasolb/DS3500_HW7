"""
Application: Climate Change Report Analysis
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud

This application demonstrates the Parsnip NLP framework by analyzing
8 landmark climate change documents spanning from 1979 to 2023.
"""

from parsnip import Parsnip
from parsnip_parsers import pdf_parser
from parsnip_visuals import NatLanGraphs


def main():
    parser = Parsnip()
    grapher = NatLanGraphs()

    # Load stop words
    print("Loading stop words...")
    parser.load_stop_words("data/stopwords.txt")

    # Load text files
    print("\nLoading documents...")

    parser.load_text(
        "data/charney_report.pdf",
        label="1979: Charney Report",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/NASA_Hansen_Testimony.pdf",
        label="1988: NASA Hansen Testimony ",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/First_IPCC_Report.pdf",
        label="1990: First IPCC Report",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/Kyoto_Protocol_Text.pdf",
        label="1997: Kyoto Protocol Text",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/Stern_Review.pdf",
        label="2006: Stern Review",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/Paris_agreement.pdf",
        label="2015: Paris Agreement",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/IPCC_Special_Report.pdf",
        label="2018: IPCC Special Report",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2023_IPCC_AR6_Report.pdf",
        label="2023: IPCC AR6 Synthesis Report",
        parser=pdf_parser,
    )

    # Create visuals
    print("=" * 60)
    print("Generating Visualizations")
    print("=" * 60)

    print("\nCreating Sankey diagram...")
    grapher.text_to_word_sankey(
        parser,
        k=5,
        title="Climate Change Reports: Word Frequency Analysis")

    print("\nCreating words frequency subplots...")
    grapher.word_frequency_bars(
        parser,
        top_n=10,
        title="Top 10 Most Frequent Words Across Climate Change Reports (1970s-2023)")

    print("\nCreating comparison chart...")
    grapher.compare_word_counts(
        parser,
        top_k=10,
        title="Evolution of Climate Terminology: Word Frequency Comparison Across Decades")

    print("=" * 60)
    print("\nDone!!")
    print("=" * 60)

if __name__ == "__main__":
    main()
