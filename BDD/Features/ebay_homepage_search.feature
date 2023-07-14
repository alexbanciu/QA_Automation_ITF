Feature: Test the search functionality in the homepage of ebay
    Scenario: Check that the user can make a simple search in the Ebay homepage
      Given Home page: I am on ebay homepage
      When Home page: I search for iphone from category Cell Phones & Accessories
      Then Home page: I have at least 1000 results returned


    Scenario: Check that the user can make an advanced search for a product
      When Home page: When I click on the advanced link
      When Advanced search page: I type pampers in the keyword textbox
      When Advanced search page: I choose exact words, exact order from keyword options
      When Advanced search page: I click search button
      Then Home page: I have at least 1200 results returned