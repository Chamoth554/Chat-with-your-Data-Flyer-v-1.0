
import pandas as pd

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
def process_query(df, query):
    # Handle average calculation in both English and Sinhala
    if "average of column" in query.lower() or "තීරුවේ මධ්‍යම වටිනාකම" in query:  # Sinhala phrase for 'average of column'
        if "'" not in query:
            return "දෝෂය: කරුණාකර තීරුවේ නාමය එක් එක් ගැටුම් ලකුණු ('') අතර දක්වන්න."
        try:
            column_name = query.split("'")[1]  # Extract column name between single quotes
            return df[column_name].mean()
        except KeyError:
            return f"දෝෂය: '{column_name}' නාමය ඇති තීරුවක් නොමැත."
        except Exception as e:
            return f"දෝෂය: {e}"
        
    # Handle maximum value calculation in both English and Sinhala
    elif "maximum value in column" in query.lower() or "තීරුවේ උපරිම වටිනාකම" in query:  # Sinhala phrase for 'maximum value in column'
        if "'" not in query:
            return "දෝෂය: කරුණාකර තීරුවේ නාමය එක් එක් ගැටුම් ලකුණු ('') අතර දක්වන්න."
        try:
            column_name = query.split("'")[1]  # Extract column name between single quotes
            return df[column_name].max()
        except KeyError:
            return f"දෝෂය: '{column_name}' නාමය ඇති තීරුවක් නොමැත."
        except Exception as e:
            return f"දෝෂය: {e}"
    
    else:
        return "ගොනු සොයා ගැනීමට නොහැකි විය. කරුණාකර 'average of column <තීරුවේ නාමය>' හෝ 'maximum value in column <තීරුවේ නාමය>' වැනි ප්‍රශ්න ප්‍රකාශ කරන්න."

if __name__ == "__main__":
    file_path = "sample_data.csv"
    data = load_data(file_path)
    print("Data Loaded!")
    
    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting the program.")
            break
        
        # Debug: print the query to see what the user entered
        print(f"Received query: {query}")
        
        result = process_query(data, query)
        print(f"Result: {result}")
