bind = "0.0.0.0:5000"
loglevel = "info"
accesslog = "-"
errorlog = '-'
access_log_format = '{"remote_address": "%(h)s","client_ip": "%(l)s","user_name": "%(u)s","request_date": "%(t)s","status_line": "%(r)s","url": "%(U)s","query_string": "%(q)s","status": "%(s)s","response_length": "%(b)s","referer": "%(f)s","user_agent": "%(a)s","request_time": "%(T)s"}'
workers = 1 # keep this as 1 - https://github.com/rycus86/prometheus_flask_exporter#multiprocess-applications
graceful_timeout = 30
