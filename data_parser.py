import json
import re

def clean_text(text):
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'_[a-z]+_', '', clean)
    return clean.strip()

corpus = []

pattern = re.compile(r"\((\d+), '(.*?)', '.*?', '.*?', \d+, \d+, \d+, '.*?', \d+, NULL, \d+, '(.*?)', \d+, '.*?', '(.*?)', '.*?', '.*?', '.*?'\),?")

#You will need to add your own local paths
with open('', 'r', encoding='utf-8') as file:
    for line in file:
        matches = pattern.findall(line)
        for match in matches:
            word = match[1]
            definition = match[2]
            examples = match[3]
            if word:
                cleaned_definition = clean_text(definition)
                cleaned_examples = clean_text(examples)
                corpus.append({
                    "word": word,
                    "definition": cleaned_definition,
                    "examples": cleaned_examples if examples else None
                })

json_corpus = json.dumps(corpus, ensure_ascii=False, indent=2)

with open('', 'w', encoding='utf-8') as f:
  f.write(json_corpus)

