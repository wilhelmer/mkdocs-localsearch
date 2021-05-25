# mkdocs-localsearch

A MkDocs plugin to make the native "search" plugin work locally (file:// protocol).

**NOTE:** This plugin only works with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. If you need support for other themes, feel free to create a pull request.

## Installation (Material v7)

To use the plugin with Material v7 projects:

1. Install the plugin using pip: `pip install mkdocs-localsearch`
2. Activate the plugin in `mkdocs.yml`, in addition to the `search` plugin:
    ```yaml
    plugins:
        - search
        - localsearch
    ```
3. Make sure that the `use_directory_urls` setting is set to `false` in `mkdocs.yml` to have filenames in the URL (required when using the file:/// protocol).
4. Add a `custom_dir` entry to the `theme` section in `mkdocs.yml`:
    ```yaml
    theme:
        name: material
        custom_dir: theme
    ```
5. Create a new file, save it in your project dir as `theme/main.html`, and add the following content: 
    ```html
    {% extends "base.html" %}
    {% block config %}
    {{ super() }}
    {% if "localsearch" in config["plugins"] %}
    <script src="https://unpkg.com/iframe-worker/polyfill"></script>
    <script src="{{ 'search/search_index.js' | url }}"></script>
    {% endif %}
    {% endblock %}
    ```
    **Note:** Don't use the `extra_javascript` option in `mkdocs.yml` to add the two scripts above. Scripts referenced via `extra_javascript` are placed at the bottom of the HTML page, i.e., after the search implementation, which is too late.
6. If your documentation should work **offline**, i.e., without internet access:
    1. Open [this file](https://unpkg.com/iframe-worker/polyfill) and save it as `iframe-worker.js` in your `docs_dir`.<br>
       Example path: `docs/assets/javascripts/iframe-worker.js`
    2. Edit `theme/main.html` and change the following line:
       ```html
       <script src="https://unpkg.com/iframe-worker/polyfill"></script>
       ```
       to this:
       ```html
       <script src="{{ 'assets/javascripts/iframe-worker.js' | url }}"></script>
       ```   

## Installation (Material v5 or v6)

To use the plugin with Material v5 or v6 projects:

1. Install version 0.7.0 of the plugin using pip: `pip install mkdocs-localsearch==0.7.0`
2. Activate the plugin in `mkdocs.yml`, in addition to the `search` plugin:
    ```yaml
    plugins:
        - search
        - localsearch
    ```
3. Make sure that the `use_directory_urls` setting is set to `false` in `mkdocs.yml` to have filenames in the URL (required when using the file:/// protocol).
4. Add a `custom_dir` entry to the `theme` section in `mkdocs.yml`:
    ```yaml
    theme:
        name: material
        custom_dir: theme
    ```
5. Create a new file, save it in your project dir as `theme/main.html`, and add the following content: 
    ```html
    {% extends "base.html" %}
    {% block config %}
    {% if "localsearch" in config["plugins"] %}
    <script src="https://unpkg.com/iframe-worker/polyfill"></script>
    <script src="{{ 'search/search_index.js' | url }}"></script>
    {% endif %}
    {% endblock %}
    ```
    **Note:** Don't use the `extra_javascript` option in `mkdocs.yml` to add the two scripts above. Scripts referenced via `extra_javascript` are placed at the bottom of the HTML page, i.e., after the search implementation, which is too late.
6. If your documentation should work **offline**, i.e., without internet access:
    1. Open [this file](https://unpkg.com/iframe-worker/polyfill) and save it as `iframe-worker.js` in your `docs_dir`.<br>
       Example path: `docs/assets/javascripts/iframe-worker.js`
    2. Edit `theme/main.html` and change the following line:
       ```html
       <script src="https://unpkg.com/iframe-worker/polyfill"></script>
       ```
       to this:
       ```html
       <script src="{{ 'assets/javascripts/iframe-worker.js' | url }}"></script>
       ```   
7. If your project has a **large search index** (several MBytes), add the `promise_delay` setting:
    ```yaml
    plugins:
        - search
        - localsearch:
            promise_delay: 100
    ```
    A delay of 100 ms worked with a search index of 24 MB ([prebuilt index](https://www.mkdocs.org/user-guide/configuration/#prebuild_index)).<br>Note that the `promise_delay` setting has a negative effect on performance (loading time will be increased).

**Note:** If you [customize search](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/#custom-search) settings, such as [query transformation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/#query-transformation), add the `useCustomSearch` setting:

```yaml
  - localsearch:
      useCustomSearch: true
```

Example of `theme/main.html` file is: 

```html
{% extends "base.html" %}
{% block config %}
{{ super() }}
{% if "localsearch" in config["plugins"] %}
<script src="{{ 'assets/javascripts/iframe-worker.js' | url }}"></script>
<script src="{{ 'search/search_index.js' | url }}"></script>
{% endif %}
<script src="https://cdn.jsdelivr.net/npm/tiny-segmenter@0.2.0/dist/tiny-segmenter-0.2.0.min.js"></script>
<script>
var __search = {
    index: Promise.resolve(local_index),
    transform: function(query) {
        var segmenter = new TinySegmenter();
        var segs = segmenter.segment(query);
        var newQuery = segs.join(" ");
        return newQuery;
    }
}
</script>
{% endblock %}
```

This setting is for Japanese "ja-jp" full-text search.

## Installation (Material v4)

To use the plugin with Material v4 projects:

1. Install version 0.5.0 of the plugin using pip: `pip install mkdocs-localsearch==0.5.0`
2. Activate the plugin in `mkdocs.yml`:
    ```yaml
    plugins:
        - localsearch
    ```
3. Add `search_index.js` to the `extra_javascript` section in `mkdocs.yml`:
    ```yaml
    extra_javascript:
        - search/search_index.js
    ```
4. Add a `custom_dir` entry to the `theme` section in `mkdocs.yml`:
    ```yaml
    theme:
        name: material
        custom_dir: theme
    ```
5. Open [this file](https://raw.githubusercontent.com/squidfunk/mkdocs-material/0730aae9c2ca8c689cc5ef4d214036b2d532138e/material/partials/header.html) and save it in your project dir as `theme/partials/header.html`.
6. Edit `theme/partials/header.html` and change the following line:<br>
   `{% if "search" in config["plugins"] %}`<br>
   to this:<br>
   `{% if "localsearch" in config["plugins"] %}`
