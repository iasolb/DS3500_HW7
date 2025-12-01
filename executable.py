"""
Main executable for NLP framework
"""

from parser import Parsnip
from visualization import NatLanGraphs


def main():
    parser = Parsnip()
    grapher = NatLanGraphs()

    # Load stop words
    parser.load_stop_words("data/stopwords.txt")

    # Load text files
    parser.load_text(
        "data/charney_report.pdf",
        label="1979: Charney Report",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/NASA_Hansen_Testimony.pdf",
        label="1988: NASA Hansen Testimony ",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/First_IPCC_Report.pdf",
        label="1990: First IPCC Report",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/Kyoto_Protocol_Text.pdf",
        label="1997: Kyoto Protocol Text",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/Stern_Review.pdf",
        label="2006: Stern Review",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/Paris_agreement.pdf",
        label="2015: Paris Agreement",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/IPCC_Special_Report.pdf",
        label="2018: IPCC Special Report",
        parser=ParserName.pdf_parser,
    )
    parser.load_text(
        "data/2023_IPCC_AR6_Report.pdf",
        label="2023: IPCC AR6 Synthesis Report",
        parser=ParserName.pdf_parser,
    )

    # Create visuals
    print("\nCreating Sankey diagram...")
    grapher.text_to_word_sankey(parser, k=5)

    print("\nCreating words frequency subplots...")
    grapher.word_frequency_bars(parser, top_n=10)

    print("\nCreating comparison chart...")
    grapher.compare_word_counts(parser, top_k=10)

    print("\nDone!!")


if __name__ == "__main__":
    main()
