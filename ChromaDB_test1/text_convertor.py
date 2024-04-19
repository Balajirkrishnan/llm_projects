import json

def json_to_text(node_data):
    text = ""
    for node_name, details in node_data.items():
        text += f"The node {node_name} runs on OS version {details['os_version']}. "
        text += f"Node exporter status is installed: {details['node_exporter_status']['installed']}, "
        text += f"status: {details['node_exporter_status']['status']}. "
        text += f"qualys service status is {details['qualys_service_status']}, "
        text += f"consul service status is {details['consul_service_status']}, and "
        text += f"NTP status is {details['ntp_status']}. "
        text += f"It's a {details['system_type']} with uptime of {details['uptime']} minutes and "
        text += f"log size of {details['logsize']}. "
        text += f"Application version includes {' and '.join(details['app_version'])}. "
        text += f"athena status is installed: {details['athena_status']['installed']}, "
        text += f"status: {details['athena_status']['status']}, "
        text += f"version: {details['athena_status']['version']}. "
        text += f"Waiting time is {details['wait_time']}. "
        text += f"Certificate package includes ops: {details['cert_package']['ops']} and "
        text += f"qtfa: {details['cert_package']['qtfa']}. "
        text += f"Bootstrap information version is {details['bootstrap_info']['Bootstrap_Version']} "
        text += f"from date {details['bootstrap_info']['Date']}. "
        text += f"SSSD information status is {details['sssd_info']}. "
        text += "\n\n"
    return text

data=''
with open('test_data_sample.json', 'r') as file:
    data = json.load(file)

final_text = json_to_text(data['node_data'])
print(final_text)


with open("Output.txt", "w") as text_file:
    text_file.write(final_text)