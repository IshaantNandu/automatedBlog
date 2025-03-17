# AUTOMATED MARKDOWN BLOG

***

## INSTALLATION

Requires python 3.8 or bigger.

```bash
pip install flask markdown markupsafe markdown_sub_sup iconfonts markdown_del_ins kbdextension markdown_checklist pygments
```

Then, to clone the repo, use

```bash
git clone http://github.com/IshaantNandu/automatedBlog.git
```

***

## CUSTOMIZATION

You can change the style of your website by changing the `css` file. Run 
```bash
 pygmentize -S default -f html > src/static/main.css
```
where default can be replaced by one of the styles  at <https://pygments.org/styles/>.

***
## USAGE

Running 
```bash
python3 ./src/wsgi.py
```
will activate a server. You can add as many `.md` markdown files in `./src/templates/blogs`.
The 

