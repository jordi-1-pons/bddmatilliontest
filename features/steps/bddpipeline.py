from behave import *
import os
import json

# Step to get the table name from the file
@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name

# Step to get the columns from the file
@given('the columns are "{columns}"')
def step_given_columns(context, columns):
    context.columns = columns.split(', ')

# Step to query the database and fetch columns
@when('I query the table {table_name}')
def step_when_query_table(context, table_name):
    # Read table data from the file
    file_path = '/tmp/table_data/table_data.txt'
    with open(file_path, 'r') as file:
        data = json.load(file)  # Use json.load to read JSON data
    context.fetched_table_name = data['table_name']
    context.fetched_columns = data['columns']

# Step to verify the columns
@then('the table {table_name} should have the columns {expected_columns}')
def step_then_verify_columns(context, table_name, expected_columns):
    expected_columns_set = set(expected_columns.split(', '))
    fetched_columns_set = set(context.fetched_columns)

    assert fetched_columns_set == expected_columns_set, f"Expected columns {expected_columns_set}, but got {fetched_columns_set}"
    print(f"Table {context.fetched_table_name} has the correct columns.")

# Optional: To verify table name as well
@then('the table name should be {expected_table_name}')
def step_then_verify_table_name(context, expected_table_name):
    assert context.fetched_table_name == expected_table_name, f"Expected table name {expected_table_name}, but got {context.fetched_table_name}"
    print(f"Table name {context.fetched_table_name} is correct.")
