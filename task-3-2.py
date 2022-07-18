def personalInformation(name, surname, birth_year, residence, email, phone_number):
    print("Author's Personal Information:")
    print(name, surname, birth_year, residence, email, phone_number, sep = ', ');

personalInformation(surname = 'Pratchett', name = 'Terry',
                    residence = 'Glasgow', birth_year = 1948,
                    phone_number = '+44 0980123123',
                    email = 't.pratchett@gmail.com');