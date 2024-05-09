# collect email from user
# split the email using the @, the first part as the user name, the second part is gonna be saved as domain
# split domain using .,

def main():
    print("Welcome to the email slicer: ") 
    print("")

    email_input = input("Give your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")


    print("username: ", username)
    print("domain: ", domain)
    print("extension: ", extension)
    print("-------------------------------------------------------")

while True:
    main()
