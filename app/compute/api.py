from app import app


@app.route("/api/compute/<int:a>/<int:b>")
def compute(a, b):
    return "computing: (%s + %s) = %s" % (a, b, a + b)
