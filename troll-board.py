import pyperclip as cb

text = "funcionando" # in this variable we're going to save the clipboard value
oldWord = ";" # is the word we are going to replace
newWord = "miau" # is the word that will replace the old word

# this is the help message that will be explained to the users
helpMsg = "\'endtroll\' = termina el programa\n\'oword:x\' = cambia la palabra a remplazar por x y la palabra nueva es igual pero con nword\n\'info\' = muestra las palabras"

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
    cb.copy("hola guapote, los comandos funcionan copiandolos\n" + helpMsg)

commands = {
    "oword": setOldWord,
    "nword": setNewWord,
    "info": showInfo,
    "help": showHelp
}

while (cb.paste() != "endtroll") :
    cb.waitForNewPaste()
    text = cb.paste()

    # if the clipboard text is not a command we're going to replace the words
    if not evaluateCommand(text) :
        text = text.replace(oldWord, newWord)
        cb.copy(text)