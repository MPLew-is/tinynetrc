import pytest
import tinynetrc
import os

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def netrc():
    return tinynetrc.Netrc(os.path.join(HERE, 'netrc_valid'))


def test_hosts(netrc):
    assert 'mail.google.com' in netrc.hosts
    assert isinstance(netrc.hosts['mail.google.com'], tuple)


def test_machines(netrc):
    assert 'mail.google.com' in netrc.machines
    assert isinstance(netrc.machines['mail.google.com'], dict)
    assert netrc.machines['mail.google.com']['login'] == 'joe@gmail.com'
    assert netrc.machines['mail.google.com']['account'] == 'justagmail'
    assert netrc.machines['mail.google.com']['password'] == 'somethingSecret'


def test_machine_formatting(netrc):
    assert 'login joe@gmail.com' in repr(netrc)


def test_machines_can_be_modified(netrc):
    netrc.machines['mail.google.com']['password'] = 'newpassword'
    assert 'newpassword' in repr(netrc)


def test_machines_can_be_added(netrc):
    netrc.machines['api.heroku.com']['login'] = 'joe@test.test'
    netrc.machines['api.heroku.com']['password'] = 'supersecret'
    assert 'api.heroku.com' in repr(netrc)
    assert 'supersecret' in repr(netrc)


def test_machines_can_be_removed(netrc):
    assert 'mail.google.com' in repr(netrc)
    del netrc.machines['mail.google.com']
    assert 'mail.google.com' not in repr(netrc)
