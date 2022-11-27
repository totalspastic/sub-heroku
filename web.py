from flask import Flask
app = Flask(__name__)

@app.route('/')
def subtract(a,b):
  return(a-b)
print(subtract(5,3))
