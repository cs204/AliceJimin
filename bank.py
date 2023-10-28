name = input("Приветствие: ")
if name=="здравствуйте" or name=="Здравствуйте"or name=="здравствуйте Крамер"or name=="Здравствуйте Крамер" or name=="здравствуйте человек" or name=="Здравствуйте человек" :
	print("$0")
elif name.startswith("з"):
	print("$20")
else:
	print("$100")