# caesar cipher   
import art

#logo from art module
print(art.logo)

#process starts
do_process=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
is_game="no"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encode functon
def encrypt(message,shifted_number):
    user_msg_list=[]
    if shifted_number>26:
        shifted_number=shifted_number%26
        print(shifted_number)    
    for i in user_message:
        user_msg_list.append(alphabet[alphabet.index(i)+shifted_number])
    print(f"the encoded message is {''.join(user_msg_list)}")  

#decode function
def decrypt(message,shifted_number):
    user_msg_list=[]
    if shifted_number>26:
        shifted_number=shifted_number%26
        print(shifted_number)
    for i in user_message:
        user_msg_list.append(alphabet[alphabet.index(i)-shifted_number])
    print(f"the decoded message is {''.join(user_msg_list)}")

#user_experience    
while is_game!="yes":
    if do_process.lower()=='encode':
        user_message=input("Type your message:\n").lower()
        shift_number=int(input("Type the shift number:\n"))
        encrypt(message=user_message,shifted_number=shift_number)
        is_user=input("type 'yes' to continue,type 'no' to break").lower()
        if is_user=='yes':
            do_process=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
            is_game='no'
        else:
            is_game='yes'     
    elif do_process.lower()=='decode':
        user_message=input("Type your message:\n").lower()
        shift_number=int(input("Type the shift number:\n"))
        decrypt(message=user_message,shifted_number=shift_number)
        is_user=input("type 'yes' to continue,type 'no' to break").lower()
        if is_user=='yes':
            do_process=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
            is_game='no'
        else:
            is_game='yes'  
