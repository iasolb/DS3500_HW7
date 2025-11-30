# Homework 7 - Natural Language Processing and Text Analysis

---

#### Group Members:
- Amir Sesay
- Cassandra Cinzori
- Ian Solberg
- Iyman Mahmoud


---

### **Make Poster!!**

---

## Project Overview

This project builds a reusable framework for comparative text analysis of climate change reports spanning five decades. By analyzing how climate science communication has evolved from the 1970s to 2023, we explore changes in:
- **Terminology and language** (e.g., "global warming" → "climate crisis")
- **Urgency and tone** (scientific caution → urgent action needed)
- **Focus areas** (future predictions → observed impacts)
- **Scientific consensus** (early hypotheses → confirmed evidence)

## Documents Analyzed

Our corpus includes 8 landmark climate change reports:

1. **1979 - Charney Report**: "Carbon Dioxide and Climate: A Scientific Assessment"
   - First major U.S. government report on CO₂

2. **1988 - NASA Hansen Testimony**: James Hansen's Congressional Testimony
   - Landmark moment: "The greenhouse effect has been detected"

3. **1990 - First IPCC Report**: Summary for Policymakers
   - Established initial scientific consensus

4. **1997 - Kyoto Protocol**: International treaty text
   - First major international policy response

5. **2006 - Stern Review**: "The Economics of Climate Change"
   - Economic perspective on climate action

6. **2015 - Paris Agreement**: International accord text
   - Landmark goal of limiting warming to 1.5°C

7. **2018 - IPCC Special Report**: "Global Warming of 1.5°C"
   - Major assessment of 1.5°C warming impacts

8. **2023 - IPCC AR6 Synthesis Report**: Most current scientific consensus
   - Synthesizes latest climate science across all working groups

## Technical Framework



1. **`parser.py`** - `ParserName` class
   - PDF loading and preprocessing
   - Custom parser support (handles both .txt and .pdf files)
   - Stop word filtering
   - Word frequency analysis
   - Sankey diagram generation

2. **`visualization.py`** - `NatLanGraphs` class
   - Three required visualizations:
     - Sankey diagram (text-to-word flow)
     - Subplots (word frequency per document)
     - Comparison overlay (cross-document analysis)

3. **`executable.py`** - Main execution script
   - Document loading pipeline
   - Visualization generation

### Key Features
1. **Extensible Design**: Custom parser support for any file format   
2. **Stop Word Filtering**: Removes common words for meaningful analysis  
3. **Multiple Visualizations**: Three complementary views of the data  
4. **Clean Data Processing**: Removes punctuation, standardizes case   
5. **Scalable**: Easy to add more documents or custom parsers



## Visualizations

### 1. Sankey Diagram
**"Climate Change Reports: Word Frequency Flow Analysis"**
- Shows flow from documents to most common words
- Line thickness = word frequency
- Reveals which terms dominate each report

### 2. Word Frequency Subplots
**"Top N Most Frequent Words Across Climate Change Reports"**
- Grid of bar charts, one per document
- Compares top words within each report
- Shows individual document characteristics

### 3. Comparative Overlay
**"Evolution of Climate Terminology: Word Frequency Comparison Across Decades"**
- Grouped bar chart comparing word usage
- Tracks how specific terms change over time
- Reveals shifts in scientific language

## Key Insights

Our analysis reveals:

1. **Increasing Urgency**: Later reports use more action-oriented language  
2. **Terminology Evolution**: Shift from "global warming" to "climate change" to "climate crisis"   
3. **Growing Certainty**: Early reports use tentative language; recent ones state facts  
4. **Broadening Scope**: Focus expands from CO₂ to comprehensive impacts  
5. **Action vs. Prediction**: Recent reports emphasize immediate action over future scenarios

## File Descriptons
- **`parser.py`**: Core NLP processing class with text and PDF loading and analysis
- **`visualization.py`**: Three visualization methods for text comparison
- **`executable.py`**: Main script that orchestrates the analysis
- **`data/stopwords.txt`**: List of common words to filter out



## Things to Do (to enhance)
- Sentiment analysis over time
- Topic modeling (LDA)
- Named entity recognition
- N-gram analysis
- Time series of term frequencies
- Geographic analysis of regional reports
