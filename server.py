from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/application-form')
def application_form():
    jobs = ['Software Engineer', 'QA Engineer', 'Product Manager']
    return render_template("application-form.html", jobs=jobs)


@app.route('/application-success', methods=["POST"])
def app_response():
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = int(request.form.get("salary_requiremment"))
    job = request.form.get("job")
    return render_template("application-response.html", first_name=first_name, last_name=last_name, salary=salary, job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
