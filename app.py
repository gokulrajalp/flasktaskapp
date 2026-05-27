from flask import Flask, render_template
from config.database import init_db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.payment_routes import payment_bp
from routes.map_routes import map_bp
from routes.ai_routes import ai_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecretkey"

init_db(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(task_bp, url_prefix="/api/tasks")


app.register_blueprint(
    payment_bp,
    url_prefix="/api/payment"
)

app.register_blueprint(
    map_bp,
    url_prefix="/map"
)

app.register_blueprint(
    ai_bp,
    url_prefix="/api/ai"
)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
