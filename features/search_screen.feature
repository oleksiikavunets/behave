Feature: Main page of booking service must open easily
  and logo should be visible


  Scenario: I open page and should see logo of company

    Given I open Search Page
    Then Logo should be visible


  Scenario Outline: I open main page and verify page title

    Given I open Search Page
    Then Page title should be "<title>"
    Examples:
      | title                                                     |
      | Online reservation and purchase tickets - Ukrzaliznytsia  |
      | Offline reservation and purchase tickets - Ukrzaliznytsia |