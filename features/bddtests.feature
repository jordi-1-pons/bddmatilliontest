<<<<<<< HEAD
Feature: Verify fact_test table 
  Scenario: Check if fact_test table has the correct columns 
    Given I connect to the Snowflake database 
    When I query the table fact_test 
=======
Feature: Verify fact_test table 
  Scenario: Check if fact_test table has the correct columns 
    Given I connect to the Snowflake database 
    When I query the table fact_test 
>>>>>>> d1d910d6be15fae780fdeb54b9146226d014edc8
    Then the table fact_test should have the columns rep_id and rep_status