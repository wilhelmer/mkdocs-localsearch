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

This plugin appends the `fetch_shim.js` content (minified) to `search_index.js`, so there's no need for a separate JS file.

Also, the plugin doesn't distinguish between local and web calls, so the fetch shim is much simpler:

```javascript
fetch = function (url, options) {
    return new Promise(
        function (resolve, reject) {
            var shimResponse = {
                json: function () {
                    // This should return the search index
                    return shim_localSearchIndex;
                }
            }
            resolve(shimResponse)
        }
    )
}
```