question_prompt=["what colors are apples?\n (a)green/red\n (b)purple\n (c)Orange\n\n",
		 "what colors are banans?\n (a)Teal\n (b)magenta\n (c) yellow\n\n",
		 "what colors are straberries?\n (a) yellow\n (b)red\n (c)blue\n\n"]
class Questions():
	def __init__(self,prompt,answer):
		self.prompt=prompt
		self.answer=answer
questions=[Questions(question_prompt[0],"a"),
	   Questions(question_prompt[1],"b"),
           Questions(question_prompt[2],"c")
	  ]
def run_test(question):
	score=0
	for question in questions:
		answer=input(question.prompt)
		if answer==question.answer:
			score+=1
		#print("You got"+str(score)+"/"+str(len(question))+"correct")
	print("You got",score,"out of",len(questions))
run_test(questions)



