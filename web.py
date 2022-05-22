from flask import Flask
app = Flask("__name__name")

@app.route('/')
def index()
  return 'hello-world'
