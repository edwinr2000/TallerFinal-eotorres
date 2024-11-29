from flask import Flask, render_template
from api.Controllers.animals_controller import animals_bp

app = Flask(__name__)

# Registrar el Blueprint
app.register_blueprint(animals_bp)

@app.route('/')
def index():
    return render_template('index.html')


