import os
import logging
from mkdocs import utils
from mkdocs.plugins import BasePlugin

log = logging.getLogger('mkdocs')

class LocalSearchPlugin(BasePlugin):

    def on_pre_build(self, config, **kwargs):
        if 'search' in config['plugins']:
            config['extra_javascript'].append('search/search_index.js')
        else:
            log.warning('localsearch: Missing search plugin. You must add both localsearch and search to the list of plugins in mkdocs.yml.')

    def on_post_build(self, config, **kwargs):
        if 'search' in config['plugins']:
            output_base_path = os.path.join(config['site_dir'], 'search')
            json_output_path = os.path.join(output_base_path, 'search_index.json')
            js_output_path = os.path.join(output_base_path, 'search_index.js')
            f = open(json_output_path,"r")
            search_index = "const idxJson = " + f.read() + "; const index = Promise.resolve(idxJson)"
            utils.write_file(search_index.encode('utf-8'), json_output_path)
            f.close()
            os.rename(json_output_path, js_output_path)