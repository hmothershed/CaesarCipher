#CAESAR CIPHER ENCRYPTION AND DECRYPTION

import os
import sys
import time
from time import sleep

#--------------------------------------ANIMATION OF TEXT-----------------------------------------------
def animate(text):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(0.05)
#------------------------------------------------------------------------------------------------------
    
#--------------------------------ANIMATION OF PROGRESS BAR---------------------------------------------
def progressbar(it, prefix="", size=60, out=sys.stdout): 
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count}", end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)
#------------------------------------------------------------------------------------------------------

#----------------------------------ENCRYPTION FUNCTION-------------------------------------------------
def encrypt():

    animate("\nYou've selected to encrypt a plaintext message.")

    animate("\nYour message can be a mix of symbols and letters, but no numbers. \n")
    animate("Please enter a message: ")
    msg = input("")


    encrypted_text = ""

    while True:
        key = int(input("Enter a shift key (0-25): "))
        # the key is based on 26 letters of alphabet
        if key < 26:
            for i in range(len(msg)):
              # ord() will give us the ASCII of space char, which is 32
                if ord(msg[i]) == 32:  
                    encrypted_text += chr(ord(msg[i]))
                    # chr() will convert ASCII back to character

                elif ord(msg[i]) + key > 122:
                    # after 'z' move back to 'a', 'a' = 97, 'z' = 122
                    temp = (ord(msg[i]) + key) - 122
                    # subtracting 122 to get a lower int and adding it in 96
                    encrypted_text += chr(96+temp)

                elif (ord(msg[i]) + key > 90) and (ord(msg[i]) <= 96):
                    # moving back to 'A' after 'Z'
                    temp = (ord(msg[i]) + key) - 90
                    encrypted_text += chr(64+temp)

                else:
                    # in case of letters being between a-z and A-Z
                    encrypted_text += chr(ord(msg[i]) + key)
            break;
        
        else:
        #user inputs a number out of range
            animate("Wrong choice. The shift key you've entered must be in range from 0 to 25.")
            animate("\nTry again... ")
            continue
            

    #progress bar animation is called
    for i in progressbar(range(100), "Computing: ", 40):
        time.sleep(0.06)
    os.system('clear')
    
    #display the message
    print(80 * "-")
    animate("Your encrypted message is ----> " + encrypted_text + "\n")
    print(80 * "-")
#------------------------------------------------------------------------------------------------------

#-----------------------------------DECRYPTION FUNCTION------------------------------------------------
def decrypt():
    animate("\nYou've selected to decrypt an encrypted message.")

    animate("\nYour message can be a mix of symbols and letters, but no numbers. \n")
    animate("Please enter the encrypted text: ")
    encrp_msg = input("")
    encrp_msg = encrp_msg.lower()

    decrypted_text = ""

    while True:
        decrp_key = int(input("Enter a reverse shift key (0-25): "))
        #decryption key will do the opposite of the encrytion key
        if decrp_key < 26:
            for i in range(len(encrp_msg)):
                if ord(encrp_msg[i]) == 32:
                    decrypted_text += chr(ord(encrp_msg[i]))

                elif ((ord(encrp_msg[i]) - decrp_key) < 97) and ((ord(encrp_msg[i]) - decrp_key) > 90):
                    # subtract key from letter ASCII and add 26 to current number
                    temp = (ord(encrp_msg[i]) - decrp_key) + 26
                    decrypted_text += chr(temp)

                #for symbols    
                elif (ord(encrp_msg[i]) - decrp_key) < 65:
                    temp = (ord(encrp_msg[i]) - decrp_key) 
                    decrypted_text += chr(temp)

                else:
                    decrypted_text += chr(ord(encrp_msg[i]) - decrp_key)
            break;
        
        else:
        #user inputs a number out of range
            animate("Wrong choice. The reverse shift key you've entered must be in range from 0 to 25.")
            animate("\nTry again... ")
            continue
    

    #progress bar animation is called
    for i in progressbar(range(100), "Computing: ", 40):
        time.sleep(0.06)
    os.system('clear')

    #display the message
    print(80 * "-")
    animate("Your decrypted message is ----> " + decrypted_text + "\n")
    print(80 * "-") 
#------------------------------------------------------------------------------------------------------

#----------------------------------------MAIN FUNCTION-------------------------------------------------
def main():
    animate("Welcome to Caesar Cipher Encryption Decryption Generator")
    
    #input user's choice
    while True:
        animate("\nType '1' to ENCRYPT")
        animate("\nType '2' to DECRYPT")
        animate("\nType '3' to EXIT")
        animate("\nEnter your choice: ")
        choice = int(input(""))
        
        if choice == 1:
          #call the encryption function
            encrypt()

          #after the encryption function is finished ask the user if they would want to continue
            animate("Would you like to continue? (Y/N) ")
            keep_going = input(" ")
            keep_going = keep_going.capitalize()
            #if answer is given in lowercase we will capitalize it to accept
            if keep_going == 'Y':
                continue
            else:
                animate("GOODBYE.")
            break;

        elif choice == 2:
          #call the decryption function
            decrypt()
            
          #after the decryption function is finished ask the user if they would want to continue
            animate("Would you like to continue? (Y/N) ")
            keep_going = input(" ")
            keep_going = keep_going.capitalize()
            #if answer is given in lowercase we will capitalize it to accept
            if keep_going == 'Y':
                continue
            else:
                animate("GOODBYE.")
            break;

        elif choice == 3:       #end the program
            animate("\nGOODBYE.")
            break;

        else:
        #if user gives a number that's not 1, 2, or 3 it will repeat the loop
        #asking for a correct number
            print("\nWrong choice. PLEASE PLEASE PLEASE")
#------------------------------------------------------------------------------------------------------            continue

if __name__ == "__main__":
    main()
