# https://open-platform.theguardian.com/documentation/tag
query = "weather"
section = "news"
page = "1"
query_url = f"http://content.guardianapis.com/tags?" \
            f"api-key={apikey}" \
            f"&q={query}" \
            f"&page={page}"

r = requests.get(query_url)
pprint(r.json())

{'response': {'currentPage': 1,
              'pageSize': 10,
              'pages': 139,
              'results': [
                          {'apiUrl': 'https://content.guardianapis.com/australia-news/australia-weather',
                           'id': 'australia-news/australia-weather',
                           'sectionId': 'australia-news',
                           'sectionName': 'Australia news',
                           'type': 'keyword',
                           'webTitle': 'Australia weather',
                           'webUrl': 'https://www.theguardian.com/australia-news/australia-weather'},
                          {'apiUrl': 'https://content.guardianapis.com/world/extreme-weather',
                           'id': 'world/extreme-weather',
                           'sectionId': 'world',
                           'sectionName': 'World news',
                           'type': 'keyword',
                           'webTitle': 'Extreme weather',
                           'webUrl': 'https://www.theguardian.com/world/extreme-weather'},
                          ],
              'startIndex': 1,
              'status': 'ok',
              'total': 1385,
              'userTier': 'developer'}}