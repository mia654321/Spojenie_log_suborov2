import unittest
import xml.etree.ElementTree as ET
from Uloha1 import update_interface_statuses


class MyTestCase(unittest.TestCase):
    def test_add_status_to_interface(self):
        xml_data = """
        <configuration>
            <network>
                <interface name="eth0">
                    <ip>192.168.0.1</ip>
                </interface>
                <interface name="eth1">
                    <ip>192.168.0.2</ip>
                    <status>disabled</status>
                </interface>
            </network>
        </configuration>
        """
        tree = ET.ElementTree(ET.fromstring(xml_data))
        updated_tree = update_interface_statuses(tree)
        root = updated_tree.getroot()
        interfaces = root.find('network').findall('interface')

        # pridám status
        self.assertEqual(interfaces[0].find('status').text, 'enabled')

if __name__ == '__main__':
    unittest.main()
