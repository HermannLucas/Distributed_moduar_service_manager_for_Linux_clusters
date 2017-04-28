import unittest

from Core import SingletonDecorator 
from Head import Order_director
from Client.Module_manager import Manager

class Head_test_case(unittest.TestCase):
    def setUp(self):
        self.order_director = SingletonDecorator(Order_director)
        self.ord_dir = self.order_director()
        for i in range(1, 4):
            self.ord_dir.set_cluster("Fake_cluster{}".format(i))
            self.ord_dir.set_client("Fake_client{}".format(i), "Fake_ref{}".format(i))

    def test_is_singleton(self):
        self.assertIs(self.ord_dir, self.order_director())
    
    def test_create_cluster(self):
        cluster = self.ord_dir.set_cluster("cluster_test")
        self.assertIn("cluster_test", self.ord_dir.cluster_list)
        self.assertIs(cluster, self.ord_dir.cluster_list["cluster_test"])
    
    def test_retrieving_cluster(self):
        cluster = self.ord_dir.set_cluster("cluster_test")
        self.assertIs(cluster, self.ord_dir.cluster_list["cluster_test"])
    
    def test_create_client(self):
        client = self.ord_dir.set_client("client_test", ("ref_test"))
        self.assertIn("client_test", self.ord_dir.client_list)
        self.assertIs(client, self.ord_dir.client_list["client_test"])
    
    def test_retrieving_client(self):
        client = self.ord_dir.set_client("client_test", ("ref_test"))
        self.assertIs(client, self.ord_dir.client_list["client_test"])
    
    def tearDown(self):
        del self.ord_dir
        del self.order_director
    
class Cluster_test_case(unittest.TestCase):
    def setUp(self):
        self.order_director = SingletonDecorator(Order_director)
        self.ord_dir = self.order_director()
        for i in range(1, 4):
            self.ord_dir.set_cluster("Fake_cluster{}".format(i))
            self.ord_dir.set_client("Fake_client{}".format(i), "Fake_ref{}".format(i))
    
    def test_add_client(self):
        self.ord_dir.add_client_in_cluster("Fake_cluster1", "Fake_client1")
        self.assertIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
    
    def test_remove_client(self):
        for i in range(1, 4):
            self.ord_dir.add_client_in_cluster("Fake_cluster1", "Fake_client{}".format(i))
        self.assertIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
        self.ord_dir.del_client_in_cluster("Fake_cluster1", "Fake_client1")
        self.assertNotIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
    
    def tearDown(self):
        del self.ord_dir
        del self.order_director
    
class Core_test_case(unittest.TestCase):
    def setUp(self):
        self.module_manager = SingletonDecorator(Manager)
        self.mod_man = self.module_manager()
    
    def test_is_singleton(self):
        self.assertIs(self.mod_man, self.module_manager())
    
    def test_status(self):
        self.assertEqual(self.mod_man.get_status(), "Waiting")
    
    def test_get_status(self):
        status = "Test"
        self.mod_man.set_status(status)
        self.assertEqual(self.mod_man.get_status(), status)
    
    def tearDown(self):
        del self.mod_man
        del self.module_manager

if __name__ == '__main__':
    unittest.main()

#print("\n \n Starting test of the module manager.")
#mod_man = Manager()
#for module in mod_man.module_list:
#    print("Module {} is the object : {}".format(module, mod_man.module_list[module]))
#if "Fake plugin" in mod_man.module_list:
#    print("Module {} the vesion is : {}".format(mod_man.module_list["Fake plugin"].name, mod_man.module_list["Fake plugin"].version))
#print(mod_man.list_modules().split('--|--'))
