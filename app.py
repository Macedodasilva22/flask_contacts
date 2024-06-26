from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Pedro!</p>"
my_contacts = [{"name": "pedro", "age": 27} , {"name": "henry", "age": 30}]
    
   

@app.route("/contacts/<int:usernumber>")
def usernumber(usernumber):
    return f"user is {usernumber}"

@app.route("/contacts")
def contacts():
    return f"{my_contacts}"

@app.route("/destination")
def destination():
    return "Please enter a destination"

if __name__ == "__main__":
    print("Starting app with debug mode:", True)
    app.run(debug=True, port=9000)