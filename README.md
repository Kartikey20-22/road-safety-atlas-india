# Road Safety Atlas India

An interactive road accident analytics dashboard designed and developed by **Kartikey Rajpoot**.

## Overview

I built this project to explore how road accident counts changed across India between **2018 and 2022**. The dashboard combines cleaned public datasets, comparative analysis, and interactive charts so users can quickly understand regional accident patterns across both **states** and **union territories**.

## Project Highlights

- Personal Streamlit dashboard with a custom portfolio-style identity
- Interactive state and union territory trend analysis
- Low-accident and high-accident region ranking views
- Side-by-side comparison charts for selected regions
- Cleaned datasets prepared for exploratory data analysis

## Dataset

- **Source:** Ministry of Road Transport & Highways (MoRTH), Government of India
- **Files used:** `datasets/states_dataset.csv` and `datasets/ut_dataset.csv`
- **Coverage:** 2018, 2019, 2020, 2021, 2022
- **Main fields:** yearly accident counts and `Total_5yr`

## Tech Stack

- Python
- Streamlit
- pandas
- plotly.express
- matplotlib
- seaborn

## Project Structure

- `app.py` - Streamlit dashboard application
- `datasets/` - cleaned state and union territory datasets
- `logo.png` - custom project logo
- `pre.ipynb` - notebook used for exploratory analysis

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this project to GitHub.
2. Create a new app on Streamlit Community Cloud.
3. Select this repository and set the main file path to `app.py`.
4. Deploy and share the generated app url 