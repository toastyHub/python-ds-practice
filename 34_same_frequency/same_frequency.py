def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    
    if len(str1) != len(str2):
        return False
    count = len(str1)
    for char in str1:
        while count > 0:
            if str1.count(char) == str2.count(char):
                str1 = str1.replace('char', '')
                str2 = str2.replace('char', '')
                count -= 1
                break
        return True
    return False   