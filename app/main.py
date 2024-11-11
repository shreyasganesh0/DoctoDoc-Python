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
    
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return document
def add_format(default_formats, new_format):
    newdict={}
    for default in default_formats:
        newdict[default] = default_formats[default]
    newdict[new_format] = True
    return newdict 


def remove_format(default_formats, old_format):
    newdict={}
    for default in default_formats:
        newdict[default] = default_formats[default]
    newdict[old_format] = False 
    return newdict 
def list_files(current_filetree, current_path=""):
    res=[]
    def dfs(current_filetree, current_path):
        if current_filetree== None:
            res.append(current_path)
            return
        for i in current_filetree:
            dfs(current_filetree[i], current_path+"/"+i)
    dfs(current_filetree, "")
    return res
#below function is an example for function transformations
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option):
        pass

    return filter_cmd

def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")

