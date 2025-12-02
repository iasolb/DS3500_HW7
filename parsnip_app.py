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
        "data/2000_DotCom_Era.pdf",
        label="2000: Dot-Com Era",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2003_Amazon_Recovery.pdf",
        label="2003: Amazon Recovery",
        parser=pdf_parser,
    )


    parser.load_text(
        "data/2006_Amazon_AWSLaunch.pdf",
        label="2006: Amazon AWS Launch",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2010_Amazon_DigitalProducts.pdf",
        label="2010: Amazon Digital Products",
        parser=pdf_parser,
    )


    parser.load_text(
        "data/2014_Amazon_VoiceAI.pdf",
        label="2014: Amazon Voice AI",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2018_Amazon_MarketLeader.pdf",
        label="2018: Amazon Market Leader",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2021_Amazon_PandemicPeak.pdf",
        label="2021: Amazon Pandemic Peak",
        parser=pdf_parser,
    )

    parser.load_text(
        "data/2024_Amazon_AI_Integration.pdf",
        label="2024: Amazon AI Integration",
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
