

def dekrip():
    private_key = 123 #change xxx with your private key 
    N = 123 #change yyy with your private key
    
    cipher_TEXT = [123] #change ccc with your list of chiper text

    c_list = []
    a = []
    
    ptext = ""
    for c in cipher_TEXT:
        long_x = (int(c)**int(private_key)) % int(N)
        c_list.append(long_x)
        a = map(int,c_list)

        atext = a[0]

        ptext = ptext + chr(atext)
  
        c_list = []
         
        atext=""

    return ptext


print dekrip()


#print "Time:", time