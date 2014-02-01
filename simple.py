import re
import sys

try:
    TEXT = sys.argv[1]
except IndexError:
    TEXT = "Here is some <em>HTML</em> markup. Another <b>element</b>"
else:
    TEXT = TEXT.replace('\n', '').replace('\r', '')

TAG_RE = re.compile(r"<(?P<tag>[a-zA-Z0-9]+?)\w?.*?>(?P<content>.*?)</(?P=tag)>")

class Tag(object):
    def __init__(self, tag, content=""):
        self.tag = tag
        self.content = content
        self.nice_content = None
        self.children = []

    def __repr__(self):
        return "<%(tag)s>%(content)s</%(tag)s>[%(child_count)d]" % {
            "tag": self.tag,
            "content": self.content,
            "child_count": len(self.children)
        }

# list of found root tags
TAGS = []

def find_tags(text):
    "return list of found tags"
    match = TAG_RE.findall(text)
    found = []
    if match:
        for tag, content in match:
            found.append(Tag(tag, content))
    return found

def fetch_tags():
    def _find_tags(tag):
        tags_found = find_tags(tag.content)
        for tf in tags_found:
            tf.children = _find_tags(tf)
        return tags_found
    global TEXT
    global TAGS
    tags_found = find_tags(TEXT)
    for tag in tags_found:
        TAGS = find_tags(TEXT)
        for t in TAGS:
            t.children = _find_tags(t)

def display_tags():
    global TAGS
    
    def _display_tag(tag, level):
        print "%s%s (%s)" % (" " * level, tag.tag, tag.content)
        if tag.children:
            for child in tag.children:
                _display_tag(child, level+4)
    level = 0
    for tag in TAGS:
        _display_tag(tag, level)

fetch_tags()
display_tags()
