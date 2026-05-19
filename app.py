import os

# 1-ին ՍԽԱԼ. Գաղտնի կոդը (Token) թողել ենք հենց կոդի մեջ
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

def execute_user_command(user_input):
    # 2-րդ ՍԽԱԼ. Վտանգավոր ֆունկցիա, որը թույլ է տալիս Command Injection անել
    os.system("echo " + user_input)

print("App is running successfully!")
