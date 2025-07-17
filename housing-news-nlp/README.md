# Analyzing the Dutch Housing Crisis: An End-to-End NLP Project

This repository documents a comprehensive project that uses Natural Language Processing (NLP) to analyze the evolving narrative of the Dutch housing crisis. The project spans the entire data analysis pipeline, from web scraping and text preparation to advanced topic modeling and sentiment analysis, culminating in a detailed narrative intelligence report.

### Project Objective
The primary goal was to move beyond surface-level statistics and understand the *story* of the Dutch housing crisis as told by the news media. This involved identifying the key themes of discussion, tracking how they changed over time, and measuring the emotional tone of the narrative in response to real-world events. A secondary objective was to demonstrate a robust, end-to-end NLP workflow.

### Project Workflow & Key Stages
The project was executed in five distinct phases using a dataset of **1,101 articles** scraped from **DutchNews.nl** (2013-2025):

**Part I: Data Acquisition & Text Preparation**

*   Commenced with raw article data (headlines, text, timestamps) acquired via web scraping.
*   Conducted fundamental text pre-processing on the article corpus, including removal of stop words and punctuation, and conversion to lowercase.
*   Implemented lemmatization to standardize words to their root form, ensuring that terms like "house" and "houses" were treated as a single concept for more accurate analysis.

**Part II: Exploratory Data Analysis (EDA) & N-Gram Analysis**

*   Performed initial visualizations to understand the dataset's characteristics, including plotting article frequency over time, which revealed a dramatic increase in coverage from 2022 onwards.
*   Conducted N-gram (unigram and bigram) frequency analysis to identify the most common single words and two-word phrases.
*   Created word clouds from both headlines and full article texts to visually represent the most prominent terms. This initial analysis confirmed the centrality of concepts like `house price` and `rent control`.

**Part III: Topic Modeling with BERTopic**

*   Implemented the powerful BERTopic modeling technique to automatically discover and cluster the latent topics within the 1,101 articles.
*   Identified **18 distinct, coherent topics**, including `Mortgages & Home Buying`, `Refugee Accommodation`, `Groningen Earthquakes`, and `Airbnb & Holiday Rentals`.
*   Visualized the prevalence of these topics over time, revealing a clear narrative shift from broad economic concerns to specific policy and social issues in recent years.

**Part IV: Sentiment Analysis with VADER**

*   Applied VADER (Valence Aware Dictionary and sEntiment Reasoner), a sentiment analysis tool specifically tuned for online and media text, to quantify the emotional tone of the articles.
*   Calculated sentiment scores for each article and analyzed the average sentiment trend over time, which showed an overall increase in positivity since 2019.
*   Created a "Sentiment per Topic" analysis, revealing a stark contrast: topics framed as problems (e.g., `Foundation & Climate Risks`) were highly negative, while topics framed as solutions (e.g., `Mortgages`, `Rent Control`) were highly positive.

**Part V: Advanced Insight Generation - Topic Sentiment Over Time**

*   Synthesized all previous stages by creating a topic-sentiment heatmap. This advanced visualization tracks the sentiment of *each individual topic* on a year-by-year basis.
*   This final analysis pinpointed dynamic narratives with high precision. For instance, it visualized the sentiment for `New Home Construction` turning sharply negative during the nitrogen crisis and later recovering. It also highlighted the highly contentious and volatile sentiment surrounding `Refugee Accommodation`.

### Key Technologies & Libraries
*   **Programming Language:** Python
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Text Processing & NLP:** NLTK, spaCy
*   **Topic Modeling:** BERTopic
*   **Sentiment Analysis:** VADER
*   **Data Visualization:** Seaborn, Matplotlib, WordCloud

### Key Insights & Conclusion
This project successfully transformed unstructured text into a clear and dynamic narrative intelligence report. The key findings include:

*   **A Narrative Shift:** The focus of housing news has evolved from a general *market problem* (dominated by house prices) to a multifaceted *political and social challenge* (dominated by rent control, refugee housing, and sustainability).
*   **Sentiment Tells a Story:** The sentiment analysis revealed a clear "problem/solution" dichotomy. The language used to describe the consequences of the crisis is negative, while the language around policy, finance, and other interventions is overwhelmingly positive.
*   **Audience Context is Key:** The choice of DutchNews.nl, which primarily targets expats, provides crucial context. The pragmatic, opportunity-focused tone (especially around home buying) is likely a reflection of its audience's needs and interests.

This project demonstrates an end-to-end NLP workflow, emphasizing meticulous text preparation, the powerful combination of different analytical techniques, and a deep focus on interpreting data-driven insights within a real-world context.
