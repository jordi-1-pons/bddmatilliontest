from behave import *

# Define a step to get table name
@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name
    print(f"Table name set to: {context.table_name}")

# Define a step to get column names
@given('the columns are "{columns}"')
def step_given_columns(context, columns):
    context.columns = columns.split(', ')
    print(f"Columns set to: {context.columns}")

# Step to query the database and fetch columns
@when('I query the table {table_name}')
def step_when_query_table(context, table_name):
    print("Querying the table...")
    context.cursor = context.cursor()
    query = "SELECT column_name FROM information_schema.columns WHERE table_name = '{}'".format(table_name)
    context.cursor.execute(query)
    result = context.cursor.fetchall()
    context.fetched_columns = [row[0] for row in result]
    print(f"Fetched columns: {context.fetched_columns}")

# Step to verify the columns
@then('the table {table_name} should have the columns {expected_columns}')
def step_then_verify_columns(context, table_name, expected_columns):
    expected_columns_set = set(expected_columns.split(', '))
    fetched_columns_set = set(context.fetched_columns)
    print(f"Expected columns: {expected_columns_set}")
    print(f"Fetched columns: {fetched_columns_set}")
    assert expected_columns_set == fetched_columns_set, f"Expected columns: {expected_columns_set}, but got: {fetched_columns_set}"
