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
                                                                                            'toc', 'wikilinks',
                                                                                            "markdown_sub_sup",
                                                                                            'iconfonts',
                                                                                            'markdown_del_ins',
                                                                                            'kbdextension',
                                                                                            'markdown_checklist.extension']))

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
