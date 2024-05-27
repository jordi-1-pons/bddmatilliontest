def fetch_data_from_context(context):
    """
    This function simulates fetching data from the context.

    Args:
        context (dict): The context from which we fetch data.

    Returns:
        dict: Dictionary with data fetched from context.
    """
    # Simulated data; in practice, this should come from the SQL query data
    data = {
        'table_name': 'fact_test',
        'columns': ['rep_id', 'rep_status']
    }
    return data

def verify_data(data):
    """
    This function verifies if the fetched data is as expected.

    Args:
        data (dict): The data fetched from the context.

    Returns:
        bool: Whether the data matches expectations.
    """
    expected_table_name = 'fact_test'
    expected_columns = ['rep_id', 'rep_status']

    table_name = data.get('table_name')
    columns = data.get('columns')

    # Check table name
    if table_name != expected_table_name:
        print(f"Error: Expected table name '{expected_table_name}', but got '{table_name}'")
        return False

    # Check columns
    for col in expected_columns:
        if col not in columns:
            print(f"Error: Expected column '{col}' not found in the passed columns")
            return False

    print("Verification successful: Table name and columns are as expected.")
    return True


# Main function
if __name__ == "__main__":
   # Fetch data from context
    data = fetch_data_from_context(context)

    # Verify the data
    is_verified = verify_data(data)

    if is_verified:
        print("Data verification passed.")
    else:
        print("Data verification failed.")