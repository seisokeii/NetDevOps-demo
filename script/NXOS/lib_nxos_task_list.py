from nornir_utils.plugins.functions import print_result
from script.NXOS.lib_nxos import *


def nxos_custom_all_config(target_devices):
    base(target_devices)
    interface(target_devices)
    vlan(target_devices)
    acl(target_devices)
    vrf(target_devices)
    vpc(target_devices)
    dhcp(target_devices)
    route_map(target_devices)
    ospf(target_devices)
    stp(target_devices)
    vrrp(target_devices)
    SaveConfig(target_devices)


def SaveConfig(nr):
    save_config_result = nr.run(task=nxos_save_config, name="NXOS SAVE CONFIGURATION")
    print_result(save_config_result, vars=['nxos_save_config_request_result'])


def base(nr):
    base_target_nxos = nr.filter(nxos_base="yes")
    base_result_nxos = base_target_nxos.run(task=nxos_base_config, name="NXOS BASE CONFIGURE")
    print_result(base_result_nxos, vars=['nxos_base_request_result'])
    # print_result(base_result_nxos, vars=['nxos_base_request_result', 'result']) # Contain jinja2 result


def interface(nr):
    interface_target_nxos = nr.filter(nxos_interface="yes")
    interface_result_nxos = interface_target_nxos.run(task=nxos_interface_config, name="NXOS INTERFACE CONFIGURE")
    print_result(interface_result_nxos, vars=['nxos_interface_request_result'])
    # print_result(interface_result_nxos, vars=['nxos_interface_request_result', 'result']) # Contain jinja2 result


def vlan(nr):
    vlan_target_nxos = nr.filter(nxos_vlan="yes")
    vlan_result_nxos = vlan_target_nxos.run(task=nxos_vlan_config, name="NXOS VLAN CONFIGURE")
    print_result(vlan_result_nxos, vars=['nxos_vlan_request_result'])
    # print_result(vlan_result_nxos, vars=['nxos_vlan_request_result', 'result']) # Contain jinja2 result


def acl(nr):
    acl_target_nxos = nr.filter(nxos_acl="yes")
    acl_result_nxos = acl_target_nxos.run(task=nxos_acl_config, name="NXOS ACL CONFIGURE")
    print_result(acl_result_nxos, vars=['nxos_acl_request_result'])
    # print_result(acl_result_nxos, vars=['nxos_acl_request_result', 'result']) # Contain jinja2 result


def vrf(nr):
    vrf_target_nxos = nr.filter(nxos_vrf="yes")
    vrf_result_nxos = vrf_target_nxos.run(task=nxos_vrf_config, name="NXOS VRF CONFIGURE")
    print_result(vrf_result_nxos, vars=['nxos_vrf_request_result'])
    # print_result(vrf_result_nxos, vars=['nxos_vrf_request_result', 'result']) # Contain jinja2 result


def vpc(nr):
    vpc_target_nxos = nr.filter(nxos_vpc="yes")
    vpc_result_nxos = vpc_target_nxos.run(task=nxos_vpc_config, name="NXOS VPC CONFIGURE")
    print_result(vpc_result_nxos, vars=['nxos_vpc_request_result'])
    # print_result(vpc_result_nxos, vars=['nxos_vpc_request_result', 'result']) # Contain jinja2 result


def dhcp(nr):
    dhcp_target_nxos = nr.filter(nxos_dhcp="yes")
    dhcp_result_nxos = dhcp_target_nxos.run(task=nxos_dhcp_config, name="NXOS DHCP CONFIGURE")
    print_result(dhcp_result_nxos, vars=['nxos_dhcp_request_result'])
    # print_result(dhcp_result_nxos, vars=['nxos_dhcp_request_result', 'result']) # Contain jinja2 result


def route_map(nr):
    route_map_target_nxos = nr.filter(nxos_route_map="yes")
    route_map_result_nxos = route_map_target_nxos.run(task=nxos_route_map_config, name="NXOS ROUTE MAP CONFIGURE")
    print_result(route_map_result_nxos, vars=['nxos_route_map_request_result'])
    # print_result(route_map_result_nxos, vars=['nxos_route_map_request_result', 'result']) # Contain jinja2 result


def ospf(nr):
    ospf_target_nxos = nr.filter(nxos_ospf="yes")
    ospf_result_nxos = ospf_target_nxos.run(task=nxos_ospf_config, name="NXOS OSPF CONFIGURE")
    print_result(ospf_result_nxos, vars=['nxos_ospf_request_result'])
    # print_result(ospf_result_nxos, vars=['nxos_ospf_request_result', 'result']) # Contain jinja2 result


def stp(nr):
    stp_target_nxos = nr.filter(nxos_stp="yes")
    stp_result_nxos = stp_target_nxos.run(task=nxos_stp_config, name="NXOS STP CONFIGURE")
    print_result(stp_result_nxos, vars=['nxos_stp_request_result'])
    # print_result(stp_result_nxos, vars=['nxos_stp_request_result', 'result']) # Contain jinja2 result


def vrrp(nr):
    vrrp_target_nxos = nr.filter(nxos_vrrp="yes")
    vrrp_result_nxos = vrrp_target_nxos.run(task=nxos_vrrp_config, name="NXOS VRRP CONFIGURE")
    print_result(vrrp_result_nxos, vars=['nxos_vrrp_request_result'])
    # print_result(vrrp_result_nxos, vars=['nxos_vrrp_request_result', 'result']) # Contain jinja2 result

