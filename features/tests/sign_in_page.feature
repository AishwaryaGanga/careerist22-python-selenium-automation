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