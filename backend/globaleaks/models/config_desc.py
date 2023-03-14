# -*- coding: utf-8
from globaleaks import __version__, DATABASE_VERSION
from globaleaks.utils.crypto import GCE
from globaleaks.utils.utility import uuid4


class Item:
    _type = None

    def __init__(self, *args, **kwargs):
        self.default = kwargs['default']


class Unicode(Item):
    _type = str

    def __init__(self, *args, **kwargs):
        if 'default' not in kwargs:
            kwargs['default'] = ''

        Item.__init__(self, *args, **kwargs)


class Int(Item):
    _type = int


class Bool(Item):
    _type = bool


ConfigDescriptor = {
    'acme': Bool(default=False),
    'acme_accnt_key': Unicode(),
    'adminonly': Bool(default=False),
    'allow_indexing': Bool(default=True),
    'anonymize_outgoing_connections': Bool(default=False),
    'counter_submissions': Int(default=0),
    'custom_support_url': Unicode(default=''),
    'crypto_escrow_prv_key': Unicode(default=''),
    'crypto_escrow_pub_key': Unicode(default=''),
    'default_language': Unicode(default='en'),
    'default_questionnaire': Unicode(default='default'),
    'description': Unicode(default='Secure whistleblowing platform based on GlobaLeaks free and open-source software.'),
    'disable_admin_notification_emails': Bool(default=False),
    'disable_custodian_notification_emails': Bool(default=False),
    'disable_privacy_badge': Bool(default=False),
    'disable_receiver_notification_emails': Bool(default=False),
    'disable_submissions': Bool(default=False),
    'enable_admin_exception_notification': Bool(default=False),
    'enable_custodian': Bool(default=False),
    'enable_custom_privacy_badge': Bool(default=False),
    'enable_developers_exception_notification': Bool(default=False),
    'enable_scoring_system': Bool(default=False),
    'enable_signup': Bool(default=False),
    'encryption': Bool(default=True),
    'escrow': Bool(default=False),
    'hostname': Unicode(default=''),
    'https_admin': Bool(default=True),
    'https_cert': Unicode(),
    'https_chain': Unicode(),
    'https_csr': Unicode(),
    'https_custodian': Bool(default=True),
    'https_enabled': Bool(default=False),
    'https_key': Unicode(),
    'https_receiver': Bool(default=True),
    'https_whistleblower': Bool(default=True),
    'ip_filter_admin': Unicode(default=''),
    'ip_filter_admin_enable': Bool(default=False),
    'ip_filter_custodian': Unicode(default=''),
    'ip_filter_custodian_enable': Bool(default=False),
    'ip_filter_receiver': Unicode(default=''),
    'ip_filter_receiver_enable': Bool(default=False),
    'latest_version': Unicode(default=str(__version__)),
    'log_accesses_of_internal_users': Bool(default=True),
    'log_level': Unicode(default='ERROR'),
    'maximum_filesize': Int(default=30),
    'mode': Unicode(default='default'),
    'multisite': Bool(default=False),
    'name': Unicode(default='GLOBALEAKS'),
    'onionservice': Unicode(default=''),
    'password_change_period': Int(default=365),  # Days
    'reachable_via_web': Bool(default=True),
    'receipt_salt': Unicode(default=GCE.generate_salt),
    'rootdomain': Unicode(default=''),
    'show_contexts_in_alphabetical_order': Bool(default=True),
    'signup_tos1_enable': Bool(default=False),
    'signup_tos2_enable': Bool(default=False),
    'simplified_login': Bool(default=False),
    'smtp_authentication': Bool(default=True),
    'smtp_password': Unicode(default='globaleaks'),
    'smtp_port': Int(default=587),
    'smtp_security': Unicode(default='TLS'),
    'smtp_server': Unicode(default='mail.globaleaks.org'),
    'smtp_source_email': Unicode(default='notifications@globaleaks.org'),
    'smtp_username': Unicode(default='globaleaks'),
    'subdomain': Unicode(default=''),
    'threshold_free_disk_megabytes_high': Int(default=200),
    'threshold_free_disk_megabytes_low': Int(default=1000),
    'threshold_free_disk_percentage_high': Int(default=3),
    'threshold_free_disk_percentage_low': Int(default=10),
    'timezone': Int(default=0),
    'tip_expiration_threshold': Int(default=72),  # Hours
    'tor': Bool(default=True),
    'tor_onion_key': Unicode(),
    'two_factor': Bool(default=False),
    'unread_reminder_time': Int(default=7),  # Days
    'version': Unicode(default=str(__version__)),
    'version_db': Int(default=DATABASE_VERSION),
    'viewer': Bool(default=False),
    'wizard_done': Bool(default=False),
    'uuid': Unicode(default=uuid4)
}

