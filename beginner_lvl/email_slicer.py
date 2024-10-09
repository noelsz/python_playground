def email_slicer(email):
    return {"user": email.split('@')[0], "domain": email.split('@')[1]}

email_data = email_slicer("john@doe.com")
print(f"E-mail username: {email_data["user"]} \nDomain name: {email_data["domain"]}")

