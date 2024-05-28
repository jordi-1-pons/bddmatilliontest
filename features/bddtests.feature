Feature: Verify fact_test table 
  Scenario: Check if fact_test table has the correct columns 
    Given I connect to the Snowflake database 
    When I query the table fact_test 
    Then the table fact_test should have the columns rep_id and rep_status