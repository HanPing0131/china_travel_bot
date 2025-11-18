from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User
from .forms import RegisterForm, LoginForm
from .services.nlp_service import answer_travel_question

from flask import current_app as app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/features")
@login_required
def features():
    """
    Feature directory that user sees after login.
    For now, only General Q&A is implemented (clickable).
    Other features are marked as 'coming soon'.
    """
    feature_list = [
        {"name": "General China Travel Q&A", "endpoint": "qna", "implemented": True},
        {"name": "Currency Exchange", "endpoint": "fx", "implemented": False},
        {"name": "Destination Recommender", "endpoint": "recommend", "implemented": False},
        {"name": "City Image Gallery", "endpoint": "city_images", "implemented": False},
        {"name": "Attraction Bilingual Introduction", "endpoint": "attraction", "implemented": False},
        {"name": "Real-time Weather", "endpoint": "weather", "implemented": False},
        {"name": "Travel Budget Estimator", "endpoint": "budget", "implemented": False},
        {"name": "Packing Checklist", "endpoint": "packing", "implemented": False},
        {"name": "Chinese Specialty Shopping Links", "endpoint": "shopping", "implemented": False},
        {"name": "Chinese Travel Phrase Helper", "endpoint": "phrases", "implemented": False},
        {"name": "English → Chinese Translation", "endpoint": "translate_text", "implemented": False},
        {"name": "Chinese Text-to-Speech", "endpoint": "tts", "implemented": False},
        {"name": "Photo-based Attraction / City Guess", "endpoint": "photo_guess", "implemented": False},
        {"name": "Itinerary Email & 24h Reminder", "endpoint": "itinerary_email", "implemented": False},
    ]
    return render_template("features.html", features=feature_list)


@app.route("/qna", methods=["GET", "POST"])
@login_required
def qna():
    """
    General China Travel Q&A.
    GET: show empty form
    POST: call answer_travel_question() and show answer
    """
    answer = None
    question = None

    if request.method == "POST":
        question = (request.form.get("question") or "").strip()
        if question:
            answer = answer_travel_question(question)

    return render_template("qna.html", question=question, answer=answer)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("features"))

    form = RegisterForm()
    if form.validate_on_submit():
        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash("This email is already registered.", "warning")
            return redirect(url_for("register"))

        user = User(
            name=form.name.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            nationality=form.nationality.data,
            travel_preferences=form.preferences.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("features"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Login successful.", "success")
            next_page = request.args.get("next")
            # After login, go to the feature directory instead of profile
            return redirect(next_page or url_for("features"))
        else:
            flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)

