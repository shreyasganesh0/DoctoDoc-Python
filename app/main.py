from decorators import *

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

# function to demonstrate closures
def new_collection(initial_docs):
    copylist = initial_docs.copy()
    def new(newval):
        copylist.append(newval)
        return copylist 
    return new
# function to demonstrate currying
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def in_doc(doc):
            count =0
            for i in doc.split("\n"):
                if sequence in i:
                    count+=1
            return count
        return in_doc
    return with_char

#decorator demo function    
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        newlist = []
        for arg in args:
            newlist.append(convert_md_to_txt(arg))
        newdict = {}
        for k in kwargs:
            newdict[k] = convert_md_to_txt(kwargs[k])
        return func(*newlist, **newdict)
    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)



@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""  First: {first_doc}
  Second: {second_doc}"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""  Title: {title}
  Body: {body}
  Conclusion: {conclusion}"""

# enforcing sum types using enums
from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            content = content[2:]
            content = "<h1>" +content+"</h1>"
        case(DocFormat.TXT, DocFormat.PDF):
            content = "[PDF] "+content+" [PDF]"
        case(DocFormat.HTML, DocFormat.MD):
            content = content[4:len(content)-5]
            print(content)
            content = "# "+ content
        case _:
            raise TypeError("Invalid type")
    return content
