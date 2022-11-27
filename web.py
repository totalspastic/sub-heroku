from flask import Flask
app = Flask(__name__)

@app.route('/')
n=int(input("Enter first number:\n"))
m=int(input("Enter second number:\n"))
def subtract(a,b):
  subtract=a-b
  return subtract
print("Result: ", subtract(n,m))
