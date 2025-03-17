# Main.md

## Basic Syntax

### Headings
# Heading Level 1
## Heading Level 2
### Heading Level 3
#### Heading Level 4
##### Heading Level 5
###### Heading Level 6

### Paragraphs

This is a paragraph. Simply write text on a line and add a blank line before and after for a new paragraph.

This is another paragraph with some *italic text* and some **bold text**.

### Line Breaks
Here's a line with a break at the end.  
And this appears on a new line due to two trailing spaces above.

### Emphasis
*Italic text using asterisks*
_Italic text using underscores_

**Bold text using double asterisks**
__Bold text using double underscores__

***Bold and italic text using triple asterisks***
___Bold and italic text using triple underscores___

### Blockquotes
> This is a blockquote. You can use it to emphasize text or show quotations.
>
> You can have multiple paragraphs in a blockquote by adding a > on the blank line between paragraphs.

> Nested blockquotes are possible too
>> Here's a nested blockquote

### Lists

#### Ordered Lists
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Another indented item
4. Fourth item

#### Unordered Lists
- First item
- Second item
- Third item
    - Indented item
    - Another indented item
- Fourth item

* Asterisks also work
+ And plus signs too

#### Task Lists
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task to do
### Super and sub script

^2^nd h~2~0

### Horizontal Rules

---
Three hyphens create a horizontal rule

***
Three asterisks also work

___
As do three underscores

### Code

Inline `code` with backticks

Code in full 

```python
from os import scandir

import markdown
from flask import *
from markupsafe import Markup


def createApp():
    app: Flask = Flask(__name__)
    view_funcs = {}
    template: str = ''
    with open('./templates/index.htm') as t:
        template = t.read()

    def create_view_func(html_content):
        return lambda: html_content

    with scandir('./templates/blogs') as entries:
        for entry in entries:
            try:
                with open(entry.path) as f:
                    print(entry.path)
                    content = template.replace('{{content}}', markdown.markdown(f.read(),
                                                                                extensions=['extra', 'admonition',
                                                                                            'codehilite',
                                                                                            'legacy_attrs', 'legacy_em',
                                                                                            'meta', 'nl2br',
                                                                                            'sane_lists', 'smarty',
                                                                                            'toc', 'wikilinks']))

                    html = Markup(content)
                    view_func_name = f'view_{entry.name.replace(".", "_")}'  # Generate a unique name
                    unique_view_func = create_view_func(html)
                    app.add_url_rule(f'/{entry.name.split(".")[0]}/', endpoint=view_func_name,
                                     view_func=unique_view_func)

            except Exception as e:
                print(e)

    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule}: {rule.endpoint}")

    return app


if __name__ == '__main__':
    server = createApp()
    server.run(debug=True, port=5001, use_reloader=False)
```