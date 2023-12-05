import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Function to load and preprocess data
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Preprocessing steps (e.g., handling missing values, feature engineering)
    return data

# Function to split data into training and testing sets
def split_data(data, target_column):
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Function to train a linear regression model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

# Function to plot predictions vs actual values
def plot_predictions(X_test, y_test, y_pred):
    plt.scatter(X_test, y_test, color='black', label='Actual values')
    plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted values')
    plt.title('Predictions vs Actual')
    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.legend()
    plt.show()

def run():
    file_path = input("Enter the path to your dataset: ")
    target_column = input("Enter the name of the target column: ")

    data = load_data(file_path)
    X_train, X_test, y_train, y_test = split_data(data, target_column)
    model = train_model(X_train, y_train)

    mse, r2 = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}, R^2 Score: {r2}")

    if input("Plot predictions? (y/n): ").lower() == 'y':
        plot_predictions(X_test, y_test, model.predict(X_test))

if __name__ == "__main__":
    run()
