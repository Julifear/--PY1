import json

def csv_to_list_dict(filename: str, delimiter: str = ",") -> list[dict]:
    with open(filename) as input_csv:
        headers = input_csv.readline().strip().split(delimiter)

        data = []
        for row in input_csv:
            row_values = row.strip().split(delimiter)
            data.append(dict(zip(headers, row_values)))
    return data

INPUT_FILE = "input.csv"
data = csv_to_list_dict(INPUT_FILE)

if __name__ == "__main__":
    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))