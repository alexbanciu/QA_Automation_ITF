Feature: Jules.app sign-up tests
  Background:
    Given sign_in: I am a user on jules sign in page

    Scenario: I create an account

      When sign_in: I click sign up button
      When sign_up: I click personal radio button
      When sign_up: I click the continue button
      When sign_up: I send first name "Adela"
      When sign_up: I click continue first name button
      When sign_up: I send last name "Alexa"
      When sign_up: I click continue last name button
      When sign_up: I set my email to "abcd"
      Then sign_up: I receive message: Please enter a valid email address
