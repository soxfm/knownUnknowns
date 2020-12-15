query = "(hurricane OR storm)"
query_fields = "body"
section = "news"  # https://open-platform.theguardian.com/documentation/section
tag = "world/extreme-weather"  # https://open-platform.theguardian.com/documentation/tag
from_date = "2019-01-01"
query_url = f"https://content.guardianapis.com/search?" \
            f"api-key={apikey}" \
            f"&q={query}" \
            f"&query-fields={query_fields}" \
            f"§ion={section}" \
            f"&tag={tag}" \
            f"&from-date={from_date}" \
            f"&show-fields=headline,byline,starRating,shortUrl"

r = requests.get(query_url)
pprint(r.json())