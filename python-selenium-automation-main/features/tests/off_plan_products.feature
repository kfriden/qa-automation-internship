# Created by Kait Kait at 5/28/2024
Feature: Off Plan Page

  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    When Click on off plan at the left side menu
    When Verify the off plan page opens
    Then Click filter button in top left-hand corner
    Then Input unit price from 1200000 AED
    Then Input unit price to 2000000 AED
    When Click Apply filter button
    Then Verify the price in all cards is inside the range (1200000 - 2000000)


  Scenario: User can filter on MOBILE the off plan products by Unit price range
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    When Click on off plan at the bottom left
    When Verify the off plan page opens
    Then Click filter button in top right-hand corner
    Then Input unit price from 1200000 AED
    Then Input unit price to 2000000 AED
    When Click Apply filter button
    Then Verify the price in all cards is inside the range (1200000 - 2000000)
