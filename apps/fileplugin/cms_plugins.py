from cms.plugin_pool import plugin_pool
from cms.plugins.file.cms_plugins import FilePlugin as CMSFilePlugin
from models import File


class FilePlugin(CMSFilePlugin):
    model = File


plugin_pool.unregister_plugin(FilePlugin)
plugin_pool.register_plugin(FilePlugin)
