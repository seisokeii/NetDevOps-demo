import os
import time
from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.functions import print_result
from script.JUNOS.lib_junos import junos_custom_all_config
from script.IOS.lib_ios import ios_custom_all_config
from script.NXOS.lib_nxos_task_list import nxos_custom_all_config
from dotenv import load_dotenv
load_dotenv()


def _execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} execute time: {execution_time} seconds")
        return result
    return wrapper


def load_vars(task):
    data = task.run(task=load_yaml, file=f'./hosts_vars/{task.host}.yaml')
    task.host["facts"] = data.result


@_execution_time
def custom_junos_all(nr):
    custom_all_target_junos = nr.filter(junos_pyez="yes")
    custom_all_result_junos = custom_all_target_junos.run(task=junos_custom_all_config, name="CONFIGURE JUNOS DEVICES")
    print_result(custom_all_result_junos, vars=['junos_save_config_request_result', 'result'])


@_execution_time
def custom_ios_all(nr):
    custom_all_target_ios = nr.filter(ios_scrapli="yes")
    custom_all_result_ios = custom_all_target_ios.run(task=ios_custom_all_config, name="CONFIGURE IOS DEVICES")
    print_result(custom_all_result_ios, vars=['ios_save_config_request_result'])


@_execution_time
def custom_nxos_all(nr):
    custom_all_target_nxos = nr.filter(nxos_restconf="yes")
    nxos_custom_all_config(custom_all_target_nxos)


def main():
    nr = InitNornir(config_file="./inventory/config.yaml")
    nr.inventory.defaults.username = os.getenv("BOT_ACCOUNT")
    nr.inventory.defaults.password = os.getenv("BOT_PASSWD")

    target_devices = nr.filter(product="yes")
    load_yaml_results = target_devices.run(task=load_vars)
    print_result(load_yaml_results)


    ### IOS ###
    # custom_ios_all(target_devices)

    ### JUNOS ###
    # custom_junos_all(target_devices)

    ### NXOS ###
    # custom_nxos_all(target_devices)



if __name__ == '__main__':
    main()
