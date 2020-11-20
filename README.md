# jinja-reverse

A simple tool to reverse a Jinja2 template. Check out this blog post [How to reverse a Jinja template](https://hodo.dev/posts/post-12-jinja-reverse) for more details.

## Installation

```bash
pip3 install https://github.com/gabihodoroaga/jinja-reverse/releases/download/v0.1/jinja_reverse-0.1-py3-none-any.whl
```

or

```bash
git clone https://github.com/gabihodoroaga/jinja-reverse.git

cd jinja-reverse

python3 setup.py install

```

## Example usage

```bash
jinja-reverse -f example/templates -b base.html -s example/samples -g "*.html"
```

## Arguments for jinja-reverse

```txt
-f, --folder        The folder where the tempalates will be created and where the base exists
-b, --base          The base jinja tempalte file
-s, --samples       The samples folder.
-g, --glob          The samples glob pattern
```

## jinja-generate

This is an additional tool to generate a list of files from a list of templates.

```bash
jinja-generate -f example/templates -g "*.j2" -o example/out
```

## Arguments for jinja-generate

```txt
-f, --folder        The folder where the tempalates will be created and where the base exists
-g, --glob          The samples glob pattern
-o, --output        The output folder
```

## Authors

* Gabriel Hodoroaga
