import requests
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from src.services.response_manager import ResponseManager

app = Flask("ops-kube-synthetic")
responseManager = ResponseManager()
metrics = PrometheusMetrics(
    app,
    defaults_prefix = 'synthetic_app',
    default_labels = {'endpoint': lambda: request.args.get('endpoint', '')
})

@app.after_request
def after_request_func(response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    if request.path.find("/metrics") != -1:
        response.headers["Content-Type"] = "text/plain; charset=utf-8"
        return response

    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route("/", methods=["GET"])
def home():
    return """Hello World."""

@app.route("/api/v1/healthz", methods=["GET"])
def check_healthz():
    return responseManager.success({"msg": "It works as expected."})
