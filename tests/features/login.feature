Feature: Login


  Background:
    Given the user is on login page


  Scenario: Create Article
    Given the drupal content "article" has been created
#    When the user enters admin credentials
#    Then the user should be redirected to admin page


  Scenario: Create Page
    Given the drupal content "page" has been created
#    When the user enters username as "Invalid" with password "User"
#    Then the user is still in login page

  Scenario: Create Recipe
    Given the drupal content "recipe" has been created