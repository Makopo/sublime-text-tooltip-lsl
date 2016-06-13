import sublime, sublime_plugin
import json
import webbrowser

class LslTooltipListener(sublime_plugin.EventListener):

    def on_selection_modified_async(self, view):
        if not (Pref.isActive):
            return

        if(view.substr(view.word(view.sel()[0])) != Pref.word):
            view.hide_popup()
            Pref.isActive = False

class LslTooltipCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # I let it be used by everywhere, even in simple text file or phonix preprocessor scripts.

        # select word
        word = self.view.substr(self.view.word(self.view.sel()[0]))

        # display popup
        self.view.show_popup(TooltipData[word], location=-1, max_width=600, max_height=350, on_navigate=self.on_navigate)

        Pref.isActive = True
        Pref.word = word

    def on_navigate(self, link):
        webbrowser.open_new_tab(link)

def plugin_loaded():
    global Pref
    global TooltipData

    class Pref:
        def load(self):
            Pref.isActive = False
            Pref.word = ""
    Pref = Pref()
    Pref.load()

    TooltipData = json.loads(sublime.load_resource("Packages/TooltipLSL/tooltipdata.json"))
