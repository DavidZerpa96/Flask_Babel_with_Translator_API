import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash, url_for, Response
from flask_mail import Mail, Message
import requests
from flask_cors import CORS
from markupsafe import Markup

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")
CORS(app)

def _(text: str) -> str:
    # Spanish-only site: keep templates readable even if they still call `_('...')`.
    # Mark safe because templates sometimes include HTML (e.g. <strong>) inside copy strings.
    return Markup(text)

@app.context_processor
def inject_template_globals():
    # Avoid hardcoding copyright year across templates.
    return {
        "current_year": datetime.utcnow().year,
        "_": _,
    }


@app.get("/robots.txt")
def robots():
    content = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {url_for('sitemap', _external=True)}",
            "",
        ]
    )
    return Response(content, mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    pages = [
        url_for("home", _external=True),
        url_for("work", _external=True),
        url_for("projects", _external=True),
        url_for("services", _external=True),
        url_for("resume", _external=True),
        url_for("contact", _external=True),
    ]
    xml = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"]
    for p in pages:
        xml.append("  <url>")
        xml.append(f"    <loc>{p}</loc>")
        xml.append("  </url>")
    xml.append("</urlset>")
    return Response("\n".join(xml) + "\n", mimetype="application/xml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        turnstile_response = request.form.get("cf-turnstile-response")
        if not turnstile_response:
            flash("Captcha no completado. Inténtalo de nuevo.", "danger")
            return redirect(url_for("contact"))
        verify_url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
        secret = os.getenv("TURNSTILE_SECRET_KEY")
        if not secret:
            flash("Captcha no configurado. Inténtalo de nuevo más tarde.", "danger")
            return redirect(url_for("contact"))
        data = {"secret": secret, "response": turnstile_response}
        try:
            response = requests.post(verify_url, data=data)
            response_data = response.json()
            if not response_data.get("success"):
                flash("Captcha no válido. Inténtalo de nuevo.", "danger")
                return redirect(url_for("contact"))
        except Exception as e:
            flash("Error al validar el captcha. Inténtalo de nuevo más tarde.", "danger")
            return redirect(url_for("contact"))
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if not name or not email or not message:
            flash("Por favor, completa todos los campos del formulario.", "danger")
            return redirect(url_for("contact"))
        msg = Message(
            subject="Nuevo mensaje desde el formulario de contacto",
            recipients=[os.getenv("RECIPIENT_EMAIL", "jbatistazerpa@gmail.com")],
            sender=app.config["MAIL_DEFAULT_SENDER"]
        )
        msg.html = f"""
            <h2 style="color: #2c3e50;">Nuevo mensaje desde el formulario de contacto</h2>
            <p><strong>Nombre:</strong> {name}</p>
            <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
            <p><strong>Mensaje:</strong></p>
            <p style="font-style: italic; color: #7f8c8d;">{message}</p>
        """
        try:
            mail.send(msg)
            flash("Mensaje enviado correctamente. Gracias por contactarme.", "success")
        except Exception as e:
            flash("Error enviando el mensaje. Inténtalo de nuevo más tarde.", "danger")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/projects/hotelsgc")
def PortfolioHotel():
    return render_template("HotelsGC.html")

@app.route("/projects/sportcollection")
def PortfolioSport():
    return render_template("sportcollection.html")

@app.route("/projects/garbelhr")
def PortfolioGarbel():
    return render_template("garbelhr.html")

@app.route('/projects/financialDashboard')
def FinancialDashboard():
    return render_template("financialdh.html")

app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", "587"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["TURNSTILE_SECRET_KEY"] = os.getenv("TURNSTILE_SECRET_KEY")

mail = Mail(app)

if __name__ == "__main__":
    app.run(debug=True)
