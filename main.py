def mysplit(strng):
    #
    # coloca tu código aquí
    #
    new = [] 
    word=''
    strng = strng.strip() #elimina espacios en blanco al principio y al final de la cadena strng
    
    if strng.isspace(): #si strng es una cadena vacia devuelve una lista vacia
        return new
    
    for x in range (len(strng)):
        if strng[x]!= chr(32):
            word += strng[x]
        else:
            new.append(word)
            word = ''
    
    if word != '': #suma la ultima palabra a la lista new ya que al no tener espacio al final no puede incluirse en el bucle for
        new.append(word)
    
    return new

# Test de la funcion "mysplit"

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
