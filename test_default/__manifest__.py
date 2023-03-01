# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  Leonardo Bozzi  (http://www.vangrow.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'test1',
    'version': '15.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Odoo Test',
    'author': 'Leonardo Bozzi',
    'depends': [
        # Applicaciones del Cliente
        'note',
        'board',


    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'env-ver': '2',
    'odoo-license': 'CE',
    # 'odoo-license': 'EE',
    'port': '8069',
    # 'server_user': ''

    'config': [
        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
            'workers = 4',
            'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
            'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
            'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
            'limit_memory_hard = 2684354560',
        # Prevents the worker from using more than CPU seconds for each request.
        # If the limit is exceeded, the worker is killed. Defaults to 60 sec.
            'limit_time_cpu = 1200',

        # Prevents the worker from taking longer than seconds to process a request.
        # If the limit is exceeded, the worker is killed. Defaults to 120. Differs
        # from --limit-time-cpu in that this is a "wall time" limit including e.g.
        # SQL queries.
            'limit_time_real = 2400',

        # default CSV separator for import and export
            'csv_internal_sep = ,',

        # disable loading demo data for modules to be installed
            'without_demo = False',

        # Comma-separated list of server-wide modules, there are modules loaded
        # automatically even if you do not create any database.
            'server_wide_modules = base,web,dbfilter_from_header',

        # Filter listed database REGEXP
            'dbfilter =',

            'db_maxconn = 64',
            'db_name = False',
            'db_password = odoo',
            'db_port = 5432',
            'db_sslmode = prefer',
            'db_template = template0',
            'db_user = odoo',
            'demo = {}',
            'email_from = False',
            'geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb',
            'http_enable = True',
            'http_interface =',
            'http_port = 8069',
            'longpolling_port = 8072',
            'limit_time_real_cron = -1',
            'list_db = True',
            'log_db = False',
            'log_db_level = warning',
            'log_handler = :INFO',
            'log_level = info',
            'logfile = /var/log/odoo/odoo.log',
            'osv_memory_age_limit = 1.0',
            'osv_memory_count_limit = False',
            'pg_path =',

            'proxy_mode = True',
            'reportgz = False',
            'screencasts =',
            'screenshots = /tmp/odoo_tests',
            'smtp_password = False',
            'smtp_port = 25',
            'smtp_server = localhost',
            'smtp_ssl = False',
            'smtp_user = False',
            'syslog = False',
            'test_enable = False',
            'test_file =',
            'test_tags = None',
            "translate_modules = ['all']",
            'unaccent = False',
            'upgrade_path =',
    ],

    'git-repos': [
        'https://github.com/leobozzi/cl-test.git',

    ],
    'docker-images': [
        'odoo lbozzi/odoo-docker-lb:15.0',
        'postgres postgres:12.10-alpine',
    ]
}
