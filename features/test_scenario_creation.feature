Feature: Scenario creation for AE

  Scenario: Create simple scenario on AE
    Given I open AE as admin user
    When I create scenario on AE
    Then I should see created scenario in scenario list