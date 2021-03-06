from flask import Blueprint, render_template

from li_metabase.utils import Dashboard, build_iframe_url_from_dashboard_url, DashboardNotFound
from li_metabase.auth import auth


TL_INVESTIGATION_DASHBOARDS = [
    Dashboard('Permits and Inspections', 'permits-and-inspections', 167),
    Dashboard('TL Investigation - Cases', 'cases', 173)
]

bp = Blueprint('tl_investigation', __name__)

@bp.route('/tl/investigations/<dashboard_url>')
@auth.login_required
def cases_violations(dashboard_url):
    global TL_INVESTIGATION_DASHBOARDS

    iframe_url = build_iframe_url_from_dashboard_url(dashboard_url, TL_INVESTIGATION_DASHBOARDS)

    return render_template('dashboard.html', iframe_url=iframe_url)

@bp.errorhandler(DashboardNotFound)
def handle_error(error):
    return render_template('error.html')
