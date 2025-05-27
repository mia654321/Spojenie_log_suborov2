import sys
import xml.etree.ElementTree as ET

def update_interface_statuses(tree):
    """
    Aktualizuje alebo pridá <status> s hodnotou 'enabled' pre každý
    <interface>.
    """
    root = tree.getroot()
    network = root.find('network')
    if network is not None:
        for interface in network.findall('interface'):
            status_element = interface.find('status')
            if status_element is not None:
                status_element.text = 'enabled'
            else:
                status_element = ET.Element('status')
                status_element.text = 'enabled'
                interface.append(status_element)
    return tree

def load_and_modify_xml(input_path):
    """Načíta XML zo súboru, upraví ho a vráti ako strom."""
    tree = ET.parse(input_path)
    return update_interface_statuses(tree)

def save_xml(tree, output_path):
    """Uloží XML strom do súboru."""
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

# Spustiteľný ako skript z príkazového riadku
if __name__ == "__main__":
    XML_FILE = sys.argv[1] if len(sys.argv) >= 2 else 'exampleXML.xml'
    CHANGED_XML_FILE = 'changed_' + XML_FILE

    tree = load_and_modify_xml(XML_FILE)
    save_xml(tree, CHANGED_XML_FILE)
    print(f"✅ Súbor '{CHANGED_XML_FILE}' bol vytvorený.")
