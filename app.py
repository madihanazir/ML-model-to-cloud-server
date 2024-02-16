from flask import Flask, request

app= Flask(__name__) #flask obj instantiating the flak lib

#routing is a mechanism user comes root of folder what needs to be done
@app.route('/')

def hello_world():
    return "Hello World"

@app.route('/spamorham', methods=['GET', 'POST'])
def spamorham():
    message = request.args.get("message")
    return message

if __name__== '__main__':
    app.run()
    #must have virtual env
    #and python version compatible
#create an instance of virtual env on ur workspace
