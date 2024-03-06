from flask import Flask # iz datoteke flask importujemo Flask, tj framework

app = Flask(__name__) #pozivamo kode, inicijalizira se clasa flask, a name je parametar

@app.route('/') #kaye da kad naidjemo sa url pocetkom sa / tada pozivamo fun

def hello_world(): #define, definisi, ime funkcije sa parametrima unutar (), i vrati string
    return "Hello World"

if __name__ == '__main__': #ako je mname jednak name, ime jednako stringu imena tada pokrenuti app.
    app.run()

#space for continuiation
#anaconda.navigator
#vs code, install python stuff and coderunner
#open vs code THRU anaconda.navigator
#have render, gitlab, github
#install python 
#localhost