from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Return homepage"""
    return render_template("homepage.html")

@app.route('/form')
def madlibs_form():
    """Return form to enter propmpts for Madlibs story"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def madlibs_story():
    """Return madlibs story using responses entered in form"""
    story_output = story.generate(request.args)
    return render_template("story.html", story_output=story_output)




