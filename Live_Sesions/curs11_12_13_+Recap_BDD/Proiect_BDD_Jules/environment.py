from browser import Browser
from pages.sign_up_page import Sign_up_page

# before_all este o metoda care este recunoscuta de libraria behave si care se va executa inainte de toate testele


def before_all(context):
    # context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser()
    context.sign_up_object = Sign_up_page()


# after_all este o metoda care este recunoscuta de libraria behave si care se va executa dupa toate testele
def after_all(context):
    context.browser.close()
