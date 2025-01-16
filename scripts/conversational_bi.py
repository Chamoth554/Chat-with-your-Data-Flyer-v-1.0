
import pandas as pd

# Load the CSV file
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return f"Error loading data: {e}"

# Process queries
def process_query(df, query):
    if "average of column" in query.lower():
        column_name = query.split('"')[1]
        return df[column_name].mean()
    elif "maximum value in column" in query.lower():
        column_name = query.split('"')[1]
        return df[column_name].max()
    else:
        return "Query not recognized."

if __name__ == "__main__":
    # Example usage
    file_path = "data/sample_data.csv"
    data = load_data(file_path)

    if isinstance(data, str):  # Error message
        print(data)
    else:
        query = 'What is the average of column "Sales"?'
        result = process_query(data, query)
        print(f"Result: {result}")