ConfigFilters = {
    'node': [
        'acme',
        'adminonly',
        'allow_indexing',
        'anonymize_outgoing_connections',
        'counter_submissions',
        'custom_support_url',
        'crypto_escrow_pub_key',
        'default_language',
        'default_questionnaire',
        'description',
        'disable_privacy_badge',
        'disable_submissions',
        'enable_admin_exception_notification',
        'enable_custodian',
        'enable_custom_privacy_badge',
        'enable_developers_exception_notification',
        'enable_scoring_system',
        'enable_signup',
        'encryption',
        'escrow',
        'hostname',
        'https_admin',
        'https_custodian',
        'https_enabled',
        'https_receiver',
        'https_whistleblower',
        'ip_filter_admin',
        'ip_filter_admin_enable',
        'ip_filter_custodian',
        'ip_filter_custodian_enable',
        'ip_filter_receiver',
        'ip_filter_receiver_enable',
        'latest_version',
        'log_accesses_of_internal_users',
        'log_level',
        'maximum_filesize',
        'mode',
        'multisite',
        'name',
        'onionservice',
        'password_change_period',
        'reachable_via_web',
        'receipt_salt',
        'rootdomain',
        'show_contexts_in_alphabetical_order',
        'signup_tos1_enable',
        'signup_tos2_enable',
        'simplified_login',
        'subdomain',
        'threshold_free_disk_megabytes_high',
        'threshold_free_disk_megabytes_low',
        'threshold_free_disk_percentage_high',
        'threshold_free_disk_percentage_low',
        'timezone',
        'tor',
        'two_factor',
        'unread_reminder_time',
        'version',
        'version_db',
        'viewer',
        'wizard_done',
        'uuid'
    ],
    'admin_node': [
        'acme',
        'adminonly',
        'allow_indexing',
        'custom_support_url',
        'default_language',
        'default_questionnaire',
        'description',
        'disable_privacy_badge',
        'disable_submissions',
        'enable_admin_exception_notification',
        'enable_custodian',
        'enable_custom_privacy_badge',
        'enable_developers_exception_notification',
        'enable_scoring_system',
        'enable_signup',
        'encryption',
        'escrow',
        'hostname',
        'latest_version',
        'log_accesses_of_internal_users',
        'log_level',
        'maximum_filesize',
        'mode',
        'multisite',
        'name',
        'onionsite',
        'password_change_period',
        'receipt_salt',
        'rootdomain',
        'show_contexts_in_alphabetical_order',
        'signup_tos1_enable',
        'signup_tos2_enable',
        'simplified_login',
        'subdomain',
        'threshold_free_disk_megabytes_high',
        'threshold_free_disk_megabytes_low',
        'threshold_free_disk_percentage_high',
        'threshold_free_disk_percentage_low',
        'timezone',
        'tor',
        'two_factor',
        'version',
        'version_db',
        'viewer',
        'wizard_done',
        'uuid',
        'unread_reminder_time'
    ],
    'admin_network': [
        'anonymize_outgoing_connections',
        'hostname',
        'https_admin',
        'https_custodian',
        'https_receiver',
        'https_whistleblower',
        'reachable_via_web',
        'ip_filter_admin',
        'ip_filter_admin_enable',
        'ip_filter_custodian',
        'ip_filter_custodian_enable',
        'ip_filter_receiver',
        'ip_filter_receiver_enable',
        'onionservice'
    ],
    'general_settings': [
        'default_language',
        'description',
        'favicon',
        'footer',
        'header_title_homepage',
        'languages_enabled',
        'languages_supported',
        'logo',
        'name',
        'presentation',
        'whistleblowing_button',
        'whistleblowing_question',
    ],
    'notification': [
        'disable_admin_notification_emails',
        'disable_custodian_notification_emails',
        'disable_receiver_notification_emails',
        'smtp_authentication',
        'smtp_password',
        'smtp_port',
        'smtp_security',
        'smtp_server',
        'smtp_source_email',
        'smtp_username',
        'tip_expiration_threshold'
    ],
    'public_node': [
        'adminonly',
        'custom_support_url',
        'default_language',
        'default_questionnaire',
        'description',
        'disable_privacy_badge',
        'disable_submissions',
        'enable_custom_privacy_badge',
        'enable_scoring_system',
        'enable_signup',
        'hostname',
        'https_whistleblower',
        'maximum_filesize',
        'name',
        'mode',
        'onionservice',
        'rootdomain',
        'show_contexts_in_alphabetical_order',
        'signup_tos1_enable',
        'signup_tos2_enable',
        'simplified_login',
        'subdomain',
        'viewer',
        'wizard_done',
    ],
    'tenant': [
        'hostname',
        'mode',
        'name',
        'onionservice',
        'subdomain',
        'rootdomain'
    ]
}


