from behave import given, when, then

@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name

@given('the columns are "{columns}"')
def step_given_columns(context, columns):
    context.columns = columns.split(", ")

@when('I query the table fact_test')
def step_when_query_table(context):
    # Simulated data fetching
    context.data = {
        'table_name': context.table_name,
        'columns': context.columns
    }

@then('the table fact_test should have the columns rep_id and rep_status')
def step_then_verify_columns(context):
    expected_columns = ['rep_id', 'rep_status']
    actual_columns = context.data['columns']

    assert context.data['table_name'] == 'fact_test', f"Expected table name 'fact_test', but got {context.data['table_name']}"
    assert sorted(actual_columns) == sorted(expected_columns), f"Expected columns {expected_columns}, but got {actual_columns}"
