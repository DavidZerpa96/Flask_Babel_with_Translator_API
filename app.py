import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from flask_mail import Mail, Message
from flask_babel import Babel, _
import requests
from flask_cors import CORS
from dash import Dash, dcc, html, Input, Output, State, no_update, dash_table
import plotly.express as px
import plotly.io as pio
import base64
import io
import pandas as pd
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")
CORS(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'es'
app.config['BABEL_SUPPORTED_LOCALES'] = ['es', 'en']
babel = Babel(app)

def get_locale():
    selected_locale = request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])
    if not selected_locale:
        selected_locale = 'en'
    if selected_locale not in app.config['BABEL_SUPPORTED_LOCALES']:
        selected_locale = 'en'
    lang_override = request.args.get('lang')
    if lang_override in app.config['BABEL_SUPPORTED_LOCALES']:
        selected_locale = lang_override
    return selected_locale

@app.before_request
def ensure_lang_in_url():
    # Si la ruta pertenece a la app Dash, no forzar lang.
    if request.path.startswith('/resources/dashboard/dash/'):
        return
    # No forzar `lang` en recursos estáticos (evita redirects por cada CSS/JS/imagen).
    if request.path.startswith('/static/'):
        return
    if 'lang' not in request.args:
        lang = request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES']) or app.config['BABEL_DEFAULT_LOCALE']
        return redirect(f"{request.path}?lang={lang}")


babel.init_app(app, locale_selector=get_locale)

@app.context_processor
def inject_template_globals():
    # Avoid hardcoding copyright year across templates.
    return {"current_year": datetime.utcnow().year}

@app.route("/")
def home():
    return render_template("index.html")

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
            flash(_("Captcha no completado. Inténtalo de nuevo."), "danger")
            return redirect(url_for("contact"))
        verify_url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
        data = {"secret": os.getenv("TURNSTILE_SECRET_KEY"), "response": turnstile_response}
        try:
            response = requests.post(verify_url, data=data)
            response_data = response.json()
            if not response_data.get("success"):
                flash(_("Captcha no válido. Inténtalo de nuevo."), "danger")
                return redirect(url_for("contact"))
        except Exception as e:
            flash(_("Error al validar el captcha. Inténtalo de nuevo más tarde."), "danger")
            return redirect(url_for("contact"))
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if not name or not email or not message:
            flash(_("Por favor, complete todos los campos del formulario."), "danger")
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
            flash(_("Message sent successfully. Thank you for contacting me!"), "success")
        except Exception as e:
            flash(_("Error sending the message. Please try again later."), "danger")
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

app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["TURNSTILE_SECRET_KEY"] = os.getenv("TURNSTILE_SECRET_KEY")

mail = Mail(app)

@app.route("/resources")
def resources():
    """
    Página principal con la lista de recursos
    (ejemplo en 'resources.html').
    """
    return render_template("resources.html")

@app.route("/resources/dashboard")
def resources_dashboard():
    """
    Página específica del recurso 'Dashboard Creator'.
    Incrusta la app Dash en un iframe.
    (ejemplo en 'dash_creator.html')
    """
    return render_template("dash_creator.html")

############################################
# APP DASH: /resources/dashboard/dash/
############################################

dash_app = Dash(
    __name__,
    server=app,  # tu instancia Flask
    url_base_pathname="/resources/dashboard/dash/"
)
dash_app.title = "Dashboard Creator"

