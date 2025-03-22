# AUTOMATED MARKDOWN BLOG

***

## INSTALLATION

Requires python 3.8 or bigger.

```bash
$ pip install flask markdown markupsafe markdown_sub_sup iconfonts markdown_del_ins kbdextension markdown_checklist pygments
```

Then, to clone the repo, use

```bash
$ git clone http://github.com/IshaantNandu/automatedBlog.git
```

***

## CUSTOMIZATION

You can change the style of your website by changing the `css` file. Run 
```bash
$ pygmentize -S default -f html > src/static/main.css
```
where default can be replaced by one of the styles  at <https://pygments.org/styles/>.
Also, you can adjust the `index.htm` file at `./src/templates/index.htm` to customize [css frameworks](https://hackr.io/blog/best-css-frameworks/) or 
icons like [Font-awesome](https://fontawesome.com).

***

## Running

Run 
```bash
$ python3 -v ./src/wsgi.py
```
to turn on a server at <http://127.0.0.1:5001>.
You can add as many `.md` markdown files in `./src/templates/blogs`.
The server will automatically detect them. All the images should be in `./src/static/images`. You can use a server like [Gunicorn](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/) for professional development. 


