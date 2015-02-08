from flask import Flask, render_template, url_for


app = Flask(__name__)


from app.compute import api
from app.compute import routes


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/sitemap")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint)
            links.append((url, rule.endpoint))
    return "</br >".join([path for path, name in links])


__all__ = [
    'app',
]