import os
import yaml
import json

yaml_directory = "yaml"
json_directory = "json"

if not os.path.exists(json_directory):
    os.makedirs(json_directory)

yaml_files = [file for file in os.listdir(yaml_directory)]

for yaml_file in yaml_files:
    yaml_file_path = os.path.join(yaml_directory, yaml_file)
    
    with open(yaml_file_path, 'r') as file:
        #yaml_data = ''.join(file.readlines()[1:-1])
        yaml_data = file.read()
        json_data = json.dumps(yaml.safe_load(yaml_data), ensure_ascii=False, indent=2)
    
    json_file_name = os.path.splitext(yaml_file)[0] + ".json"
    json_file_path = os.path.join(json_directory, json_file_name)
    
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

print("Finished")

