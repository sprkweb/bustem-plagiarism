# Get plain text from an EditorJS markup
def plaintext_from_editorjs(editorjs_data):
    text = []
    for block in editorjs_data['blocks']:
        if 'text' in block['data']:
            text.append(block['data']['text'])
        else:
            print('Unknown block type: ' + block['type'])
    return ' '.join(text)