from app import app


@app.route("/compute")
def hello():
    return "try hitting with /api/compute"
