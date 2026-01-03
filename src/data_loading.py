import pandas as pd

def load_data():
    """
    Loads the Telco Customer Churn dataset
    """
    df = pd.read_csv("../data/Telco-Customer-Churn.csv")
    return df


if __name__ == "__main__":
    df = load_data()
    print("Dataset loaded successfully")
    print("Shape:", df.shape)
    print(df.head())
    print(df.info())
