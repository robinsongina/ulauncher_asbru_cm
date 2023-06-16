import asbru_tools
import os
import logging

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = logging.getLogger(__name__)

class AsbruConnectionManager(Extension):
     def __init__(self):
        super(AsbruConnectionManager, self).__init__()

        # Subscribe plugin listeners to launcher
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        search_query = event.get_argument()
        connections = asbru_tools.get_connections()
        connections = sorted(connections, key=lambda d: d["name"].lower())

        items = []
        for a in connections:
            name = a["name"]
            if search_query is not None and search_query not in name.lower():
                continue

            description = "Probando Ando"
            icon_path = 'images/network-server.svg'

            if not os.path.isfile(icon_path):
                logger.warning("Icon not found: " + icon_path)

            on_click_event = ExtensionCustomAction(a, keep_app_open=False)
            item_row = ExtensionResultItem(icon=icon_path,
                                           name=name,
                                           description=description,
                                           on_enter=on_click_event)
            items.append(item_row)

        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        pass


if __name__ == '__main__':
    AsbruConnectionManager().run()