from flask import Flask, render_template, request
import os

app = Flask(__name__)

def convert_base(number, from_base, to_base):
    try:
        decimal = int(number, from_base)
        if to_base == 2:
            return bin(decimal)[2:]
        elif to_base == 8:
            return oct(decimal)[2:]
        elif to_base == 10:
            return str(decimal)
        elif to_base == 16:
            return hex(decimal)[2:].upper()
    except:
        return "แปลงไม่ได้"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    number = ""
    from_base = "10"
    to_base = "2"

    if request.method == "POST":
        number = request.form["number"]
        from_base = request.form["from_base"]
        to_base = request.form["to_base"]

        result = convert_base(number, int(from_base), int(to_base))

    return render_template(
        "index.html",
        result=result,
        number=number,
        from_base=from_base,
        to_base=to_base
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
