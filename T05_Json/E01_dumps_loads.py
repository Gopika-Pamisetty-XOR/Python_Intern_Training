import json


def roundtrip(obj):
    text = json.dumps(obj)
    return json.loads(text)


sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}

# 1. Compact JSON text
compact = json.dumps(sample)
print(f"compact: {compact}")

# 2. Indented JSON with sorted keys
indented = json.dumps(sample, indent=2, sort_keys=True)
print("indented:")
print(indented)

# 3. Round-trip conversion and type changes
restored = roundtrip(sample)
print(f"scores type before: {type(sample['scores']).__name__} | after: {type(restored['scores']).__name__}")
print(f"married after: {restored['married']} | nickname after: {restored['nickname']}")
print(f"equal after round trip: {sample == restored}")

# 4. Integer dictionary keys
print(f"int keys: {roundtrip({1: 'a', 2: 'b'})}")

# 5. Catching TypeError when dumping a set
try:
    json.dumps({"tags": {1, 2, 3}})
except TypeError as e:
    print(f"TypeError: {e}")
