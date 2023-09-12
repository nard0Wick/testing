def isPalindrome(s):  
    """ 
    >>> Función palindromo recibe un string y retorna un valor booleano según se trate o no de un palindromo. 
    >>> NO maneja acentos!.
    """
    def toChars(s):  
        #Convierte los caracteres en minúsculas y elimina los espacios. 
        s = s.lower() 
        ans = '' 
        for c in s: 
            if(c in 'abcdefghijklmnopqrstuvmxyz'): 
                ans = ans + c 
        return ans 
    def isPal(s):  
        #Define si se trata de un palíndromo. 
        if len(s) <= 1: 
            return True 
        else:  
            return s[0] == s[-1] and isPal(s[1:-1]) 
    
    return isPal(toChars(s))

#print(isPalindrome('A luna ese anula.')) 
#print(isPalindrome('A mama, Roma le aviva el amor a papa, y a papa, Roma le aviva el amor a mama.')) 
#print(isPalindrome('Aji traga la lagartija.'))  

