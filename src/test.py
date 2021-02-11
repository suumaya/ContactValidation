import main
if __name__ == "__main__":
    # One time:
    main.resetAll()
    main.run()

    # # Many times:


    while True:
        x = input("""Please Select one of the following:
                  1. Add Person
                  2. Delete Person
                  3. List all persons
                  4. Exit\n""")
        if x == '1':
            main.addPerson()
        else:
            if x == '2':
                by_value = input("Do you prefer to delete by phone press 1, other wise press 2:\n")
                main.delPerson(by_value)
            else:
                if x == '3':
                    main.listAll()
                else:
                    break