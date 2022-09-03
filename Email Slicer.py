

try:
    email = input("Enter your email id: ").strip()

    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]

    print(f"Username: {username}")
    print(f"Domain: {domain}")

except:
    print("Please enter valid email")
