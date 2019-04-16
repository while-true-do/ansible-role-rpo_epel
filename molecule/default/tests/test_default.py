import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_file(host):
    file = host.file('/etc/yum.repos.d/epel.repo')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_epel_testing_file(host):
    file = host.file('/etc/yum.repos.d/epel-testing.repo')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
