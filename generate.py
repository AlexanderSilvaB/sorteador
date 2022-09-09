# -*- coding: utf-8 -*-
# @Author: Alexander Silva Barbosa
# @Date:   2022-09-09 12:13:25
# @Last Modified by:   Alexander Silva Barbosa
# @Last Modified time: 2022-09-09 12:57:14

import os
import sys
import json
import copy
import random
import string

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
    url = config['url'] + '/' + output

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
        links[participant] = url + '#' + code

    title = config['title']
    restrictions = config['restrictions']
    template = config['template']

    restrictions = '<br/>'.join(restrictions)

    with open(template) as file:
        html = file.read()
    
    html = html.replace("$DATA", json.dumps(results))
    html = html.replace("$TITLE", title)
    html = html.replace("$RESTRICTIONS", restrictions)
    
    

    try:
        os.mkdir('resultados')
    except:
        pass

    with open(output, 'w') as file:
        file.write(html)

    results = json.dumps(links, indent=4)
    print(results)
    
    with open('results.json', 'w') as file:
        file.write(results)

if __name__ == "__main__":
    main(sys.argv[1:])
