from flask import Flask, render_template
from config.database import init_db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecretkey"

init_db(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(task_bp, url_prefix="/api/tasks")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
