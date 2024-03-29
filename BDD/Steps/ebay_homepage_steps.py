from behave import *

@given("Home page: I am on ebay homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()

@when("Home page: I search for iphone from category Cell Phones & Accessories")
def step_impl(context):
    context.home_page_object.insert_search_value(product_name)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()

@then("Home page: I have at least 1000 results returned")
def step_impl(context):
    context.home_page_object.check_search_results(nr_of_results)