import yaml
from gns3fy import Gns3Connector, Project
import os
from dotenv import load_dotenv

load_dotenv()


def get_project_id(gns3_server, project_name):
    lab = Project(name=project_name, connector=gns3_server)
    lab.get()
    return lab.project_id


def create_project(gns3_server, project_name):
    lab = Project(name=project_name, connector=gns3_server)
    lab.create()
    return lab.project_id


def add_nodes(gns3_server, project_id, node_list):
    lab = Project(project_id=project_id, connector=gns3_server)

    for node in node_list:
        try:
            lab.create_node(name=node[0], template=node[1])
            # print("Add node: " + node[0] + ", template: " + node[1])
        except Exception as e:
            print(e)
            pass


def add_link(gns3_server, project_id, link_list):
    lab = Project(project_id=project_id, connector=gns3_server)

    for link in link_list:
        try:
            lab.create_link(link[0], link[1], link[2], link[3])
            # print("Add Link of node: " + link[0] + " " + link[1] + " --> node: " + link[2] + " " + link[3])
        except Exception as e:
            print(e)
            pass


def main():
    gns3_server = Gns3Connector("{URL}}",
                                user=os.environ.get("GNS3_ACCOUNT"),
                                cred=os.environ.get("GNS3_PASSWD"))

    with open('./gns3_topology/devices.yaml', 'r') as f:
        file_data = yaml.safe_load(f)
    f.close()

    nxos_temp = "Cisco NX-OSv 9000 9300v 9.3.9"
    junos_temp = "vJunos-switch 23.2R1.14"
    ios_temp = "Cisco IOSvL2 15.2(20200924:215240)"

    node_list = []
    link_list = []

    for device_type, devices in file_data.items():
        for device, links in devices.items():
            if device_type == "Nexus":
                node_list.append((device, nxos_temp))
            elif device_type == "Junos":
                node_list.append((device, junos_temp))
            elif device_type == "IOS":
                node_list.append((device, ios_temp))

            for link in links:
                # link = [ src_port, dst_device, dst_port ]
                link_list.append((device, link[0], link[1], link[2]))


    project_name = "NetDevOps-sim-product"
    project_ID = get_project_id(gns3_server, project_name)
    add_nodes(gns3_server, project_ID, node_list)
    add_link(gns3_server, project_ID, link_list)


if __name__ == '__main__':
    main()
