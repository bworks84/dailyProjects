# collect email from user
# split the email using the @, the first part as the user name,
# the second part is the domain
# split domain using '.'

def emailSlicer():
    print("Welcome to the email Slicer!")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split('.')

    print("Username : ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


emailSlicer()
