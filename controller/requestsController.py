import urllib3 as urllib3
import json
import pathlib

from controller import searchController as sc


def get_github_api_response(url, api_token=None, headers=None):
    """
    Make a request to the GitHub API, and return the body of the response.

    :param api_token: API token to use in HTTP Basic Auth requests.  You don't
        have to provide this, but some API endpoints require authorization,
        and others are rate-limited without authorization.  (Optional)
    :param headers: Any extra HTTP headers to add to the request.  (Optional)

    """
    if headers is None:
        headers = {}

    # Add the Authorization header
    if api_token is not None:
        headers.update(urllib3.util.make_headers(basic_auth=api_token))

    # The GitHub API rejects requests that don't have a User-Agent header.
    headers["User-Agent"] = f"Python script {__file__}, written by alexwlchan"

    http = urllib3.PoolManager()
    resp = http.request("GET", url, headers=headers)

    if resp.status != 200:
        raise print(
            f"❌ - Non-200 HTTP status code from GitHub ({resp.status}): {resp.data}")

    return resp.data


def get_cache_path(url, file_name):
    return pathlib.Path("result") / (str(file_name) + ".txt")


def save_json_response(url, api_key_start, data):
    cache_path = get_cache_path(url, api_key_start)
    cache_path.parent.mkdir(exist_ok=True)

    json_string = json.dumps(data, indent=2, sort_keys=True)

    json_data = json.loads(json_string)

    keys_list = ""
    for item in json_data["search_response"]["items"]:
        for matches in item["text_matches"]:
            if api_key_start in matches["fragment"]:
                key = api_key_start + matches["fragment"].split(api_key_start)[1]

                key = key.split()[0]
                for i in ["(", ")", ",", ";", " ", "&", "'", '"', "`"]:
                    key = key.split(i)[0]

                if key != api_key_start and key not in keys_list:
                    keys_list = keys_list + key + '\n'

    # with open(cache_path, "w") as f:
    #     f.write(keys_list)

    cache_path.write_text(keys_list)

    return cache_path
