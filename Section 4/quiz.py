selection = int(input("Select an option from the choices below: \n"
                      "1. Learn Python\n"
                      "2. Learn Java\n"
                      "3. Learn C++\n"
                      "4. Learn MatLab\n"
                      "0. Exit\n"))
while selection != 0:
    if selection == 1:
        print("Lets learn Python!")
        print()
        selection = int(input("Select another option from the choices below: \n"
                              "1. Learn Python\n"
                              "2. Learn Java\n"
                              "3. Learn C++\n"
                              "4. Learn MatLab\n"
                              "0. Exit\n"))
    elif selection == 2:
        print("Lets learn Java!")
        print()
        selection = int(input("Select another option from the choices below: \n"
                              "1. Learn Python\n"
                              "2. Learn Java\n"
                              "3. Learn C++\n"
                              "4. Learn MatLab\n"
                              "0. Exit\n"))
    elif selection == 3:
        print("Lets learn C++!")
        print()
        selection = int(input("Select another option from the choices below: \n"
                              "1. Learn Python\n"
                              "2. Learn Java\n"
                              "3. Learn C++\n"
                              "4. Learn MatLab\n"
                              "0. Exit\n"))
    elif selection == 4:
        print("Lets learn MatLab!")
        print()
        selection = int(input("Select another option from the choices below: \n"
                              "1. Learn Python\n"
                              "2. Learn Java\n"
                              "3. Learn C++\n"
                              "4. Learn MatLab\n"
                              "0. Exit\n"))
    else:
        selection = int(input("Select another option from the choices below: \n"
                              "1. Learn Python\n"
                              "2. Learn Java\n"
                              "3. Learn C++\n"
                              "4. Learn MatLab\n"
                              "0. Exit\n"))
else:
    print("Goodbye!")
