import topsis
from bottle import Bottle, template, request

app = Bottle()
output = {}


@app.route('/')
def index():
    """Home Page"""
    return template("./templates/index.tpl", result="", resultname="")


@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""

    files = request.forms.get('files')
    weights = request.forms.get('weights')
    impact = request.forms.get('impact')
   
    output = topsis.webService(files,weights,impact)
    return template("./templates/index.tpl",
                    result=output['result'],
                    resultname=output['resultname']
                    )


if __name__ == '__main__':
    app.run(debug=True)
