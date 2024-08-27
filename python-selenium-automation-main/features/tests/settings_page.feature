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


  Scenario: User can go to settings and change language to Russian
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click on the settings option on the left side
    When Change the language of the page to Russian in top right corner
    Then Verify the language has changed to Russian


  Scenario: User can add a project through Settings Page
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click on the settings option on the left side
    When Click on the Add a project button
    Then Verify the Add a project page opens
    When Enter test data into the name field: Daenerys
    When Enter test data into the Company name field: Krispy Kreme
    When Enter test data into the Company role field: QA
    When Enter test data into the age of company field: 1
    When Enter test data into the country of project field: USA
    When Enter test data into the Name of project field: Venti Towers
    When Enter test data into the phone number field: 1 800 789 2345
    When Enter test data into the email field: venti_towersUSA@gmail.com
    Then Verify the right information is present in the name field
    Then Verify the right information is present in the Company name field
    Then Verify the right information is present in the Company role field
    Then Verify the right information is present in the Company age field
    Then Verify the right information is present in the Company country field
    Then Verify the right information is present in the Name of project field
    Then Verify the right information is present in the phone number field
    Then Verify the right information is present in the email field
    When Verify "Send an application" button is available and clickable


  Scenario: User can open the Community Page
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click on the settings option on the left side
    When Click on the Community button
    When Verify that the Community page opens
    Then Click the “Contact support” button is available and clickable

  Scenario: User can open the Contact Us page
    Given Open the main page
    When Login to the main page with username iarekitkit@gmail.com
    When Login to the main page with password $onicx89
    Then Click continue button
    Then Click on the settings option on the left side
    When Click on the Contact Us button
    Then Verify the correct page opens
    Then Verify there are at least 4 social media icons
    Then Verify “Connect the company” button is available and clickable
