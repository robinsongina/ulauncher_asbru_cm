import subprocess
from pprint import pprint

def get_connections():
    process = subprocess.run(['asbru-cm', '--list-uuids'], stdout = subprocess.PIPE)
    connections_for_groups = []
    connections = process.stdout.decode('utf8')
    # print(connections)
    try:
        connections = connections.split("\n")[4:-2]
        groups = [ { "uuid": conn.split("|")[0].strip(), "name": conn.split("|")[-1].strip() } for conn in connections if "GROUP" in conn ]
        
        for group in groups:
            tmp= [ { "uuid": conn.split("|")[0].strip(), "name": conn.split("|")[-1].strip() } for conn in connections if group["uuid"] in conn and "SSH" in conn]
            connections_for_groups.append({ group["name"]: tmp })
    except:
        return []
   
    return connections_for_groups
    
def connect(uuid: str):
    process = subprocess.run(['asbru-cm', f'--start-uuid={uuid}'], stdout = subprocess.PIPE)
    print(process.stdout.decode('utf8'))
     
# conns = get_connections()
# print(conns)
# connect("1f3c4e0c-1a84-44b3-8def-a7b5ec6cc160")