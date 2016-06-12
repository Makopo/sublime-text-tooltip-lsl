import sublime, sublime_plugin
import os
import xml.etree.ElementTree as etree

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

        # I temporarily borrow the logic from @buildersbrewery here for PoC - it will be replaced later on
        try:
            tooltipRows = []
            for result in KWDB.findall(".//*[@name='" + word + "']"):
                if result.tag == 'param':
                    continue
                if result.tag == 'function' or result.tag == 'constant':
                    tooltipRows.append('### (%s) <a href="https://wiki.secondlife.com/w/index.php?title=Special:Search&go=Go&search=%s">%s</a>' % (result.get('type', 'void'), result.get('name'), result.get('name')))
                else:
                    tooltipRows.append('### <a href="https://wiki.secondlife.com/w/index.php?title=Special:Search&go=Go&search=%s">%s</a>' % (result.get('name'), result.get('name')))
                if result.tag == 'constant':
                    tooltipRows.append(' ')
                    tooltipRows.append('**Value**: %s' % str(result.get('value')))
                if result.get('status', None) is not None and result.get('status', 'normal') != 'normal':
                    tooltipRows.append(' ')
                    tooltipRows.append('<body style="color:#fff;background-color:#820124;">**Status**: %s</body>' % result.get('status', 'normal'))
                if result.get('delay', None) is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('**Delay**: %s' % str(result.get('delay')))
                if result.get('energy', None) is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('**Energy**: %s' % str(result.get('energy')))
                if result.tag == 'function' or result.tag == 'event':
                    if result.findall('./param') != []:
                        tooltipRows.append(' ')
                        tooltipRows.append('#### Parameters')
                        for param in result.iter('param'):
                            tooltipRows.append('* (%s) **%s**' % (param.get('type'), param.get('name')))
                if result.find('description').text is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('#### Description')
                    tooltipRows.append(' ')
                    tooltipRows.append('%s' % result.find('description').text.strip())

        except Exception as e:
            print(e)

        self.view.show_popup('\n'.join(tooltipRows),
            location=-1, max_width=600, max_height=350
        )

        Pref.isActive = True
        Pref.word = word

def plugin_loaded():
    global Pref
    global KWDB

    class Pref:
        def load(self):
            Pref.debug = False
            Pref.isActive = False
            Pref.word = ""
    Pref = Pref()
    Pref.load()

    kwdbElementTree = etree.parse(os.path.join(sublime.packages_path(), 'TooltipLSL', 'kwdb.xml'))
    KWDB = kwdbElementTree.getroot()
 