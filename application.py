from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def show_application():
    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def process_application():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    job_title = request.form.get("jobtitle")
    salary_req = request.form.get("salaryreq")
    return render_template("application-response.html", first=first_name, last=last_name, title=job_title, salary=salary_req)


if __name__ == "__main__":
    app.run(debug=True)
