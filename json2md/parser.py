import json
from ctor import MDDoc


def get_rows(raw, keys):
    result = list()
    for i in raw:
        result.append([i.get(k, '') for k in keys])
    return result


def parse(in_file, out_file):
    doc = MDDoc()

    with open(in_file) as f:
        collection = json.load(f)

    # The basic info.
    doc.hr()
    doc.text("title: "+collection['info']['name'])
    doc.text("language_tabs:\n  - shell")
    doc.text("toc_footers:\n - <a href='https://github.com/accubits'>Documentation Powered by Accubits</a>")
    doc.text("search: true")
    doc.hr()
    doc.title("Introduction")
    doc.text(collection['info']['description'])
 
    for module in collection['item']:
        doc.title(module['name'])
        for api in module['item']:
            doc.title(api['name'],2)
            doc.text("> The API returns JSON structured like this:")
            request = api["request"]
            response = api["response"]
            doc.code_block(response[0]["body"],"json")
            doc.text(request["description"])
            doc.title("HTTP request",3)
            doc.text("`"+request["method"]+" "+request["url"]["raw"]+"`")

            doc.title("Headers",3)
            if request['header']:
                rows = get_rows(
                    request['header'],
                    ['key', 'description', 'value']
                )
                doc.table(['Parameter', 'Description', 'Value'], rows)

            
            if request['body']:
                content = request['body'][request['body']['mode']]
                if request['body']['mode'] == 'file' and isinstance(content, dict):
                    content = content.get('src', '')

                if content:
                    doc.title("Query parameters",3)
                    if request['body']['mode'] in ['formdata', 'urlencoded']:
                        rows = get_rows(
                            request['body'][request['body']['mode']],
                            ['key','description', 'value']
                        )
                        doc.table(['Parameter', 'Description', 'Example'], rows)
                    elif request['body']['mode'] == 'raw':
                        doc.code_block(request['body']['raw'])
                    elif request['body']['mode'] == 'file':
                        doc.text(request['body']['file']['src'])
    

    with open(out_file, 'w+') as f:
        f.write(doc.output())

