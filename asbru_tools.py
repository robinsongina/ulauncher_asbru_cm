import subprocess
import os

def send_notification(text):
    subprocess.run(["notify-send",
                    "-h", "int:transient:1",
                    "--icon=" + os.path.dirname(os.path.realpath(__file__)) + "/images/icon.svg",
                    text,
                    "ULauncher AsbruConnectionManager"
                    ])

def get_connections():
    process = subprocess.run(['asbru-cm', '--list-uuids'], stdout = subprocess.PIPE)
    connections_for_groups = []
    connections = process.stdout.decode('utf8')
    # print(connections)
    try:
        connections = connections.split("\n")[4:-2]
        groups = [ { "uuid": conn.split("|")[0].strip(), "name": conn.split("|")[-1].strip() } for conn in connections if "GROUP" in conn ]
        
        for group in groups:
            for conn in connections:
                if group["uuid"] in conn and "SSH" in conn:
                    tmp = { "uuid": conn.split("|")[0].strip(), "name": "%s %s"%(group["name"], conn.split("|")[-1].strip()), "server": conn.split("|")[-1].strip() }
                    connections_for_groups.append(tmp)
    except:
        return []
   
    return connections_for_groups
    
def connect(uuid: str):
    process = subprocess.run(['asbru-cm', f'--start-uuid={uuid}'], stdout = subprocess.PIPE)
    # print(process.stdout.decode('utf8'))
    return process.stdout.decode('utf-8')
     
# conns = get_connections()
# print(conns)
# connect("1f3c4e0c-1a84-44b3-8def-a7b5ec6cc160")