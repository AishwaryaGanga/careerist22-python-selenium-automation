# Created by vaishnavisethuraman at 13/03/25
Feature: Test Scenarios for Search functionality

  Scenario: User verify the Cart button
    Given Open target.com
    When Click on the Cart icon
    Then Verify "Your cart is empty"