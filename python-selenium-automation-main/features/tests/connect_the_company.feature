# Created by Kait Kait at 7/8/2024
Feature: Connect the company Page

  Scenario: Verify right tab opens when clicking on the 'connect the company' button
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click 'Connect the company' button on left side column
    When Switch to current window
    Then Verify that the correct tab opens
