import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_TITLE = os.environ.get("APP_TITLE", "Каталог облачных сервисов")

SERVICES = {
    "IaaS": ["Amazon EC2", "Google Compute Engine", "Azure Virtual Machines"],
    "PaaS": ["Google App Engine", "Azure App Service", "AWS Elastic Beanstalk"],
    "SaaS": ["Google Workspace", "Microsoft 365", "Zoom"],
}


@app.route("/")
def index():
    return f"{APP_TITLE}: приложение работает!\n"


@app.route("/services")
def services():
    return jsonify(SERVICES)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
