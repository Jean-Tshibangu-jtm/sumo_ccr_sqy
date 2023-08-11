import os
import sys

def convert_xml_to_csv(input_dir, output_dir):
    # Iterate over XML files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(input_dir, filename)
            csv_filename = filename.replace('.xml', '.csv')
            csv_path = os.path.join(output_dir, csv_filename)

            # Execute the command for each XML file
            command = f"/Data1/Tools/sumo/tools/xml/xml2csv.py -s , {xml_path} -o {csv_path}"
            os.system(command)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 xml_batch_converter.py <input_directory> <output_directory>")
    else:
        input_directory = sys.argv[1]
        output_directory = sys.argv[2]
        convert_xml_to_csv(input_directory, output_directory)
