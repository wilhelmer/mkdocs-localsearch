# mkdocs-localsearch

A MkDocs plugin to replace the native "search" plugin with a search plugin that also works locally (file:// protocol)

## Installation

Install the plugin using pip:

`pip install mkdocs-localsearch`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
```

Add `search_index.js` to the `extra_javascript` section in `mkdocs.yml`:
```yaml
extra_javascript:
  - search/search_index.js
```

## How It Works

See https://github.com/mkdocs/mkdocs/pull/1805

Modifications to the solution given above:

- The JS code given in `fetch_shim.js` is appended to `search_index.js`, so there's no need for a separate JS file.
- The plugin doesn't distinguish between local and web calls. It always uses `search_index.js`.
- The plugin only modifies the fetch function if the url parameter contains "search_index.js". Otherwise, it uses the the native fetch function.

```javascript
fetch_native = fetch;
fetch = function (url, options) {
    if (url.indexOf("search_index.js") !== -1) {
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