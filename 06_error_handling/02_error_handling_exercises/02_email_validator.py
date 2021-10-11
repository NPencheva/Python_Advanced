class NameTooShortError(Exception):
    """name is <= 4 symbols"""
    pass


class MustContainAtSymbolError(Exception):
    """@ symbol not contained in e-mail"""
    pass


class InvalidDomainError(Exception):
    """invalid domain"""
    pass


valid_domains = {"com", "bg", "org", "net"}

while True:
    input_text = input()
    if input_text == "End":
        break
    else:
        e_mail_parts = input_text.split("@")
        name = e_mail_parts[0]
        if len(e_mail_parts) < 2:
            raise MustContainAtSymbolError("Email must contain @")

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        domain_name = e_mail_parts[1]
        domain_name_parts = domain_name.split(".")

        domain = domain_name_parts[-1]
        if domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")
