import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Function to load your data
def load_data():
    # Prompt the user to enter the file path
    filepath = input("Please enter the path to your dataset (CSV format): ")
    try:
        # Try to read the file at the provided path
        return pd.read_csv(filepath)
    except FileNotFoundError:
        # If the file is not found, inform the user and return None
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred while reading the file: {e}")
        return None

# Convert categorical columns to numeric using one-hot encoding
def convert_categorical_to_numeric(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        # For each categorical column, apply label encoding
        label_encoder = LabelEncoder()
        df[col] = label_encoder.fit_transform(df[col])
    return df

def run():
    # Load your dataset
    df = load_data()
    if df is not None:
        # Convert categorical data to numeric
        df = convert_categorical_to_numeric(df)
        
        # Prompt user for target column name
        target_column = input("Enter the name of the target column: ")

        # Split the data into features and target variable
        X = df.drop(target_column, axis=1)
        y = df[target_column]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions and evaluate the model
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse}')
    else:
        print("Data loading failed.")

if __name__ == "__main__":
    run()
