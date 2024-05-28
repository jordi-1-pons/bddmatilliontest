Feature: Verify fact_test table
  Scenario: Check if fact_test table has the correct columns
    Given the table name is "fact_test"
    And the columns are "rep_id, rep_status"
    When I query the table fact_test
    Then the table fact_test should have the columns rep_id, rep_status
