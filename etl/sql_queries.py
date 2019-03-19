class SqlQuery():
    def __init__(self, extract_query_file, source_db, target_table):
        self.extract_query_file = 'queries/' + extract_query_file
        self.source_db = source_db
        self.target_table = target_table

# LI Dash Queries
IndividualWorkloads = SqlQuery(
    extract_query_file = 'individual_workloads.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'li_dash_indworkloads'
)

IncompleteProcessesBL = SqlQuery(
    extract_query_file = 'incomplete_processes_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'incompleteprocesses_bl'
)

IncompleteProcessesTL = SqlQuery(
    extract_query_file = 'incomplete_processes_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'incompleteprocesses_tl'
)

ActiveJobsBL = SqlQuery(
    extract_query_file = 'active_jobs_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'active_jobs_bl'
)

ActiveJobsTL = SqlQuery(
    extract_query_file = 'active_jobs_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'active_jobs_tl'
)

ActiveProcessesBL = SqlQuery(
    extract_query_file = 'active_processes_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'active_processes_bl'
)

ActiveProcessesTL = SqlQuery(
    extract_query_file = 'active_processes_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'active_processes_tl'
)

SubmissionModeBL = SqlQuery(
    extract_query_file = 'licenses/submission_mode_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'submission_mode_bl'
)

SubmissionModeTL = SqlQuery(
    extract_query_file = 'licenses/submission_mode_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'submission_mode_tl'
)

ExpiringLicensesBL = SqlQuery(
    extract_query_file = 'expiring_licenses_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'expiring_licenses_bl'
)

ExpiringLicensesTL = SqlQuery(
    extract_query_file = 'expiring_licenses_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'expiring_licenses_tl'
)

OverdueInspectionsBL = SqlQuery(
    extract_query_file = 'overdue_inspections_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'overdue_inspections_bl'
)

SLA_BL = SqlQuery(
    extract_query_file = 'sla_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'sla_bl'
)

SLA_BL_BUS_DAYS = SqlQuery(
    extract_query_file = 'sla_bl_bus_days.sql',
    source_db = 'GISLICLD',
    target_table = 'sla_bl_bus_days'
)

SLA_TL = SqlQuery(
    extract_query_file = 'sla_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'sla_tl'
)

SLA_TL_BUS_DAYS = SqlQuery(
    extract_query_file = 'sla_tl_bus_days.sql',
    source_db = 'GISLICLD',
    target_table = 'sla_tl_bus_days'
)

UninspectedBLsWithCompCheck = SqlQuery(
    extract_query_file = 'uninsp_bl_comp_check.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'uninsp_bl_comp_check'
)

# LI Stat Queries
LicensesIssuedBL = SqlQuery(
    extract_query_file = 'licenses/licenses_issued_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'licenses_issued_bl'
)

LicensesIssuedTL = SqlQuery(
    extract_query_file = 'licenses/licenses_issued_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'licenses_issued_tl'
)

LicenseRevenueBL = SqlQuery(
    extract_query_file = 'licenses/revenue_bl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'revenue_bl'
)

LicenseRevenueTL = SqlQuery(
    extract_query_file = 'licenses/revenue_tl.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'revenue_tl'
)

LicenseTrendsBL = SqlQuery(
    extract_query_file = 'licenses/slide3_license_trends_BL.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'li_stat_licensetrends_bl'
)

SubmittalVolumesBL = SqlQuery(
    extract_query_file = 'licenses/slide4_submittal_volumes_BL.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'li_stat_submittalvolumes_bl'
)

SubmittalVolumesTL = SqlQuery(
    extract_query_file = 'licenses/slide4_submittal_volumes_TL.sql',
    source_db = 'ECLIPSE_PROD',
    target_table = 'li_stat_submittalvolumes_tl'
)

PermitsFees = SqlQuery(
    extract_query_file = 'permits/permits_and_fees.sql',
    source_db='LIDB',
    target_table = 'permits_fees'
)

PermitsOTCvsReview = SqlQuery(
    extract_query_file = 'permits/Slide3_all_count_monthly_permits.sql',
    source_db = 'LIDB',
    target_table = 'li_stat_permits_otcvsreview'
)

PermitsAccelReview = SqlQuery(
    extract_query_file = 'permits/Slide5_accelerated_reviews.sql',
    source_db = 'LIDB',
    target_table = 'li_stat_permits_accelreview'
)

ImmDang = SqlQuery(
    extract_query_file = 'imm_dang.sql',
    source_db = 'GISLNI',
    target_table = 'imm_dang'
)

Unsafes = SqlQuery(
    extract_query_file = 'unsafes.sql',
    source_db = 'GISLNI',
    target_table = 'unsafes'
)

PublicDemos = SqlQuery(
    extract_query_file = 'public_demos.sql',
    source_db = 'DataBridge',
    target_table = 'public_demos'
)

UninspectedServiceRequests = SqlQuery(
    extract_query_file = 'UninspectedServiceRequests.sql',
    source_db = 'GISLNI',
    target_table = 'li_stat_uninspectedservreq'
)

UninspectedServiceRequestsBusDays = SqlQuery(
    extract_query_file = 'UninspectedServiceRequestsBusDays.sql',
    source_db = 'GISLICLD',
    target_table = 'uninspectedservreq_busdays'
)

queries = [
    # LI Dash Queries
    IndividualWorkloads,
    IncompleteProcessesBL,
    IncompleteProcessesTL,
    UninspectedBLsWithCompCheck,
    ActiveJobsBL,
    ActiveJobsTL, 
    ActiveProcessesBL,
    ActiveProcessesTL,
    SubmissionModeBL,
    SubmissionModeTL,
    ExpiringLicensesBL,
    ExpiringLicensesTL,
    OverdueInspectionsBL,
    SLA_BL,
    SLA_BL_BUS_DAYS,
    SLA_TL,
    SLA_TL_BUS_DAYS,
    # LI Stat Queries
    PermitsFees,
    PermitsOTCvsReview,
    PermitsAccelReview,
    ImmDang,
    Unsafes,
    PublicDemos,
    UninspectedServiceRequests,
    UninspectedServiceRequestsBusDays,
    LicensesIssuedBL,
    LicensesIssuedTL,
    LicenseRevenueBL,
    LicenseRevenueTL,
    LicenseTrendsBL,
    SubmittalVolumesBL,
    SubmittalVolumesTL,
]
