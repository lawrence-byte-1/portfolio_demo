# 📊 Automated Data Cleanup & Visualization Pipeline

> **"Turning real-world data chaos into structured insights and clean visuals."**

## 🎯 The Purpose & Problem Solved
Let’s face it: real-world spreadsheets are a disaster. They come packed with missing values, bad formatting, and useless noise. Manually hacking through them is a waste of time. 

This project demonstrates a streamlined two-stage data pipeline:
1. **The Cleanup:** Automatically strips out the junk from a raw file and outputs a clean, reliable master dataset.
2. **The Focus & Visualization:** Isolates only the key variables that matter (e.g., Column A vs. Column B) and turns them into a clean, presentation-ready chart.

---

## 🛠️ The Tech Stack
* **Python:** The core programming language powering the workflow.
* **Pandas:** The data wrangler. It handles file ingestion, strips out missing or corrupt rows, and restructures chaotic spreadsheets into clean tables.
* **Matplotlib:** The visualizer. It takes those structured columns and instantly brings your data to life as an easy-to-read chart.

---

## 📂 Project Layout
The project is organized into a clean data pipeline structure:
* **`data/`** → Drop your raw, uncleaned spreadsheets here.
* **`code/`** → Where the Python automation scripts live.
* **`output/`** → Where your freshly cleaned data files and visual charts pop out automatically.

---

## 💻 Code Demonstration (The Two-Stage Pipeline)

Here is a look at the core logic. It splits the job cleanly: first sanitizing the data and exporting a clean file, then narrowing down to two key columns for visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STAGE 1: Clean the raw data & save it
# ==========================================
# Ingest raw file (supports CSV, Excel, etc.)
raw_data = pd.read_your_format("data/your_messy_file")

# Clean missing rows and strip out the junk
cleaned_df = raw_data.dropna()

# Output the fully cleaned master spreadsheet
cleaned_df.to_your_format("output/cleaned_master_file")


# ==========================================
# STAGE 2: Isolate, Focus, and Visualize
# ==========================================
# Grab only the two core columns you care about
chart_data = cleaned_df[['Column_A', 'Column_B']]

# Plot the focused insights
plt.figure(figsize=(8, 4))
plt.bar(chart_data['Column_A'], chart_data['Column_B'])
plt.title("Key Insights Overview")
plt.xlabel("Column A")
plt.ylabel("Column B")

# Save the visual output
plt.savefig("output/final_chart.png")
