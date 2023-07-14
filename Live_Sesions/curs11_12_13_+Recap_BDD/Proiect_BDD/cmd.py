# 1. De instalat:
# Pycharm -> New Project (name it e.g.: BDD)
# ● pip install selenium (sau pip install -U selenium - pt update la zi)
# ● from packages, search and install webdriver-manager/webdrivermanager
# ● pip install behave (o librărie BDD care va interpreta și rula testele scrise în Gherkin)
# ● pip install behave-html-formatter (ne ajută să generăm rapoarte BDD)
#
# 2. Rulare fisier BDD:
#   ● behave -f html -o behave-report.html
# vs
#   ● behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
# unde:
# behave = pachetul / libraria care suporta framework-ul de bdd
# -f = formatter (detalii la linkul https://behave.readthedocs.io/en/stable/behave.html#command-line-arguments)
# html = o mapare a comenzii de generare raport de executie in format html
# -o = specifica faptul ca vrem sa scriem intr-un fisier extern in loc de consola
# behave-report.html = numele raportului de executie care vrem sa fie generat (custom name)