# mkdocs-localsearch

A MkDocs plugin to replace the native "search" plugin with a search plugin that also works locally (file:// protocol)

**NOTE:** This plugin only works with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, version 5.x. If you need support for other themes, feel free to create a pull request.

## Installation

1. Install the plugin using pip: `pip install mkdocs-localsearch`
2. Activate the plugin in `mkdocs.yml`, in addition to the `search` plugin:
    ```yaml
    plugins:
        - localsearch
        - search
    ```
