from controller import requestsController as rc

import hyperlink
import json
import re


def search_on_github(api_key, api_key_start, github_api):
    # https://developer.github.com/v3/search/#search-code
    api_url = hyperlink.URL.from_text("https://api.github.com/search/code")
    query_url = api_url.set("q", api_key)

    resp = rc.get_github_api_response(
        url=str(query_url),
        api_token=github_api,

        # This header means we get text-match data in the response, so we can
        # see which part of the code fragment matched this query.
        headers={"Accept": "application/vnd.github.v3.text-match+json"}
    )

    out_data = {
        "query": api_key,
        "search_response": json.loads(resp)
    }

    out_path = rc.save_json_response(url=query_url, api_key_start=api_key_start, data=out_data)

    return out_path


def slugify(u):
    """Convert Unicode string into blog slug."""
    # From https://leancrew.com/all-this/2014/10/asciifying/

    u = re.sub(u'[–—/:;,.]', '-', u)  # replace separating punctuation
    a = u.lower()  # best ASCII substitutions, lowercased
    a = re.sub(r'[^a-z0-9 -]', '', a)  # delete any other characters
    a = a.replace(' ', '-')  # spaces to hyphens
    a = re.sub(r'-+', '-', a)  # condense repeated hyphens
    return a
