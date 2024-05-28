from behave import *

# Function to fetch data from the context (real data from Matillion context)
def fetch_data_from_context(context):
    """
    This function fetches data from the Matillion context.
    
    Args:
        context (dict): The context from which we fetch data.
    
    Returns:
        dict: Dictionary with data fetched from context.
    """
    table_name = context.getVariable('table_name')
    columns = context.getVariable('fetched_columns')
    
    data = {
        'table_name': table_name,
        'columns': columns
    }
    return data

# Function to verify the fetched data
def verify_data(data):
    """
    This function verifies if the fetched data is as expected.
    
    Args:
        data (dict): Dictionary with data fetched from the context.
    """
    expected_columns = {'rep_id', 'rep_status'}
    actual_columns = set(data['columns'])
    
    assert actual_columns == expected_columns, f"Expected columns {expected_columns}, but got {actual_columns}"

@given('I connect to the Snowflake database')
def step_impl(context):
    context.data = fetch_data_from_context(context)

@when('I query the table {table_name}')
def step_impl(context, table_name):
    assert context.data['table_name'] == table_name, f"Expected table {table_name}, but got {context.data['table_name']}"

@then('the table {table_name} should have the columns {columns}')
def step_impl(context, table_name, columns):
    expected_columns = set(columns.split(', '))
    actual_columns = set(context.data['columns'])
    assert actual_columns == expected_columns, f"Expected columns {expected_columns}, but got {actual_columns}"
