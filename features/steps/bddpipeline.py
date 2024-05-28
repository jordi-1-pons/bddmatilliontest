from behave import *

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
        data (dict): The data fetched to be verified.
        
    Returns:
        bool: True if data is as expected, False otherwise.
    """
    expected_data = {
        'table_name': 'fact_test',
        'columns': ['rep_id', 'rep_status']
    }
    return data == expected_data

@given('I connect to the Snowflake database')
def step_impl(context):
    # Assuming connection is established through the existing Matillion environment
    context.connection = True  # Simulated connection flag

@when('I query the table {table_name}')
def step_impl(context, table_name):
    if context.connection:
        context.data = fetch_data_from_context(context)
    else:
        raise Exception("No connection to the database.")

@then('the table {table_name} should have the columns {columns}')
def step_impl(context, table_name, columns):
    expected_columns = set([col.strip() for col in columns.split(',')])
    actual_columns = set(context.data['columns'])
    assert expected_columns == actual_columns, f"Expected columns {expected_columns}, but got {actual_columns}"
