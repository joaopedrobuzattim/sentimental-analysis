import re

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
