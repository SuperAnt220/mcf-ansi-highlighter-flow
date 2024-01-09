from flowlauncher import FlowLauncher,FlowLauncherAPI
import webbrowser
import Highlighter
import pyperclip



class Highlight(FlowLauncher):

    def query(self, query):
        global highlighted
        highlighted = ''
        withMarkdown = True
        if query != '':
            highlighted = str(Highlighter.highlight_text(query))
        return [
            {
                "Title": "Copy Highlighted text: {}".format((highlighted , highlighted)[highlighted == '']),
                "SubTitle": "Copy the output to the clipboard",
                "IcoPath": "logo.png",
                "JsonRPCAction": {
                    "method": "copy",
                    "parameters": [highlighted]
                },
                "score": 1
            },
            {
                "Title": "Copy the output with markdown",
                "SubTitle": "With these ```ansi ``` things",
                "IcoPath": "logo.png",
                "JsonRPCAction": {
                    "method": "copy",
                    "parameters": [highlighted, withMarkdown]
                },
                "score": 0
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Open highlighter web app",
                "SubTitle": "That supports multiple commands at once",
                "IcoPath": "logo.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://bth123.github.io/mcf-ansi-highlighter/"]
                }
            },
            {
                "Title": "Open highlighter github",
                "SubTitle": "From bth123",
                "IcoPath": "logo.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/bth123/mcf-ansi-highlighter"]
                }
            }
        ]

    def copy(self, txt, *withMarkdown):
        if withMarkdown:
            txt = "```ansi\n" + txt + "\n```"
        pyperclip.copy(txt)

    def open_url(self, url):
        webbrowser.open(url)