ConfigL10NFilters = {
    'node': [
        'presentation',
        'footer',
        'disclaimer_text',
        'whistleblowing_question',
        'whistleblowing_button',
        'custom_privacy_badge_text',
        'header_title_homepage',
        'contexts_clarification',
        'signup_tos1_title',
        'signup_tos1_text',
        'signup_tos1_checkbox_label',
        'signup_tos2_title',
        'signup_tos2_text',
        'signup_tos2_checkbox_label'
    ],

    'notification': [
        'activation_mail_template',
        'activation_mail_title',
        'account_activation_mail_template',
        'account_activation_mail_title',
        'account_recovery_key_instructions',
        'admin_anomaly_activities',
        'admin_anomaly_disk_high',
        'admin_anomaly_disk_low',
        'admin_anomaly_mail_template',
        'admin_anomaly_mail_title',
        'admin_pgp_alert_mail_template',
        'admin_pgp_alert_mail_title',
        'admin_signup_alert_mail_template',
        'admin_signup_alert_mail_title',
        'admin_test_mail_template',
        'admin_test_mail_title',
        'email_validation_mail_template',
        'email_validation_mail_title',
        'export_message_recipient',
        'export_message_whistleblower',
        'export_template',
        'https_certificate_expiration_mail_template',
        'https_certificate_expiration_mail_title',
        'https_certificate_renewal_failure_mail_template',
        'https_certificate_renewal_failure_mail_title',
        'identity_access_authorized_mail_template',
        'identity_access_authorized_mail_title',
        'identity_access_denied_mail_template',
        'identity_access_denied_mail_title',
        'identity_access_request_mail_template',
        'identity_access_request_mail_title',
        'identity_provided_mail_template',
        'identity_provided_mail_title',
        'password_reset_validation_mail_template',
        'password_reset_validation_mail_title',
        'pgp_alert_mail_template',
        'pgp_alert_mail_title',
        'receiver_notification_limit_reached_mail_template',
        'receiver_notification_limit_reached_mail_title',
        'signup_mail_template',
        'signup_mail_title',
        'software_update_available_mail_template',
        'software_update_available_mail_title',
        'tip_access_mail_template',
        'tip_access_mail_title',
        'tip_expiration_summary_mail_template',
        'tip_expiration_summary_mail_title',
        'tip_mail_template',
        'tip_mail_title',
        'tip_update_mail_template',
        'tip_update_mail_title',
        'unread_tips_mail_template',
        'unread_tips_mail_title',
        'user_credentials'
    ]
}

ConfigL10NFilters['admin_node'] = ConfigL10NFilters['node']
ConfigL10NFilters['public_node'] = ConfigL10NFilters['node']
ConfigL10NFilters['general_settings'] = ConfigL10NFilters['node']
