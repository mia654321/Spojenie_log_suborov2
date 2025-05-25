import sys
import xml.etree.ElementTree as ET

"""
Program načíta XML z lokálneho priečinka.
Zmení <status> do každého elementu <interface> na 'enabled'.
Súbor vieme zadať ako argument programu.
Uloží kópiu XML.
"""

# Načítať názov súboru z argumentu (alebo použiť default)
if len(sys.argv) >= 2:
    XML_FILE = sys.argv[1]
else:
    XML_FILE = 'exampleXML.xml'

CHANGED_XML_FILE = 'changed_' + XML_FILE

# Načíta XML strom
tree = ET.parse(XML_FILE)
root = tree.getroot()
network = root.find('network')

if network is not None:
    # Nájde každý <interface>
    for interface in network.findall('interface'):
        status_element = interface.find('status')
        # Ak <status> existuje, zmeň ho na 'enabled'
        if status_element is not None:
            status_element.text = 'enabled'
            print(f"Aktualizovaný <status> v interface {interface.get('name')}")
        else:
            # Ak <status> neexistuje, pridaj ho
            status_element = ET.Element('status')
            status_element.text = 'enabled'
            interface.append(status_element)
            print(f"Pridaný <status> do interface {interface.get('name')}")

# Uložiť do nového súboru
tree.write(CHANGED_XML_FILE, encoding='utf-8', xml_declaration=True)

print(f"Súbor '{XML_FILE}' bol upravený a uložený do '{CHANGED_XML_FILE}'.")
