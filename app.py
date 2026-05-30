from flask import Flask, render_template
from config.database import init_db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.payment_routes import payment_bp
from routes.map_routes import map_bp
from routes.ai_routes import ai_bp
from routes.oauth_routes import (
    oauth_bp,
    init_oauth
)
from config.oauth_config import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger":"2.0",
    "securityDefinitions":{
        "Bearer":{
            "type":"apikey",
            "name":"Authorization",
            "in":"header"
        }
    }
}

swagger = Swagger(app,template=swagger_template)
app.config["SWAGGER"]={
    "title":"Task Management",
    "uiversion":3
}
app.secret_key = "oauth-secret-key"

app.config["SECRET_KEY"] = "supersecretkey"
app.config["GOOGLE_CLIENT_ID"] = (
    GOOGLE_CLIENT_ID
)
app.config["GOOGLE_CLIENT_SECRET"] = (
    GOOGLE_CLIENT_SECRET
)

init_db(app)
init_oauth(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(
    oauth_bp,
    url_prefix="/auth"
)
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
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )