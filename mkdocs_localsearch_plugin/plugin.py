import os
import logging
from mkdocs import utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

log = logging.getLogger('mkdocs')

class LocalSearchPlugin(BasePlugin):

    config_scheme = (
        ('keep_both', config_options.Type(bool, default=False)),
    )

    def on_post_build(self, config, **kwargs):
        if 'search' in config['plugins']:
            output_base_path = os.path.join(config['site_dir'], 'search')
            json_output_path = os.path.join(output_base_path, 'search_index.json')
            js_output_path = os.path.join(output_base_path, 'search_index.js')
            # Open JSON search index file
            f = open(json_output_path,"r")
            if self.config["keep_both"]:
                # Use JS variable on file protocol, keep JSON on others
                search_index = "const local_index = " + f.read() + "; var __config = (location.protocol === 'file:' ? { search: { index: new Promise(resolve => setTimeout(() => resolve(local_index), 100)) } } : undefined)" 
                # Write to JS file. Both JS and JSON will be kept
                utils.write_file(search_index.encode('utf-8'), js_output_path)
                f.close()
            else:
                # Use JS variable on all protocols
                search_index = "const local_index = " + f.read() + "; var __config = { search: { index: new Promise(resolve => setTimeout(() => resolve(local_index), 100)) } }"
                # Write to JSON file and rename JSON to JS
                utils.write_file(search_index.encode('utf-8'), json_output_path)
                f.close()
                os.rename(json_output_path, js_output_path)
        else:
            log.warning('localsearch: Missing search plugin. You must add both search and localsearch to the list of plugins in mkdocs.yml.')