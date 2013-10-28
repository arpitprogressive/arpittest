"""
    fabfile

    Fabric script to deploy django-pursuite

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import os
import getpass

import requests
from fabric.api import sudo, cd, prefix, run, env
from fabric.decorators import hosts

# Forward the SSH agent so that git pull works
env.forward_agent = True
env.use_ssh_config = True

hipchat_notification_token = open(
    os.path.expanduser('~/.hipchat-token')
).read().replace('\n', '')


def notify_hipchat(
        message, from_='deployer', color='gray', room_id='292065',
        message_format="text", notify=False):
    """
    Send the given message to hipchat room
    """
    rv = requests.post(
        "https://api.hipchat.com/v1/rooms/message?format=json"
        "&auth_token=%s" % (hipchat_notification_token),
        data={
            'room_id': room_id,
            'from': from_,
            'message': message,
            'message_format': message_format,
            'notify': notify and 1 or 0,
            'color': color,
        }
    )
    return rv


@hosts('%s@pursuite.openlabs.us' % getpass.getuser())
def deploy_staging(schema_update=False, migrate=False):
    "Deploy to staging"
    notify_hipchat("Beginning deployment", from_="Staging")
    root_path = '/opt/pursuite'
    sudo('chmod -R g+rw %s' % root_path)

    with cd(root_path):
        with prefix("source %s/bin/activate" % root_path):
            with cd('django-pursuite'):
                run('git fetch')
                run('git checkout origin/develop')
                run('python setup.py install')

                manage = 'python manage.py '
                settings = '--settings="pursuite.settings.staging" '
                run(manage + ' collectstatic --noinput ' + settings)

                if schema_update:
                    notify_hipchat("Running syncdb", from_="Staging")
                    run(manage + ' syncdb --all ' + settings)

                if migrate:
                    notify_hipchat("Running migrate", from_="Staging")
                    run(manage + ' migrate ' + settings)
            # Rebuild index for search
            run(manage + ' rebuild_index ' + settings)

            notify_hipchat("Restarting services", from_="Staging")
            sudo('bin/supervisorctl restart all')

    update_documentation()


def update_documentation():
    """
    Update the documentation on the current host.

    This method is host agnostic
    """
    root_path = '/opt/pursuite'

    with cd(root_path):
        with prefix("source %s/bin/activate" % root_path):
            with cd('django-pursuite/pursuite/doc'):
                run('make html')
