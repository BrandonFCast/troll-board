import pyperclip as cb

text = "working" # in this variable we're going to save the clipboard value
oldWord = "hi" # is the word we are going to replace
newWord = "miau" # is the word that will replace the old word

# this is the help message that will be explained to the users
helpMsg = "\'endtroll\' = program exit\n\'oword:x\' = Indicates the word that will be replaced, where 'x' is the word\n\'nword:x\' = indicates the replacement (x is the replacement) \n\'info\' = shows the word to be replaced and its replacement"

def evaluateCommand (text) :
    sections = text.split(":")
    commandKey = sections[0]
    commandValue = sections[1] if len(sections) > 1 else ""

    if (not commandKey in commands): return False

    commands[commandKey](commandValue)
    return True

def setOldWord (value) :
    global oldWord
    oldWord = value

def setNewWord (value) :
    global newWord
    newWord = value

def showInfo (value) :
    cb.copy("palabra a remplazar: " + oldWord + "\npalabra nueva: " + newWord)

def showHelp (value) :
    cb.copy(helpMsg)

# to add new commands insert the key word and the command function,
# it receives a parameter (the text after colon)
commands = {
    "oword": setOldWord,
    "nword": setNewWord,
    "info": showInfo,
    "help": showHelp
}

while (cb.paste() != "endtroll") :
    cb.waitForNewPaste()
    text = cb.paste() # the text in the clipboard

    # evaluate the clipboard text, if it's not a command we're going to replace the words
    if not evaluateCommand(text) :
        text = text.replace(oldWord, newWord)
        cb.copy(text)