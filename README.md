# mkdocs-localsearch

A MkDocs plugin to replace the native "search" plugin with a search plugin that also works locally (file:// protocol)

**NOTE:** This plugin only works with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, version 5.x. If you need support for other themes, feel free to create a pull request.

## Installation

1. Install the plugin using pip: `pip install mkdocs-localsearch`
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
4. Add `custom_dir` to the `theme` section in `mkdocs.yml`:
    ```yaml
    theme:
        name: material
        custom_dir: theme
    ```
5. Open [this file](https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/material/partials/header.html) and save it in your project dir as `theme/partials/header.html`.
6. Edit `theme/partials/header.html` and change the following line:<br>
   `{% if "search" in config["plugins"] %}`<br>
   to this:<br>
   `{% if "localsearch" in config["plugins"] %}`
7. Done!

## How It Works

See https://github.com/mkdocs/mkdocs/pull/1805

Modifications to the solution given above:

- The JS code given in `fetch_shim.js` is appended to `search_index.js` (in minified format), so there's no need for a separate JS file.
- `fetch_shim.js` has been tweaked as follows (code shown below): 
    - No distinction between local and web use. Always use `search_index.js` file instead of `search_index.json`.
    - Only use the shim if the fetch function is used to fetch `search_index.json`. For all other fetches, use the native fetch function.

```javascript
fetch_native = fetch;
fetch = function (url, options) {
    if (url.indexOf("search_index.json") !== -1) {
        return new Promise(
            function (resolve, reject) {
                var shimResponse = {
                    json: function () {
                        return shim_searchIndex;
                    }
                }
                resolve(shimResponse)
            }
        )
    }
    else {
        return fetch_native(url, options);
    }
}
```
