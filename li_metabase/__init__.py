from flask import Flask, render_template

from li_metabase.config import SECRET_KEY
from li_metabase.views import (
    business_licenses, trade_licenses, permits,
    violations, misc
)
from li_metabase.utils import build_iframe_url


INDEX_PAGE_DASHBOARD_ID = 33

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    app.register_blueprint(business_licenses.bp)
    app.register_blueprint(trade_licenses.bp)
    app.register_blueprint(permits.bp)
    app.register_blueprint(violations.bp)
    app.register_blueprint(misc.bp)

    @app.route('/')
    def index():
        global INDEX_PAGE_DASHBOARD_ID

        payload = {
            'resource': {'dashboard': INDEX_PAGE_DASHBOARD_ID},
            'params': {}
        }

        iframe_url = build_iframe_url(payload)

        return render_template('dashboard.html', iframe_url=iframe_url)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html')

    return app