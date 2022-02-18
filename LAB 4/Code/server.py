from black import out
import extractFeatures
from bottle import Bottle, template, request

app = Bottle()
output = {}

@app.route('/')
def index():
    """Home Page"""
    return template("./templates/index.tpl", result="", log="", resultname="", logname="")

@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""

    files = request.forms.get('files')
    print(files)
    output = extractFeatures.webService(files)
    return template("./templates/index.tpl",
                    result=output['result'],
                    log=output['log'],
                    resultname=output['resultname'],
                    logname=output['logname'])

if __name__ == '__main__':
    app.run(debug=True)
