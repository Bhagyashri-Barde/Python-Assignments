# Program - Accept 1 character and chekcks whether
# It is Vowel or Consonant

def ChkVowel(chr):
    if(chr in "aeiouAEIOU"):              # check chr is avilable in given string "aeiouAEIOU"

    # if(chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u' or 
    #    chr == 'A' or chr == 'E' or chr == 'I' or chr == 'O' or chr == 'U'):

        return True
    else:
        return False
    
def main():
    Char = input("Enter your chracter : ")

    Ret = ChkVowel(Char)
    
    if (Ret == True):
        print(Char,"is Vowel")
    else:
        print(Char,"is Consonant")

if __name__ == "__main__":
    main()