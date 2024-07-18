# Created by Kait Kait at 7/16/2024
Feature: Editing Info on Settings Page

  Scenario: User can go to settings and edit the personal information
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click on the settings option on the left side
    Then Click on the Edit profile option
    When Enter some test data into the name field: Kit
    Then Enter some test data into the phone number field: 668 902 7880
    When Enter some test data into the company field: helllooooo
    Then Verify the right information is present in the name input field
    Then Verify the right information is present in the phone number input field
    Then Verify the right information is present in the company input field
    When Check “Save Changes” button is available and clickable
    When Check “Close” button is available and clickable
