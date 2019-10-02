from flask import Flask, render_template, request
app = Flask(__name__)


name = "Team OlympiadBowl Period 1"
roster = "Amanda Chen & Yevgeniy Gorbachev"

@app.route("/")

def root():
    print(app)
    return render_template('input.html',
                            team = name,
                            rost = roster)

@app.route("/auth")
def authenticate():
    # print("This is print(app): " + str(app))
    # print("This is print(request): " + str(request))
    # print("This is print(request.method): " + str(request.method))
    # print("This is print(request.headers): " + str(request.headers))
    # print("This is print(request.args): " + str(request.args))
    # print("This is print(request.form): " + str(request.form))
    # print("user input for username: {0}".format(request.args["username"]))

    return render_template('out.html',
                            team = name,
                            rost = roster,
                            arg_user = str(request.args["username"]),
                            arg_method = str(request.method),
                            greeting = "hello, {0}! If you're reading this, the server worked.".format(request.args["username"]))

if __name__ == "__main__":
    app.debug = True
    app.run()
