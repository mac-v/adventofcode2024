import requests
import json


def get_cookies():
    json_path = 'cookie_data.json'
    with open(json_path, 'r') as json_path:
        cookies = json.load(json_path)
    print(cookies)
    return cookies


def calculate_sum_of_diffs(left_list, right_list):
    diff_sum = sum(abs(a - b) for a, b in zip(left_list, right_list))
    return diff_sum


def convert_to_int_list(data_list):
    return [int(x) for x in data_list]


def extract_locations(cookies, url):
    response = requests.get(url, cookies=cookies)
    content = (response.content.decode('utf-8').replace('\n', '  ')).replace('   ', '  ')
    ids = content.split('  ')
    even_indexed = convert_to_int_list(sorted(ids[::2][:-1]))
    odd_indexed = convert_to_int_list(sorted(ids[1::2]))

    return even_indexed, odd_indexed


if __name__ == '__main__':
    cookies = get_cookies()
    URL = 'https://www.adventofcode.com/2024/day/1/input'
    left_list, right_list = extract_locations(cookies, URL)
    sum = calculate_sum_of_diffs(left_list, right_list)
    print("Size of lists: ", len(left_list))
    print("Sum of differences: ", sum)