alphabets= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=1,2,3,4,5,6,7,8,9,0
def encryption(plain_text,shift_index):
    cipher=""
    for character in plain_text:
        position=alphabets.index(character)
        new_position=(position + shift_index)%26
        cipher +=alphabets[new_position]
        print(f"Here is your encrypt data :{cipher}")




