import os
from mkdocs import utils
from mkdocs.plugins import BasePlugin

class LocalSearchPlugin(BasePlugin):

    def on_pre_build(self, config, **kwargs):
        config['extra_javascript'].append('search/search_index.js')

    def on_post_build(self, config, **kwargs):
        output_base_path = os.path.join(config['site_dir'], 'search')
        json_output_path = os.path.join(output_base_path, 'search_index.json')
        js_output_path = os.path.join(output_base_path, 'search_index.js')
        f = open(json_output_path,"r")
        search_index = "const idxJson = " + f.read() + "; const index = Promise.resolve(idxJson)"
        utils.write_file(search_index.encode('utf-8'), json_output_path)
        f.close()
        os.rename(json_output_path, js_output_path)