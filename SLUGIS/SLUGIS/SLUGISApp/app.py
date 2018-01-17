from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def showMachineList():
    return render_template('list.html')

if __name__ == "__main__":
    application.run(host='localhost')