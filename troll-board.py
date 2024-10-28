import pyperclip as cb

text = "funcionando"
oldWord = ";"
newWord = " miuau"
cb.copy(text)
helpMsg = "\'endtroll\' = termina el programa\n\'oword:x\' = cambia la palabra a remplazar por x y la palabra nueva es igual pero con nword\n\'info\' = muestra las palabras"

while (cb.paste() != "endtroll") :
    cb.waitForNewPaste()
    text = cb.paste()
    if (text[:6] == "oword:") :
        oldWord = text[6:]
    elif (text[:6] == "nword:") :
        newWord = text[6:]
    elif (text[:4] == "info") :
        cb.copy("palabra a remplazar: " + oldWord + "\npalabra nueva: " + newWord)
    elif (text[:4] == "help") :
        cb.copy("hola guapote, los comandos funcionan copiandolos\n" + helpMsg)
    else :
        text = text.replace(oldWord, newWord)
        cb.copy(text)