import os
import requests
import pandas as pd
import numpy as np

# Function to automatically download data from a given URL
def download_data(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Data downloaded to {save_path}")
    except requests.RequestException as e:
        print(f"Error downloading data: {e}")

# Function to process downloaded data
def process_data(file_path):
    try:
        data = pd.read_csv(file_path)
        # Example preprocessing steps
        data = data.dropna()  # Remove missing values
        data = data.drop_duplicates()  # Remove duplicate rows
        print("Data processing complete.")
        return data
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

# Function to perform analysis on the data
def analyze_data(data):
    try:
        analysis_results = {}
        # Example analysis - replace with your analysis logic
        analysis_results['mean'] = data.mean()
        analysis_results['median'] = data.median()
        analysis_results['std_dev'] = data.std()
        print("Data analysis complete.")
        return analysis_results
    except Exception as e:
        print(f"Error analyzing data: {e}")
        return None

# Function to generate a report from analysis
def generate_report(analysis_results, report_path):
    try:
        with open(report_path, 'w') as file:
            for key, value in analysis_results.items():
                file.write(f"{key}: {value}\n")
        print(f"Report generated at {report_path}")
    except Exception as e:
        print(f"Error generating report: {e}")

# Main function to run the automated tasks
def run():
    url = input("Enter the URL to download data: ")
    save_path = "downloaded_data.csv"
    report_path = "analysis_report.txt"

    download_data(url, save_path)
    data = process_data(save_path)
    if data is not None:
        analysis_results = analyze_data(data)
        if analysis_results:
            generate_report(analysis_results, report_path)

if __name__ == "__main__":
    run()
