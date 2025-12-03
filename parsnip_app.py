"""
Application: Climate Change Report Analysis
DS 3500: Advance Programming with Data
Members: Amir Sesay, Cassandra Cinzori, Ian Solberg, Iyman Mahmoud

This application demonstrates the evolution of the language used in Q4 earnings reports/calls issued by
Amazon between 2000 and 2024.
"""

from parsnip import Parsnip


def main():
    parsnip = Parsnip()

    # Load stop words (stop words tailored to dataset)
    print("Loading stop words...")
    parsnip.load_stop_words("data/stopwords.txt")

    # Load text files
    print("\nLoading documents...")

    parsnip.load_text(
        "data/2000_DotCom_Era.pdf",
        label="2000: Dot-Com Era",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2003_Amazon_Recovery.pdf",
        label="2003: Amazon Recovery",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2006_Amazon_AWSLaunch.pdf",
        label="2006: Amazon AWS Launch",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2010_Amazon_DigitalProducts.pdf",
        label="2010: Amazon Digital Products",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2014_Amazon_VoiceAI.pdf",
        label="2014: Amazon Voice AI",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2018_Amazon_MarketLeader.pdf",
        label="2018: Amazon Market Leader",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2021_Amazon_PandemicPeak.pdf",
        label="2021: Amazon Pandemic Peak",
        parser=parsnip.pdf_parser,
    )

    parsnip.load_text(
        "data/2024_Amazon_AI_Integration.pdf",
        label="2024: Amazon AI Integration",
        parser=parsnip.pdf_parser,
    )

    print("=" * 60)
    print("Generating Visualizations")
    print("=" * 60)

    print("\nCreating Sankey diagram...")
    parsnip.text_to_word_sankey(
        k=5, title="Climate Change Reports: Word Frequency Analysis"
    )

    print("\nCreating words frequency subplots...")
    parsnip.word_frequency_bars(
        top_n=10,
        title="Top 10 Most Frequent Words Across Climate Change Reports (1970s-2023)",
    )

    print("\nCreating comparison chart...")
    parsnip.compare_word_counts(
        top_k=10,
        title="Evolution of Climate Terminology: Word Frequency Comparison Across Decades",
    )

    print("=" * 60)
    print("\nDone!!")
    print("=" * 60)


if __name__ == "__main__":
    main()
