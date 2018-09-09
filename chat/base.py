import aiml
import os


kernel = aiml.Kernel()

# checking whether a brain file exists 
# if not create a new one
# also load the std-startup.xml

if os.path.isfile("chat/bot_brain.brn"):
		kernel.bootstrap(brainFile = "chat/bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "chat/aiml/standard/std-startup.xml",commands = "load aiml b")
	kernel.saveBrain("chat/bot_brain.brn")
