import os
import logging
from mkdocs import utils
from mkdocs.plugins import BasePlugin

log = logging.getLogger('mkdocs')

class LocalSearchPlugin(BasePlugin):

    def on_post_build(self, config, **kwargs):
        if 'search' in config['plugins']:
            output_base_path = os.path.join(config['site_dir'], 'search')
            json_output_path = os.path.join(output_base_path, 'search_index.json')
            js_output_path = os.path.join(output_base_path, 'search_index.js')
            # Open JSON search index file
            f = open(json_output_path,"r")
            # Assign the JSON object to a JS variable
            search_index = "const local_index = " + f.read() + ";"
            utils.write_file(search_index.encode('utf-8'), json_output_path)
            f.close()
            # Rename JSON to JS
            os.rename(json_output_path, js_output_path)
        else:
            log.warning('localsearch: Missing search plugin. You must add both search and localsearch to the list of plugins in mkdocs.yml.')