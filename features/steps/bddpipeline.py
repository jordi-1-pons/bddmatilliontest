from behave import *

def fetch_data_from_matillion(context):
    cursor = context.cursor()
    query = """
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'fact_test'
    AND COLUMN_NAME IN ('rep_id', 'rep_status')
    """
    cursor.execute(query)
    columns = cursor.fetchall()
    return [column[0] for column in columns]

@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name

@given('the columns are "{columns}"')
def step_given_columns(context, columns):
    context.expected_columns = columns.split(', ')

@when('I query the table {table_name}')
def step_when_query_table(context, table_name):
    context.fetched_columns = fetch_data_from_matillion(context)

@then('the table {table_name} should have the columns {columns}')
def step_then_verify_columns(context, table_name, columns):
    actual_columns = set(context.fetched_columns)
    expected_columns = set(columns.split(', '))
    assert actual_columns == expected_columns, f"Expected columns {expected_columns}, but got {actual_columns}"
