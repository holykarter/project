''' 
story : my best friend is {var1}, i loves me , and i love him , 
i like the way he {var2} , it also fun with him , now we lived {var3}


'''
var1 = input('the name of your best friend')  # changed firend for friend
var2 = input('one thing you like about him')
var3 = input('where you best friend lives')

story = f'''my best friend is {var1}, i loves me , and i love him , 
i like the way he {var2} , it also fun with him , now we lived {var3}''' # a triple quote work for multiple line
# mistake f"" instead of f''' ''' (phrase \n phrase 2)


print(story)
