class Order_director:
    
    def __init__(self):
        self.cluster_list = {}
        self.client_list = {}
    
    def set_client(self, name, ref):
        if name not in self.client_list:
            client = Client(name, ref)
            self.client_list[name] = client
            return client
        else:
            print("A client  named {} already exists.".format(name))
            return self.client_list[name]
    
    def del_client(self, name):
        if name in self.client_list:
            for cluster in self.cluster_list:
                if self.client_list[name] in cluster.client_list:
                    cluster.del_client(self.client_list[name])
            del self.client_list[name]

    def set_cluster(self, name):
        if name not in self.cluster_list:
            cluster = Cluster(name)
            self.cluster_list [name] = cluster
            return cluster
        else:
            print("A cluster is alreday named {}".format(name))
            return self.get_cluster(name)
    
    def add_client_in_cluster(self, cluster, client_name):
        if cluster in self.cluster_list:
            if client_name in self.client_list:
                self.cluster_list[cluster].add_client(self.client_list[client_name])
            else:
                print("You must set the client before adding it to a cluster.")
    
    def del_client_in_cluster(self, cluster, client_name):
        if cluster in self.cluster_list:
            if client_name in self.client_list:
                self.cluster_list[cluster].del_client(self.client_list[client_name])
            else:
                print("The client {} doesn't exists.".format(client_name))
    
    def list_client_in_cluster(self, cluster):
        if cluster in self.cluster_list:
            return self.cluster_list[cluster].client_list

    def del_cluster(self, cluster):
        if cluster in self.cluster_list:
            del self.cluster_list[cluster]
        else:
            print("The cluster {} doesn't exists.".format(cluster))
    
    def send(self, order):
        target = input("Please enter the destination(s) :\n")
        target = target.split()
        if target[0] == "cluster":
            for i in range(1, target.len()):
                self. send_to_cluster(target[i], order)
        elif target[0] == "client":
            for i in range(1, len(target)):
                self.send_to_client(target[i], order)
        
    def send_to_client(self, client_name, order):
        for client in self.client_list:
            if client_name == client:
                self.server.send(self.client_list[client].ref, order)
                break
        else:
            print("The client {} isn't connected to this head.".format(client_name))
    
    def send_to_cluster(self, cluster_name, order):
        for cluster in self.cluster_list:
            if cluster_name == cluster:
                for client in self.cluster_list[cluster].client_list:
                    self.server.send(client.ref, order)
            break
        else:
            print("There is no cluster named {} on this head.".format(cluster_name))
    
    def get_client_status(self, client_name):
        if client_name in self.client_list:
            print(self.client_list[client_name].get_status())
    
    def get_cluster_status(self, cluster_name):
        if cluster_name in self.luster_list:
            for client in self.cluster_list[cluster_name].client_list:
                print(client.get_status())

class Cluster:
    def __init__(self, name):
        self.name = name
        self.client_list = []
    
    def add_client(self, client):
        if client not in self.client_list:
            self.client_list.append(client)
        else:
            print("The client {} is alreday in this cluster.".format(client.name))
    
    def del_client(self, client):
        if client in self.client_list:
            self.client_list.remove(client)
        else:
            print("The client {} is not in this cluster.".format(client.name))

class Client:
    def __init__(self, name, ref):
        self.name = name
        self.ref = ref

