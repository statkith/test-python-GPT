import pypandoc

def convert (doc_url,txt_url):

    output = pypandoc.convert_file(doc_url, 'plain', outputfile=txt_url)
    assert output == ""