dash_app.layout = html.Div([
    html.H2("Dashboard Creator", style={"textAlign": "center", "marginTop": "20px"}),
    html.P(
        "Upload one or multiple CSV/Excel files. Then select one file to plot, choose chart type, X/Y columns, perform calculations, and export to PNG.",
        style={"textAlign": "center", "color": "gray"}
    ),
    dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag & Drop or Click to Select Files"]),
        style={
            'width': '80%',
            'height': '80px',
            'lineHeight': '80px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '20px auto',
            'cursor': 'pointer'
        },
        multiple=True
    ),
    dcc.Store(id="stored-data"),
    html.Div(id="file-gallery", style={
        "display": "flex",
        "flexWrap": "wrap",
        "margin": "20px",
        "justifyContent": "center"
    }),
    html.Div([
        html.Label("Select file to plot:"),
        dcc.Dropdown(id="dropdown-file", placeholder="Choose a file")
    ], style={"width": "50%", "margin": "auto"}),

    # Dropdown para elegir el tipo de gráfico
    html.Div([
        html.Label("Select chart type:"),
        dcc.Dropdown(
            id="dropdown-chart-type",
            options=[
                {"label": "Line Chart", "value": "line"},
                {"label": "Bar Chart", "value": "bar"},
                {"label": "Scatter Plot", "value": "scatter"},
                {"label": "Pie Chart", "value": "pie"},
                {"label": "Treemap", "value": "treemap"}
            ],
            value="line",
            clearable=False
        )
    ], style={"width": "45%", "margin": "auto", "padding": "10px"}),

    # Dropdowns para eje X e Y
    html.Div([
        html.Label("Select X-axis:"),
        dcc.Dropdown(id="dropdown-x", placeholder="Select x-axis column")
    ], style={"width": "45%", "display": "inline-block", "padding": "10px"}),
    html.Div([
        html.Label("Select Y-axis:"),
        dcc.Dropdown(id="dropdown-y", placeholder="Select y-axis column(s)", multi=True)
    ], style={"width": "45%", "display": "inline-block", "padding": "10px"}),

    # NUEVO: Sección de cálculos
    html.Div([
        html.Label("Select calculation function:"),
        dcc.Dropdown(
            id="calc-function",
            options=[
                {"label": "None", "value": "None"},
                {"label": "Count", "value": "Count"},
                {"label": "Sum", "value": "Sum"},
                {"label": "Average", "value": "Average"},
                {"label": "Min", "value": "Min"},
                {"label": "Max", "value": "Max"}
            ],
            value="None",
            clearable=False
        )
    ], style={"width": "45%", "display": "inline-block", "padding": "10px"}),
    html.Div([
        html.Label("Select column for calculation:"),
        dcc.Dropdown(id="calc-column", placeholder="Choose a column")
    ], style={"width": "45%", "display": "inline-block", "padding": "10px"}),
    html.Div(id="calc-result", style={"textAlign": "center", "fontWeight": "bold", "margin": "10px"}),

    dcc.Graph(id="graph"),
    html.Button("Export to PNG", id="export-btn", style={"display": "block", "margin": "20px auto"}),
    dcc.Download(id="download-image")
])


