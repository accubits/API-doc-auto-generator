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
    doc.text("title: "+collection['name'])
    doc.text("language_tabs:\n  - shell")
    doc.text("toc_footers:\n - <a href='https://github.com/accubits'>Documentation Powered by Accubits</a>")
    doc.text("search: true")
    doc.hr()
    doc.title("Introduction")
    doc.text(collection['description'])
 
    for module in collection['folders']:
        doc.title(module['name'])
        for api in collection['requests']:
            if module['id'] == api['folder']:
                doc.title(api['name'],2)
                # doc.text("> The API returns JSON structured like this:")
                # request = api["request"]
                # response = api["response"]
                # doc.code_block(response[0]["body"],"json")
                doc.text(api["description"])
                doc.title("HTTP request",3)
                doc.text("`"+api["method"]+" "+api["url"]+"`")

                if api['method'] == 'POST':
                    if api['dataMode'] == 'raw':
                        doc.text("> POST raw data JSON:")
                        doc.code_block(api['rawModeData'],'json')
                
                if api['headerData']:
                    doc.title("Headers",3)
                    rows = get_rows(
                        api['headerData'],
                        ['key', 'description', 'value']
                    )
                    doc.table(['Parameter', 'Description', 'Value'], rows)

                if api['queryParams']:
                    doc.title("Query Params",3)
                    rows = get_rows(
                        api['queryParams'],
                        ['key', 'description', 'value']
                    )
                    doc.table(['Parameter', 'Description', 'Value'], rows)

                if api['method'] == 'POST':
                    if api['dataMode'] in ['formdata', 'urlencoded', 'params']:
                        doc.title("POST parameters",3)
                        rows = get_rows(
                            api['data'],
                            ['key','description', 'value']
                        )
                        doc.table(['Parameter', 'Description', 'Example'], rows)
                    elif api['dataMode'] == 'file':
                        doc.text(api['file']['src'])
        doc.title("Untitled")
        for api in collection['requests']:
            if api['folder'] == None:
                doc.title(api['name'],2)
                doc.text(api["description"])
                doc.title("HTTP request",3)
                doc.text("`"+api["method"]+" "+api["url"]+"`")

                if api['method'] == 'POST':
                    if api['dataMode'] == 'raw':
                        doc.text("> POST raw data JSON:")
                        doc.code_block(api['rawModeData'],'json')
                
                if api['headerData']:
                    doc.title("Headers",3)
                    rows = get_rows(
                        api['headerData'],
                        ['key', 'description', 'value']
                    )
                    doc.table(['Parameter', 'Description', 'Value'], rows)

                if api['queryParams']:
                    doc.title("Query Params",3)
                    rows = get_rows(
                        api['queryParams'],
                        ['key', 'description', 'value']
                    )
                    doc.table(['Parameter', 'Description', 'Value'], rows)

                if api['method'] == 'POST':
                    if api['dataMode'] in ['formdata', 'urlencoded', 'params']:
                        doc.title("POST parameters",3)
                        rows = get_rows(
                            api['data'],
                            ['key','description', 'value']
                        )
                        doc.table(['Parameter', 'Description', 'Example'], rows)
                    elif api['dataMode'] == 'file':
                        doc.text(api['file']['src'])

            # if request['body']:
            #     content = request['body'][request['body']['mode']]
            #     if request['body']['mode'] == 'file' and isinstance(content, dict):
            #         content = content.get('src', '')

            #     if content:
            #         doc.title("Query parameters",3)
            #         if request['body']['mode'] in ['formdata', 'urlencoded']:
            #             rows = get_rows(
            #                 request['body'][request['body']['mode']],
            #                 ['key','description', 'value']
            #             )
            #             doc.table(['Parameter', 'Description', 'Example'], rows)
            #         elif request['body']['mode'] == 'raw':
            #             doc.code_block(request['body']['raw'])
            #         elif request['body']['mode'] == 'file':
            #             doc.text(request['body']['file']['src'])
    

    with open(out_file, 'w+') as f:
        f.write(doc.output())

