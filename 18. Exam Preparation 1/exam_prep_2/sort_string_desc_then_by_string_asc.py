a = { "a": {"name": "bobi", "grade": "exc"}, "b": {"name": "abi", "grade": "exc"}, }


sorted_a = sorted(a.items(), key=lambda x: x[1]["grade"], reverse=True)

for key, value in sorted_a:
    current_grade = value["grade"]
    sub_result = filter(lambda x: x[1]["grade"] == current_grade, sorted_a)
    sub_filtered_results = sorted(sub_result, key=lambda x: x[1]['name'])
    for s_key, val in sub_result:
        print()
    continue
print(sorted_a)