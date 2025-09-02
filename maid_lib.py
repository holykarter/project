'''var1 = input('the name of your best firend')
var2 = input('one thing you like about him')
var3 = input('where you best friend lives')

story = my best friend is {var1}, i loves me , and i love him , /n
i like the way he {var2} , it also fun with him , now we lived {var3}

print(story)'''

# a more sophisticated version of this program

# test dict
'''d = {'name' : 'austin',
    'age' : 10,
     'job' : "adventure travel guide"}  mistake : used = instead of :''' 


# principale code 
class MadLib:
	def __init__(self, prompt, story):
		self.answer = {}
		self.story = story 
		self.prompt = prompt
	
	def get_inputs(self):
		print('the game start , provide the following word:' )
		for key, text in self.prompt.items():
			answer = input(f"{text}: ")
			self.answer[key] = answer

	def for_story(self):
		return self.story.format(**self.answer)  # format story 

	def play(self):
		self.get_inputs()
		final_story = self.for_story()
		print("\n--- your Story ---")
		print(final_story)
		
 # story template
text_base =''' 
I met {adjective} {animal_name} at the zoo. It had  {color} fur
and a long {body_part}.My new friend the {animal_name} loves to 
{verb_present_tense}
and play in the mud. I hope to see it again soon !
''' 
# prompt to ask  the user
prompt = {
   "adjective": "an adjective",
   "animal_name" : "an animal name",
   "color" : " a color", 
   "body_part" : " a body part (e.g., tail, ear)",
   "verb_present_tense": "a present-tense verb (e.g., run, fly)"
}

madLib1 = MadLib(prompt, text_base)
madLib1.play()


'''personal remark , i make mistake about variable , didn't use the same name in text_base and prompt ''' 