###############################################################################
# 1) PROCESAR LOS ARCHIVOS Y GUARDARLOS
###############################################################################
@dash_app.callback(
    Output("stored-data", "data"),
    Output("file-gallery", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("stored-data", "data")
)
def store_files(list_of_contents, list_of_filenames, current_store):
    if list_of_contents is None:
        if current_store:
            return current_store, gallery_children_from_store(current_store)
        return {}, []
    if not current_store:
        current_store = {}
    if isinstance(current_store, str):
        current_store = eval(current_store)
    for contents, fname in zip(list_of_contents, list_of_filenames):
        try:
            df = parse_file(contents, fname)
            current_store[fname] = df.to_json(date_format='iso', orient='split')
        except Exception as e:
            pass
    gallery = gallery_children_from_store(current_store)
    return current_store, gallery

def parse_file(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    if filename.lower().endswith('.csv'):
        return pd.read_csv(io.StringIO(decoded.decode("utf-8")), engine='python')
    elif filename.lower().endswith(('.xls', '.xlsx')):
        return pd.read_excel(io.BytesIO(decoded))
    else:
        raise ValueError("Unsupported file format. Must be CSV or Excel.")

def gallery_children_from_store(store_dict):
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    children = []
    for fname in store_dict.keys():
        children.append(
            html.Div(fname, style={
                "border": "1px solid #ccc",
                "padding": "8px 12px",
                "margin": "5px",
                "borderRadius": "5px"
            })
        )
    return children

###############################################################################
# 2) ACTUALIZAR EL DROPDOWN DE ARCHIVOS
###############################################################################
@dash_app.callback(
    Output("dropdown-file", "options"),
    Input("stored-data", "data")
)
def update_file_dropdown(store_dict):
    if not store_dict:
        return []
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    return [{"label": f, "value": f} for f in store_dict.keys()]

@dash_app.callback(
    Output("calc-column", "options"),
    Input("dropdown-file", "value"),
    State("stored-data", "data")
)
def update_calc_column(selected_file, store_dict):
    if not selected_file or not store_dict:
        return []
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    df_json = store_dict.get(selected_file)
    if not df_json:
        return []
    df = pd.read_json(df_json, orient='split')
    return [{"label": col, "value": col} for col in df.columns]

@dash_app.callback(
    Output("calc-result", "children"),
    [Input("dropdown-file", "value"),
     Input("calc-function", "value"),
     Input("calc-column", "value")],
    State("stored-data", "data")
)
def update_calculation(selected_file, calc_func, calc_col, store_dict):
    if not selected_file or not calc_func or calc_func == "None" or not calc_col:
        return ""
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    df_json = store_dict.get(selected_file)
    if not df_json:
        return ""
    df = pd.read_json(df_json, orient="split")
    try:
        if calc_func == "Count":
            result = df[calc_col].count()
        elif calc_func == "Sum":
            result = df[calc_col].sum()
        elif calc_func == "Average":
            result = df[calc_col].mean()
        elif calc_func == "Min":
            result = df[calc_col].min()
        elif calc_func == "Max":
            result = df[calc_col].max()
        else:
            result = ""
        return f"{calc_func} of {calc_col}: {result}"
    except Exception as e:
        return f"Calculation error: {e}"

###############################################################################
# 3) AL ELEGIR UN ARCHIVO, ACTUALIZAR DROPDOWNS DE COLUMNAS
###############################################################################
@dash_app.callback(
    [Output("dropdown-x", "options"),
     Output("dropdown-y", "options"),
     Output("dropdown-x", "value"),
     Output("dropdown-y", "value")],
    Input("dropdown-file", "value"),
    State("stored-data", "data")
)
def update_xy_dropdowns(selected_file, store_dict):
    if not selected_file or not store_dict:
        return [], [], None, []
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    df_json = store_dict.get(selected_file)
    if not df_json:
        return [], [], None, []
    df = pd.read_json(df_json, orient='split')
    col_options = [{"label": col, "value": col} for col in df.columns]
    return col_options, col_options, None, []

###############################################################################
# 4) GENERAR LA GRÁFICA SEGÚN EL TIPO SELECCIONADO
###############################################################################
@dash_app.callback(
    Output("graph", "figure"),
    [
        Input("dropdown-file", "value"),
        Input("dropdown-x", "value"),
        Input("dropdown-y", "value"),
        Input("dropdown-chart-type", "value"),
    ],
    State("stored-data", "data")
)
def update_graph(selected_file, x_col, y_cols, chart_type, store_dict):
    if not selected_file or not x_col or not y_cols or not chart_type:
        return {}
    if isinstance(store_dict, str):
        store_dict = eval(store_dict)
    df_json = store_dict.get(selected_file)
    if not df_json:
        return {}
    df = pd.read_json(df_json, orient='split')
    try:
        if chart_type == "line":
            fig = px.line(df, x=x_col, y=y_cols, title=f"Line Chart for {selected_file}")
        elif chart_type == "bar":
            fig = px.bar(df, x=x_col, y=y_cols, title=f"Bar Chart for {selected_file}")
        elif chart_type == "scatter":
            fig = px.scatter(df, x=x_col, y=y_cols, title=f"Scatter Plot for {selected_file}")
        elif chart_type == "pie":
            if isinstance(y_cols, list) and y_cols:
                fig = px.pie(df, names=x_col, values=y_cols[0], title=f"Pie Chart for {selected_file}")
            else:
                fig = {}
        elif chart_type == "treemap":
            if isinstance(y_cols, list) and y_cols:
                fig = px.treemap(df, path=[x_col], values=y_cols[0], title=f"Treemap for {selected_file}")
            else:
                fig = {}
        else:
            fig = {}
        fig.update_layout(template="seaborn")
        return fig
    except Exception as e:
        print("Error generating figure:", e)
        return {}

###############################################################################
# 5) EXPORTAR A PNG
###############################################################################
@dash_app.callback(
    Output("download-image", "data"),
    Input("export-btn", "n_clicks"),
    State("graph", "figure"),
    prevent_initial_call=True
)
def export_png(n_clicks, figure):
    if not figure:
        return no_update
    try:
        img_bytes = pio.to_image(figure, format="png")
        return dcc.send_bytes(lambda: img_bytes, "visual.png")
    except Exception as e:
        print("Error exporting PNG:", e)
        return no_update

if __name__ == "__main__":
    app.run(debug=True)
