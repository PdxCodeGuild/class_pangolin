import psutil

fetch_remote_system_connections = list(psutil.net_connections(kind='inet4'))

def remote_connections(connections):
    ''' Function that takes in a list of (IPv4, Port) connections and returns a (k, v) pair dictionary '''
    b = []
    for i in range(len(connections)):
        b.append(connections[i][4])
    return  dict(list(filter(None, b))) # Filter funciton removes empty (k, v) pairs in the list.

# Variable stores the remote connections (k, v) tupples as a dictionary
remote_connections_dict = remote_connections(fetch_remote_system_connections)

print(remote_connections_dict)