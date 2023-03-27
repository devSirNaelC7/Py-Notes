def createNote(notes=[], note=''):
    notes.append('\033[31m' + note + '\033[0m')
    return 'Note added'


def readNotes(notes=[]):
    if len(notes) == 0:
        return 'You have no notes to display.'
    return notes


def updateNote(notes=[]):
    if len(notes) == 0:
        return 'There are no notes to update.'

    index = int(input('Enter the index of the note you want to update:'))

    if index <= 0 or index > len(notes):
        return 'The index does not match any notes.'

    notes[index - 1] = input('Enter note update:')
    return 'Updated note.'


def deleteNote(notes=[]):
    index = int(input('Enter the index of the note you want to delete:'))
    if index > len(notes) or index < 0:
        return 'Index entered does not match any note.'
    del notes[index - 1]
    return 'Deleted note.'


def finalized(notes=[]):
    if len(notes) == 0:
        return 'No notes to finish.'
    index = int(input('Enter the index of the note you want to end:'))
    if index <= 0 or index > len(notes):
        return 'The index does not match any notes.'
    notes[index-1] = '\033[32m' + notes[index - 1] + '\033[0m'
    return 'Completed note.'
