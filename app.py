import os
import subprocess

# 1-ԻՆ ՈՒՂՂՈՒՄ. Գաղտնի կոդը կարդում ենք Environment-ից (ոչ թե hardcode ենք անում)
AWS_SECRET_KEY = os.environ.get("AWS_Secret_KEY")

def execute_user_command(user_input):
	## 2-ՐԴ ՈՒՂՂՈՒՄ. os.system-ի փոխարեն օգտագործում ենք անվտանգ subprocess.run
	# Սա թույլ չի տա Command Injection անել
	subprocess.run(["echo", user_input])

print("App is runnig safely and successfully!")
