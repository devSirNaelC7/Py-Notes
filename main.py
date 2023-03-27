import crud

notes = []

menu = ('1 - Add note\n'
        '2 - List notes\n'
        '3 - Edit note\n'
        '4 - Delete note\n'
        '5 - Finalized note\n'
        '0 - Exit\n')

print('Welcome to PyNotes!\n')

print(menu)

while True:
    print('Enter the number that corresponds to your option: ')
    option = int(input())
    if option < 0 and option > 4:
        print('The value entered does not match any option.')
    if option == 0:
        print('Application closed.')
        break
    elif option == 1:
        print(crud.createNote(notes, input('Enter you note:')))
    elif option == 2:
        for note in notes:
            print(note)
    elif option == 3:
        print(crud.updateNote(notes))
    elif option == 4:
        print(crud.deleteNote(notes))
    elif option == 5:
        print(crud.finalized(notes))
