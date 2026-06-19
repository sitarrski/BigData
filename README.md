# Music Streaming Data Analyzer

A Python data analysis script built with `pandas` that processes user listening histories and song metadata (inspired by the Million Song Dataset). It cleans, merges, and extracts key insights regarding user behavior and artist popularity.

## Features

* **Data Cleaning:** Automatically strips whitespace, handles encoding issues, and safely converts Unix timestamps into readable DateTime objects.
* **Top Charts:** Calculates and displays the top 10 most popular songs and the single most-played artist across the entire dataset.
* **User Analytics:** Identifies the top 10 most active users based on the number of unique songs they have listened to.
* **Temporal Trends:** Groups listening data by month to show a 1-12 chronological breakdown of listening activity.
* **"Superfan" Finder:** A specialized query that identifies dedicated fans of specific artists (e.g., finding users who have listened to all of the top 3 most popular Queen songs).

## Setup

In order to run the script, you need to download datasets and include them in the same directory:

https://drive.google.com/file/d/14YhXDwI9Y4lNrADbmCpAMpgkJ4QcHq5g/view?usp=drive_link 
https://drive.google.com/file/d/1_PHw_218Oa0jGRmwIyd3xOlZ4FcIrmnH/view?usp=drive_link

Install the required dependency:

```bash
pip install pandas
```
## Usage

Run the script from your terminal:
```bash
python musicdata.py
```
