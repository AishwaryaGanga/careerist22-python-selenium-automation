# Created by vaishnavisethuraman at 13/04/25
Feature: Search for product and loop through to test the name and image of the product


  Scenario: User loops through searched product.
    Given Open target main page
    When Search for orange juice
    Then Verify products has a product name and image