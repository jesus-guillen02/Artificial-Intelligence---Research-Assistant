import pandas as pd # Used for data manipulation and analysis
import matplotlib.pyplot as plt # Creating static, interactive, and animated visualizations
import seaborn as sns # Based on matplotlib, provides a high-level interface for drawing informative statistics and graphs

def load_csv_data(filepath): # Loads your data from a CSV file
    try:
        return pd.read_csv(filepath) # filepath(str) is the filepath in string form.
    except FileNotFoundError:
        print("Oops! File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occured: {str(e)}")
    return None # Returning the pandas.DF because we loaded the data

def show_stats(df): # Displays basic statistics (Mean, Mode, etc.) of the function
    print("\nData Statistics:\n", df.describe())

def plot_graph(df, x_column, y_column):
    if x_column not in df.columns or y_column not in df.columns:
        print(f"Columns {x_column} or {y_column} not found in the DataFrame.")
        return

    sns.scatterplot(x=x_column, y=y_column, data=df)
    plt.show()

def run():
    print("Welcome to the Data Analysis Tool!") # Intro to the data analysis tool
    filepath = input("Enter the path of your CSV data file: ") # Ensure to input the file in the correct /file/filename.xx

    # Loading the data
    df = load_csv_data(filepath)
    if df is not None:
        show_stats(df) # Showing the basic statistics of the data

    # Plotting Section
    print("\nLet's create a scatter plot.")
    x_column = input("Choose your X-axis column: ")
    y_column = input("Choose your Y-axis column: ")
    plot_graph(df, x_column, y_column)

if __name__ == "__main__":
    run()
