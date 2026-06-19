# Music Streaming Data Analyzer

A Python data analysis script built with `pandas` that processes user listening histories and song metadata (inspired by the Million Song Dataset). It cleans, merges, and extracts key insights regarding user behavior and artist popularity.

## Features

* **Data Cleaning:** Automatically strips whitespace, handles encoding issues, and safely converts Unix timestamps into readable DateTime objects.
* **Top Charts:** Calculates and displays the top 10 most popular songs and the single most-played artist across the entire dataset.
* **User Analytics:** Identifies the top 10 most active users based on the number of unique songs they have listened to.
* **Temporal Trends:** Groups listening data by month to show a 1-12 chronological breakdown of listening activity.
* **"Superfan" Finder:** A specialized query that identifies dedicated fans of specific artists (e.g., finding users who have listened to all of the top 3 most popular Queen songs).

## Setup

Install the required dependency:

```bash
pip install pandas
```
## Usage

Run the script from your terminal:
```bash
python musicdata.py
