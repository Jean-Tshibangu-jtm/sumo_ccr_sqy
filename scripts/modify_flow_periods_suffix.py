import argparse
import xml.etree.ElementTree as ET
import re


def modify_flow_periods(file_path, suffix, new_value, new_color):
    # Load the SUMO flow file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find and modify the 'period' attribute for matching flows
    for flow_elem in root.iter('flow'):
        flow_id = flow_elem.get('id')
        if flow_id.endswith(suffix):
            flow_elem.set('period', 'exp({})'.format(new_value))
            flow_elem.set("color", new_color)
    
    # Save the modified SUMO flow file
    tree.write(file_path)

def reduce_edge_spaces(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find and modify the 'edges' attribute for all flow elements
    for flow_elem in root.findall(".//flow"):
        route_elem = flow_elem.find("route")
        if route_elem is not None:
            edges = route_elem.get("edges")
            if edges is not None:
                edges = " ".join(edges.split())
                route_elem.set("edges", edges)

    # Write the modified XML back to the file
    tree.write(file_path)

        
if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser(description='Modify SUMO flow file')
    
    # Add arguments
    parser.add_argument('file_path', type=str, help='Path to the SUMO flow file')
    parser.add_argument('suffix', type=str, help='Ending pattern for flow IDs')
    parser.add_argument('new_value', type=float, help='New value for the period attribute')
    parser.add_argument('new_color', type=str, help='New color value')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the modify_flow_periods function with the provided arguments
    modify_flow_periods(args.file_path, args.suffix, args.new_value, args.new_color)
    reduce_edge_spaces(args.file_path)
