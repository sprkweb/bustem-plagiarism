# Get plain text from an EditorJS markup
def plaintext_from_editorjs(editorjs_data: dict) -> str:
    text = []
    for block in editorjs_data['blocks']:
        if 'text' in block['data']:
            text.append(block['data']['text'])
        elif block['type'] == 'list':
            for item in block['data']['items']:
                text.append(item)
        elif block['type'] == 'image':
            pass
        elif block['type'] == 'code':
            pass
        else:
            print('Unknown block type: ' + block['type'])
    return ' '.join(text)