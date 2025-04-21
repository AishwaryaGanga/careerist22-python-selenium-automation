# Created by vaishnavisethuraman at 18/04/25
Feature: Verify sign in page

  Scenario: Verify the user can access Sign in
    Given Open target main page
    When Click on Sign In button
    And Click Sign In from navigation menu
    Then Verify Sign in form opened

  Scenario: Create login page
    Given Open target main page
    When Click on Sign In button
    And Click Sign In from navigation menu
    Then Verify user can login

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target sign in page
    And Store original window
    When Click on Target terms and conditions link
    #And Switch to the newly opened window
    #Then Verify Terms and Conditions page is opened
    #And User can close new window and switch back to original

