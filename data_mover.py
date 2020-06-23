import json
import collections
import sys

def move_data(prev_path, current_path):
	with open(prev_path) as f:
		prev_data = json.load(f)
	with open(current_path) as f:
		current_data = json.load(f, object_pairs_hook=collections.OrderedDict)

	for key, value in current_data.items():
		if key in prev_data:
			current_data[key] = prev_data[key]
			prev_data.pop(key, None)
		else:
			print("Key {0} is not in previous data!".format(key))
	print(prev_data)

	for key, value in prev_data.items():
		current_data[key] = value

	with open(current_path, "w") as f:
		json.dump(current_data, f, ensure_ascii=False, indent=2)

move_data(sys.argv[1], sys.argv[2])
