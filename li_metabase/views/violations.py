from flask import Blueprint, render_template

from li_metabase.utils import Dashboard, build_iframe_url_from_dashboard_url, DashboardNotFound
from li_metabase.auth import auth


VIOLATIONS_DASHBOARDS = [
    Dashboard('Unsafe Violations', 'unsafe', 42),
    Dashboard('Imminently Dangerous Violations', 'imminently-dangerous-violations', 36),
    Dashboard('Current Imminently Dangerous Properties', 'current-imminently-dangerous-properties', 85)
]

bp = Blueprint('violations', __name__)

@bp.route('/violations/<dashboard_url>')
@auth.login_required
def violations(dashboard_url):
    global VIOLATIONS_DASHBOARDS

    iframe_url = build_iframe_url_from_dashboard_url(dashboard_url, VIOLATIONS_DASHBOARDS)

    return render_template('dashboard.html', iframe_url=iframe_url)

@bp.errorhandler(DashboardNotFound)
def handle_error(error):
    return render_template('error.html')
