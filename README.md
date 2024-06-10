# WhatsApp-Chat-Analysis
## Overview
#### WhatsApp Chat Analyzer is a powerful tool built with Streamlit, designed to help you analyze your WhatsApp chat data. This project preprocesses chat data and provides detailed insights, including top statistics, activity timelines, most busy users, word clouds, and common words, among other features.

## Features
* Top Statistics: Provides total messages, total words, media shared, and links shared.
* Monthly and Daily Timelines: Visualize your chat activity over time.
* Activity Maps: Identify the most active days and months.
* Heat Maps: Analyze chat activity patterns over different times of the day and week.
* Most Busy Users: Find out who the most active participants in the chat are.
* Word Cloud: Generate a word cloud to visualize the most frequent words used in the chat.
* Most Common Words: List the most common words in the chat, excluding stop words.

## Installation
1. Clone the Repository:
```
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```
2. Install Dependencies:
#### Make sure you have Python 3.7+ installed. Install the required packages using pip:
```
pip install -r requirements.txt
```
3. Run the Application:
```
streamlit run app.py
```
## Usage
1. Upload your WhatsApp chat file (in .txt format) using the file uploader in the sidebar.
2. Select the user for which you want to analyze the chat data, or choose 'Overall' for all users.
3. Click on 'Show Analysis' to generate and display the analysis.

## Dependencies
* Streamlit
* pandas
* matplotlib
* seaborn
* urlextract
* wordcloud
* emoji
