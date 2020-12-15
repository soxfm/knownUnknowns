# https://open-platform.theguardian.com/documentation/section
query = "science"
query_url = f"https://content.guardianapis.com/sections?" \
            f"api-key={apikey}" \

r = requests.get(query_url)
pprint(r.json())

{'response': {'results': [{'apiUrl': 'https://content.guardianapis.com/science',
                           'editions': [{'apiUrl': 'https://content.guardianapis.com/science',
                                         'code': 'default',
                                         'id': 'science',
                                         'webTitle': 'Science',
                                         'webUrl': 'https://www.theguardian.com/science'}],
                           'id': 'science',
                           'webTitle': 'Science',
                           'webUrl': 'https://www.theguardian.com/science'}],
              'status': 'ok',
              'total': 1,
              'userTier': 'developer'}}