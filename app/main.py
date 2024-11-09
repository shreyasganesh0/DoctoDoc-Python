def stylize_title(document):
    return add_border(center_title(document))

def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)

def add_prefix(document, documents):
    
    doclist = [] 
    for i in range(len(documents)):
        doclist.append(documents[i])

    doclist.append(f'{len(documents)}. {document}')
    return tuple(doclist)

