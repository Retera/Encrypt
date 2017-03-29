def encrypt(i, tokey):
    """
    function encrypt takes integer i and string tokey,
    returns string
    
    changes the number i into a number in a base determined
    by the length of the tokey using the characters
    provided in the tokey in the order provided
    """
    Base = len(tokey) #the base that we convert to
    curpow = 0  #the current power of the base that we are working with
    out = ''    #the output string, declared beforehand
    
    while i>=Base**curpow: #increase the current power until it is 
        curpow+=1          #greater than the greatest power in the input i
    
    curpow-=1              #reduce the curpow by 1 to put it in the input
    
    while curpow >= 0:     #convert from number to string
        num = int(i/(Base**curpow)) #get the number of instances of the current power in the input
        out+= str(tokey[num])    #add the letter/number to the output
        i-=num*Base**curpow #reduce the input to prevent reuse of values
        curpow-=1           #reduce the power by one
    
    return out              #return the output
    
def unencrypt(input, fromkey):
    """
    function unencrypt takes string input and string/list/tuple fromkey, 
    returns int
    
    changes the string input into a base 10 number by coverting the
    string using a base determined by the length of the tokey and
    using the characters provided in the tokey in the order provided
    """
    Base = len(fromkey)         #base we convert from
    length = len(input)         #length of the input
    seglength = len(fromkey[0]) #length of the segments the input is cut into
    out = 0                     #declare the output
    pos = 0                     #declare position variable
    
    while pos <= length/seglength:  #convert from string to int
        rtlpos=length-pos           #get the current position in the input from the right
        #this several step part gets the current character or set of characters from the imput
        #and gets the first occurance in the key
        #that index is multiplied by the base to the current power (divided by seglength to make up for larger increments)
        #finally, that is converted to an integer and added to the output
        out+=int(fromkey.index(input[rtlpos-seglength:rtlpos]))*Base**int(pos/seglength)
        pos+=seglength
        
    return out
    
def dblencrypt(input, fromkey, tokey):
    """
    function dblencrypt takes string input and string/list/tuple fromkey, tokey,
    returns string
    
    performs two conversions on the input changing it from the fromkey's
    base to the tokey's base using the characters provided in order
    """
    return encrypt(unencrypt(input, fromkey), tokey)
   
def dblencryptx(input, tokey, fromkey):
    return encrypt(unencrypt(input, fromkey), tokey)
   

print dblencrypt('97299372997492794278920761936891684', '0123456789', 'abcdefghijklmnopqrstuvwxyz ')
print dblencrypt('97299372997492794278920761936891684', '0123456789', 'qwertyuiopasdfghjklzxcvbnm ')

print dblencrypt('Apparently, I have just invented a simple language.', 'abcdefghijklmnopqtsruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.0123456789!@#$%^&*()"', 'ekjlafghicdbmnypqrstuxvwozECBDAFGHIJKLNMUQPTRSOXVWYZ ,.0123456789!@#$%^&*()"')
print dblencrypt('posted', 'abcdefghijklmnopqtsruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.0123456789!@#$%^&*()"', 'abcegnouyk .,')
print dblencrypt('Shis is e saquanja.', 'abcdefghijklmnopqtsruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.0123456789!@#$%^&*()"', 'ekjlafghicdbmnypqrstuxvwozECBDAFGHIJKLNMUQPTRSOXVWYZ ,.0123456789!@#$%^&*()"')

print dblencrypt('97299372997492794278920761936891684', '0123456789', 'qwertyuiopasdfghjklzxcvbnm ')

print dblencrypt('posted', 'abcdefghijklmnopqtsruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.0123456789!@#$%^&*()"', '01')


#NOTE; this does not work:
#dblencrypt(['3','0','0','0'], ['10','30','00'], 'abcde')
#the input cannot be a list, tuple, or real