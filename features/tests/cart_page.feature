# Created by vaishnavisethuraman at 14/03/25
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on the Cart icon
    Then Verify 'Your cart is empty' message is shown
    And Verify cart page opens


  Scenario: 'Selected target product added to cart' shown in cart page
    Given Open target main page
    When Search for white  chocolate
    And Add the product to the cart
    Then Verify cart has the product