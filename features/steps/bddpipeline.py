<<<<<<< HEAD
from behave import given, when, then 



@given('I connect to the Snowflake database')
def step_impl(context):
    context.connection = context.config.userdata['connection']
    context.cursor = context.connection.cursor() 

@when('I query the table fact_test') 
def step_impl(context): 
    query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'fact_test'" 
    context.cursor.execute(query) 
    context.columns = [row[0] for row in context.cursor.fetchall()] 

@then('the table fact_test should have the columns rep_id and rep_status') 
def step_impl(context): 
    expected_columns = {'rep_id', 'rep_status'} 
    assert expected_columns.issubset(set(context.columns)), f"Missing columns: {expected_columns - set(context.columns)}"
=======
from behave import given, when, then 
import snowflake.connector


@given('I connect to the Snowflake database')
def step_impl(context):
    context.connection = context.config.userdata['connection']
    context.cursor = context.connection.cursor() 

@when('I query the table fact_test') 
def step_impl(context): 
    query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'fact_test'" 
    context.cursor.execute(query) 
    context.columns = [row[0] for row in context.cursor.fetchall()] 

@then('the table fact_test should have the columns rep_id and rep_status') 
def step_impl(context): 
    expected_columns = {'rep_id', 'rep_status'} 
    assert expected_columns.issubset(set(context.columns)), f"Missing columns: {expected_columns - set(context.columns)}"
>>>>>>> d1d910d6be15fae780fdeb54b9146226d014edc8
