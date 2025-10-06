 # FILE NAME - grade_converter.py

# NAME: Mike Rahne
# DATE: 10/6/2025 
# BRIEF DESCRIPTION: My grade_converter submission 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    grade_convert()
def grade_convert():

    print('===== Grade Converter =====')
    grade = int(input('Enter a numerical grade (1-100): '))

    if grade >= 100:
        print('A+')
    elif grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 65:
        print('D')
    else:
        print('F')



main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
# I guess my advice would be to always look at the repo first. I didn't see that the code was already in here (I knew it would be in one of them, as you said - I didn't know it was this one
# and I originally had the last line as an elif <65, which worked, but I guess this way is easier.





'''
