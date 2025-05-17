import re

text1 = "Телефонний номер: (123) 456-7890"
text2 = "Телефонний номер: (123) 456-78-90"
text3 = "Телефонний номер: (123)456-78-90"
pattern = r'\(\d{3}\) \d{3}-(\d{2}-\d{2}|\d{4})'

for t in [text1, text2, text3]:
    match = re.search(pattern, t)
    if match:
        phone_number = match.group()
        print("Найдено номер телефону:", phone_number)


def is_valid_mail(mail_str:str) -> bool:
    """What can I do?"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, mail_str))


email = "user@domain.name"
print(is_valid_mail(email))