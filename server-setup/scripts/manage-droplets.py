#! /usr/bin/env python
"""
Script to start a new droplet, provision it and add a DNS entry.
"""
from __future__ import print_function
import argparse
import time
import yaml
import digitalocean
import logging

logger = logging.getLogger("digitalocean")

CONFIG_FILE = "digitalocean.yml"

DEFAULT_IMAGE = 'ubuntu-16-04-x64'
DEFAULT_REGION = 'BLR1'
DEFAULT_SIZE = '512mb'
DOMAIN_NAME = "pipal.in"
SSH_KEY = ""

USER_DATA = """\
#!/bin/bash
apt-get install -y python
"""

def read_config():
    return yaml.safe_load(open(CONFIG_FILE))

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=['list', 'create', 'destroy', 'test'], default="list", help="command to run")
    p.add_argument("nodes", nargs="*", help="nodes to create or destroy")
    return p.parse_args()

def get_ip(droplet):
    networks = droplet.networks['v4']
    networks = [n for n in networks if n['type'] == 'public']
    return networks[0]['ip_address']

class DigitalOcean:
    def __init__(self, config):
        self.droplet_token = config['droplets_api_token']
        self.dns_token = config['dns_api_token']

    def list(self):
        for name, d in self._list_droplets().items():
            print(name, get_ip(d))

    def _list_droplets(self):
        logger.info("listing droplets")
        manager = digitalocean.Manager(token=self.droplet_token)
        droplets = manager.get_all_droplets()
        return {d.name: d for d in droplets}

    def is_ready(self, droplet):
        actions = droplet.get_actions()
        for action in actions:
            action.load()
            if action.status == 'in-progress':
                return False
        return True

    def create(self, name):
        logger.info("creating a new droplet with name %s ...", name)
        manager = digitalocean.Manager(token=self.droplet_token)
        ssh_keys = manager.get_all_sshkeys()
        ssh_keys = [k.id for k in ssh_keys]

        droplet = digitalocean.Droplet(token=self.droplet_token,
                                       name=name,
                                       region=DEFAULT_REGION,
                                       image=DEFAULT_IMAGE,
                                       size_slug=DEFAULT_SIZE,
                                       user_data=USER_DATA,
                                       ssh_keys=ssh_keys,
                                       backups=False)
        droplet.create()

        while not self.is_ready(droplet):
            logger.info("droplet is not ready yet. waiting for some more time...")
            time.sleep(0.5)

        droplet = self._list_droplets()[name]

        ip = get_ip(droplet)
        logger.info("IP address: %s", ip)
        print(name, ip)
        logger.info("Adding DNS entry...")
        self.add_dns_entry(name, ip)
        logger.info("done")

    def add_dns_entry(self, name, ip):
        manager = digitalocean.Manager(token=self.dns_token)
        domain = manager.get_domain(DOMAIN_NAME)
        self._add_or_update_dns_entry(name=name, type="A", data=ip)
        self._add_or_update_dns_entry(name="*."+name, type="A", data=ip)

    def list_dns_entries(self):
        manager = digitalocean.Manager(token=self.dns_token)
        domain = manager.get_domain(DOMAIN_NAME)
        return {r.name:r for r in domain.get_records()}

    def _add_or_update_dns_entry(self, name, type, data):
        records = self.list_dns_entries()
        if name in records:
            logger.info("updating dns record: %s %s %s", name, type, data)
            rec = records[name]
            rec.type = type
            rec.data = data
            rec.save()
        else:
            logger.info("creating new dns record: %s %s %s", name, type, data)
            rec = digitalocean.Record(
                        token=self.dns_token,
                        domain_name=DOMAIN_NAME,
                        name=name, type=type, data=data)
            rec.create()

    def destroy(self, name):
        droplets = self._list_droplets()
        logger.info("destroying droplet %s ...", name)
        droplets[name].destroy()
        logger.info("done")

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    setup_logger()
    config = read_config()
    digitalocean = DigitalOcean(config)

    args = parse_args()
    if args.cmd == "list":
        digitalocean.list()
    elif args.cmd == "create":
        for name in args.nodes:
            digitalocean.create(name)
    elif args.cmd == "destroy":
        for name in args.nodes:
            digitalocean.destroy(name)
    elif args.cmd == "test":
        main_test(digitalocean)

def main_test(digitalocean):
    records = digitalocean.list_dns_entries()
    for name, rec in records.items():
        print(rec.id, rec.type, rec.name, rec.data)

if __name__ == '__main__':
    main()
