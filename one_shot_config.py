import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from dotenv import load_dotenv
load_dotenv()


def save2file(task):
    junos = task.filter(junos_pyez="yes")
    nxos = task.filter(nxos_restconf="yes")
    junos_result = junos.run(task=netmiko_send_command, command_string="show config")
    nxos_result = nxos.run(task=netmiko_send_command, command_string="show running-config")
    junos.run(task=write_file, content=junos_result.result, filename=str(task.host.name))
    nxos.run(task=write_file, content=nxos_result.result, filename=str(task.host.name))


def main():
    nr = InitNornir(config_file="./inventory/config.yaml")
    nr.inventory.defaults.username = os.getenv("BOT_ACCOUNT")
    nr.inventory.defaults.password = os.getenv("BOT_PASSWD")

    # files = nr.run(task=save2file)
    # print_result(files)


if __name__ == '__main__':
    main()


