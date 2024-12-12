### FastAPI Translation
```
pip install fastapi-and-babel
```
Other methods and modules exists, this is simple to use and works.

```python
from fastapi import FastAPI, Request
from fastapi_and_babel.translator import FastAPIAndBabel
from fastapi_and_babel import gettext as _
app = FastAPI()
app_language = "en" # or zh, es, fr etc..
translator = FastAPIAndBabel(root_dir=__file__, app=app, translation_dir="lang")
# root dir __file__ means the directory of this file, app is the FastAPI app
translator.set_default_locale(app_language)
```

```python
template = Jinja2Templates(directory="templates")
template.env.globals['_'] = _ # Important for Jinja2 to use _
```

```python
# Python Translation syntax
_("String to translate")
```

### Jinja Translation Syntax
```html
{{ _('String to translate') }}
```
### Initializing Translation
Create a file `babel.cfg` in the root of your project with the following content:
```ini
[ignore: **/venv/**]
[python: **.py]
[jinja2: **/templates/**.html]
```
- any ignore needs to be added before
The folder `lang` will be used for translation. The first step is using `pybabel` to initialize the translation, it takes all .py files and .html
```bash
pybabel extract -F babel.cfg -o lang/messages.pot .
```
### Create and Updating Translation
```bash
pybabel init -i lang/messages.pot -d lang -l en
pybabel init -i lang/messages.pot -d lang -l zh
```
Afterward, compile the translation
```bash
pybabel compile -d lang
```
To update the translation, extract the messages again and update the translation
```bash
pybabel extract -F babel.cfg -o lang/messages.pot .
pybabel update -i lang/messages.pot -d lang
```
