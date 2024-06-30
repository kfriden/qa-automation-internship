# Created by Kait Kait at 6/29/2024
Feature: Registration Page

  Scenario: Verify user can input data on registration page
    Given Open registration page
    Then Input text for first and last name Kaitlyn Friden
    Then Input text for phone 888 350 1600
    When Input text for email cutelizzie@verizon.net
    Then Input text for password $onicx89
    When Verify info in first and last name field
    Then Verify info in phone number field
    Then Verify info in email field
    Then Verify info in password field
