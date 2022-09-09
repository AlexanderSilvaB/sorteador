# -*- coding: utf-8 -*-
# @Author: Alexander Silva Barbosa
# @Date:   2022-09-09 12:13:25
# @Last Modified by:   Alexander Silva Barbosa
# @Last Modified time: 2022-09-09 13:56:14

import os
import sys
import json
import copy
import random
import string
import glob

CODE_LENGTH = 5
CODE_CHARS = string.ascii_uppercase + string.digits

def main(args):
    if len(args) > 0:
        config_file = args[0]
    else:
        config_file = "config.json"
    
    with open(config_file) as file:
        config = json.load(file)
    
    output = 'resultados/' + config['output']
    os.makedirs(output, exist_ok=True)
 
    files = glob.glob(output + '/*')
    for f in files:
        os.remove(f)

    
    

    
    url = config['url'] + '/' + output

    title = config['title']
    restrictions = config['restrictions']
    template = config['template']

    restrictions = '<br/>'.join(restrictions)

    results = {}
    links = {}
    participants = copy.copy(config['participants'])
    for participant in config['participants']:
        code = ''.join(random.choice(CODE_CHARS) for _ in range(CODE_LENGTH))
        while code in results:
            code = ''.join(random.choice(CODE_CHARS) for _ in range(CODE_LENGTH))

        results[code] = random.choice(participants)
        while results[code] == participant:
            results[code] = random.choice(participants)
        participants.remove(results[code])

        file_name = code + '.html'
        links[participant] = url + '/' + file_name

        with open(template) as file:
            html = file.read()
        
        html = html.replace("$NAME", results[code])
        html = html.replace("$TITLE", title)
        html = html.replace("$RESTRICTIONS", restrictions)


        with open(output + '/' + file_name, 'w') as file:
            file.write(html)

    try:
        with open('results.json') as file:
            results = json.load(file)
    except:
        results = {}

    results[title] = links
    
    with open('results.json', 'w') as file:
        file.write(json.dumps(results))

    links = {}
    for title in results:
        for person in results[title]:
            if person not in links:
                links[person] = {}
            links[person][title] = results[title][person]

    text = ''
    for person in links:
        text += person + '\n'
        for title in links[person]:
            text += title + ': ' + links[person][title] + '\n'
        text += '\n'
    
    print(text)
    with open('results.txt', 'w') as file:
        file.write(text)

if __name__ == "__main__":
    main(sys.argv[1:])
