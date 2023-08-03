from flask import Flask, render_template, request
app = Flask(__name__)

board = [" " for x in range(9)]

@app.route("/")
def index():
    return render_template("index.html", board=board)

@app.route("/play", methods=["POST"])
def play():
    global board
    row = int(request.form["row"])
    col = int(request.form["col"])
    player = request.form["player"]
    index = 3 * row + col
    if board[index] == " ":
        board[index] = player
    return render_template("index.html", board=board)

if __name__ == "__main__":
    app.run(debug=True)
