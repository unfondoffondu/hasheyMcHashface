import hashlib

#MAKE SURE YOUR WORD LIST IS NAMED PROPERLY HERE.
with open("words.txt") as f:
    episodes = f.read().splitlines()
    
#PUT YOUR HASH_STRING HERE
string_of_hash = "string your hash here" 
#YOU CAN ADD MORE IF YOU WANT JUST CHANGE THE CONDITIONAL STATEMENT BELOW
nums = [i for i in range(101)]
for i in episodes:
    for j in nums:
        guess = i + str(j)
        hashed = hashlib.md5(guess.encode('utf8')).hexdigest()
        if hashed == string_of_hash:
            print(guess, "  DING DING DING DING DING DING", str(hashed))
        
        
        
