def mysplit(strng):
    #
    # coloca tu código aquí
    #
    new = []
    word=''
    
    if strng.isspace():
        return new
    
    for x in range (len(strng)):
        if strng[x]!= chr(32):
            word += strng[x]
                
        else:
            new.append(word)
            word = ''
    
    if word != '':
        new.append(word)
    
    return new

# Test de la funcion "mysplit"

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
