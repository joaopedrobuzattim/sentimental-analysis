import re
import requests
import time

def getUrl(url, headers, params):
    for i in range(0, 20):
        try:
          response = requests.get(url=url, headers=headers, params=params)

          if(response.status_code == 403):
            raise Exception('RateLimitError')
          if(response.status_code != 200):
            raise Exception('Request error')

        except Exception as e:
          print(e)
          if(e.args[0] == 'RateLimitError'):
              print('Sleeping app for 10 minutes!')
              time.sleep(600)

          print(f"Starting retry: {i}")
          if(i == 19):
              print("Retry failled")
              exit(1)
        else:
          break
    return response

    

##This function will be used on senti-strentgth stage...
def cleanText(text):
    parsed = text.replace('\n', '') \
        .replace('\r', '') \
        .replace('##', '') \
        .replace('#', '') \
        .replace('- [x]', '') \
        .replace('- [ ]', '')

    parsed = re.sub(r'`````.+?`````', '', parsed)
    parsed = re.sub(r'````.+?````', '', parsed)
    parsed = re.sub(r'```.+?```', '', parsed)
    parsed = re.sub(r'``.+?``', '', parsed)
    parsed = re.sub(r'`.+?`', '', parsed)
    parsed = re.sub(r'<!--.+?--', '', parsed)
    parsed = re.sub(r'\d', '', parsed)

    parsed = \
        parsed \
            .replace('"', "") \
            .replace("'", "") \
            .replace("(", " ") \
            .replace(")", " ") \
            .replace("[", " ") \
            .replace("]", " ") \
            .replace(">", "") \
            .replace("/", "-") \
            .replace("<", "") \
            .replace("|", "") \
            .replace("`", "") \
            .replace("*", "") \
            .replace("{", "") \
            .replace("}", "") \
            .replace("%", "")

    parsed = re.sub(' +', ' ', parsed)

    return parsed


