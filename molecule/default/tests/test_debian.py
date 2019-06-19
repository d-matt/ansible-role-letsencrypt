import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('debian')


@pytest.fixture(scope="module")
def AnsibleDefaults(host):
    return host.ansible("include_vars",
                        "../../defaults/main.yml")["ansible_facts"]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_certbot_file(host):
    f = host.file('/opt/letsencrypt/certbot-auto')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


def test_crontab(host):
    f = host.file('/var/spool/cron/crontabs/root')

    assert f.exists
    assert f.contains('30 2 * .*1.*/opt/letsencrypt/certbot-auto renew')


def test_cert_file(host, AnsibleDefaults):
    domain = AnsibleDefaults['letsencrypt_domain_name']
    f = host.file('/etc/letsencrypt/live/' + domain + '/fullchain.pem')
    assert f.exists
