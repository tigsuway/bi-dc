Feature: Login


  Background:
    Given the user is on login page


  Scenario: Valid user can login
    When the user enters username as "Mello" with password "M3ll0m4r!123"
    Then the user should be redirected to admin page


  Scenario: Invalid user login
    When the user enters username as "Invalid" with password "User"
    Then the user is still in login page