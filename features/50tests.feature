@50tests
Feature: Contains 50 tests for execution time comparing with pytest


# 10 title scenarios - passed
  Scenario Outline: I open main page and verify page title

    Given User opens Search Page
    Then Page title should be "<title>"
    Examples:
      | title                                                    |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |
      | Online reservation and purchase tickets - Ukrzaliznytsia |

    #  10 logo scenarios - passed
  Scenario Outline: I open page and should see logo of company <iteration>

    Given User opens Search Page
    Then Logo should be visible

    Examples:
      | iteration |
      | 1         |
      | 2         |
      | 3         |
      | 4         |
      | 5         |
      | 6         |
      | 7         |
      | 8         |
      | 9         |
      | 10        |

#  authorization - 30 scenarios (20 passed 10 failed
  @auth_bulk
  Scenario Outline: User authorization
    Given User opens Search Page
    When User logs in via authorization form using "<email>" and "<password>"
    Then Successful login for "<email>" and "<password>" is expected to "<pass_or_fail>"

    Examples:
      | email              | password | pass_or_fail |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |
      | qavunets@gmail.com | tttt1111 | Pass         |
      | qavunets@gmail.com | Turle    | Fail         |
      | qavunets@gmail.com | Turle    | Pass         |




