import os
# from bottle import route, run

from flask import Flask
app = Flask(__name__)

@app.route('/')

@app.route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name

# @route('/page1/:greet','boh')
# def page1(greet='mikey',boh='boh'):
# mystring +=  '<b>Boh %s!</b>' % boh    
    
@app.route('/page1/:greet')
def page1(greet='mikey'):
    mystring = '''<html>
    <head><title>Page 1</title></head>
    <body>'''
    mystring += '<p>Bla, Bla, Bla.....</p>'
    mystring +=  '<b>Ciao %s!</b>' % greet
    mystring += '</body></html>'    
    return mystring

@app.route('/page2/:greet','boh')
def page1(greet='mikey',boh='boh'):
    mystring = '''<html>
    <head><title>Page 1</title></head>
    <body>'''
    mystring += '<p>Bla, Bla, Bla.....</p>'
    mystring +=  '<b>Ciao %s!</b>' % greet
    mystring +=  '<b>Boh %s!</b>' % boh
    mystring += '</body></html>'    
    return mystring

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    app.run(host='0.0.0.0', port=port)
