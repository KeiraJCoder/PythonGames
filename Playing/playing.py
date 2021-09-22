# import string
# # import the string library


# sample_text = "when you try your best but you dont succeed. when you get what you want but not what you need."
# # enter the text you want to capitalize

# result = string.capwords(sample_text)
# # make the result capitalized for each start of word

# print(result)
# # print the result

# original_data =input()
# list = original_data.split(".")
# if original_data.endswith('.'):
#     list.remove('')

# for x in list:
#     stripper= x.strip().capitalize() +"."
#     print(stripper)
    
num = 126

if num % 3 == 0 and num % 7 == 0:
    print ("Fizzbuzz") 
elif num % 7 == 0:
    print ("Buzz") 
elif num % 3 == 0:
    print ("Fizz")
else:
    print (num)