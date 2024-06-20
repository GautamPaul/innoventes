import re


def check_valid_company_code(code):
    if len(code) == 5:
        code = code.lower()
        return re.search("[a-z][a-z][0-9][0-9][en]", code)
    return False
