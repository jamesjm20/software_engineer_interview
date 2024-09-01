from solution.db_connection import get_connection
from solution.query import calculate_gaps
from solution.process_results import process_results

# run the application and print the list
def main():
    conn = get_connection()
    cursor = conn.cursor()
    
    results = calculate_gaps(cursor)

    json_output = process_results(results)
    print(json_output)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()