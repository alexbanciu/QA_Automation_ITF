from behave import *

@given(u'sign_in: I am a user on jules sign in page')
def step_impl(context):
    context.sign_up_object.navigate_to_sign_in_page()


@when(u'sign_in: I click sign up button')
def step_impl(context):
    context.sign_up_object.navigate_to_sign_up_page()


@when(u'sign_up: I click personal radio button')
def step_impl(context):
    context.sign_up_object.click_personal_button()


@when(u'sign_up: I click the continue button')
def step_impl(context):
    context.sign_up_object.click_continue_button()


@when(u'sign_up: I send first name "Adela"')
def step_impl(context):
    context.sign_up_object.send_first_name('Adela')


@when(u'sign_up: I click continue first name button')
def step_impl(context):
    context.sign_up_object.click_continue_first_name_button()


@when(u'sign_up: I send last name "Alexa"')
def step_impl(context):
    context.sign_up_object.send_last_name('Alexa')


@when(u'sign_up: I click continue last name button')
def step_impl(context):
    context.sign_up_object.click_continue_last_name_button()


@when(u'sign_up: I set my email to "abcd"')
def step_impl(context):
    context.sign_up_object.send_email('abcd')


@then(u'sign_up: I receive message: Please enter a valid email address')
def step_impl(context):
    context.sign_up_object.check_error_message_email()
