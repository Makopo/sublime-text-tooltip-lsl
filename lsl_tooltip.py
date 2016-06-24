import sublime, sublime_plugin
import json
import webbrowser

TooltipData = json.loads(sublime.load_resource("Packages/TooltipLSL/tooltipdata.json"))

def plugin_loaded():
    global TooltipData

class Lsl(sublime_plugin.TextCommand):

    def on_navigate(self, link):
        webbrowser.open_new_tab(link)

    def on_hover(self, view, point, hover_zone):

        if view.settings().get('is_widget'):
            return

        if not view.settings().get('show_definitions'):
            return

        if hover_zone != sublime.HOVER_TEXT:
            return

        word = view.substr(view.word(point))

        if not word:
            return

        if not TooltipData:
            return

        if not TooltipData[word]:
            return

        self.view.show_popup(
            TooltipData[word],
            flags=sublime.COOPERATE_WITH_AUTO_COMPLETE|sublime.HIDE_ON_MOUSE_MOVE_AWAY,
            location=point, max_width=1024,
            on_navigate=self.on_navigate)
