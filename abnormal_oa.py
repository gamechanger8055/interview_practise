import json
import os


class SchemaTransformer:
    def __init__(self, schema_dir='schema', mapping_file='mapping.json'):
        self.schema_dir = schema_dir
        self.mapping_file = mapping_file
        self.mapping = self.load_mapping()

    def load_mapping(self):
        with open(self.mapping_file, 'r') as f:
            return json.load(f)

    def load_schema(self, schema_name):
        schema_path = os.path.join(self.schema_dir, f"{schema_name}.json")
        # print("sc",schema_path)
        with open(schema_path, 'r') as f:
            return json.load(f)

    def get_schema_name_from_filename(self, filename):
        filename = filename[:-5]
        # print("1",filename.split('_'))
        return filename.split('_')[1]

    def get_provider_from_filename(self, filename):
        return filename.split('_')[0]

    def build_from_json(self, json_file_path):
        with open(json_file_path, 'r') as f:
            input_data = json.load(f)

        filename = os.path.basename(json_file_path)
        schema_name = self.get_schema_name_from_filename(filename)
        provider_name = self.get_provider_from_filename(filename)

        schema = self.load_schema(schema_name)
        optional_fields = schema.get('optional', [])
        required_fields = [field for field in schema.keys() if field != 'optional']

        output_data = {}
        mapping = self.mapping.get(schema_name, {}).get(provider_name, {})

        # Map fields according to the mapping rules
        for input_field, schema_field in mapping.items():
            if input_field in input_data:
                output_data[schema_field] = input_data[input_field]

        # Handle non-mapped fields and apply conversions
        for field in input_data:
            if field not in mapping:
                output_field = field
                output_data[output_field] = self.convert_none_to_null(input_data[field])

        # Validate required fields are present
        for field in required_fields:
            if field not in output_data and field not in optional_fields:
                raise ValueError(f"Missing required field: {field}")

        return output_data

    def convert_none_to_null(self, value):
        # Convert None to null in the output data
        if isinstance(value, dict):
            return {k: self.convert_none_to_null(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self.convert_none_to_null(v) for v in value]
        elif value is None:
            return None  # This will be converted to null in JSON
        return value

    def transform_directory(self, input_dir, output_dir):
        for filename in os.listdir(input_dir):
            if filename.endswith('.json'):
                input_file_path = os.path.join(input_dir, filename)
                output_file_path = os.path.join(output_dir, filename)

                try:
                    output_data = self.build_from_json(input_file_path)
                    with open(output_file_path, 'w') as f:
                        json.dump(output_data, f, indent=4)
                except Exception as e:
                    print(f"Failed to transform {filename}: {e}")

