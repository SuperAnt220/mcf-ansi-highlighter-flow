from flowlauncher import FlowLauncher
import webbrowser
from Highlighter import Highlighter
import pyperclip

class Highlight(FlowLauncher):

    def copy(self, txt, *withMarkdown):
        if withMarkdown:
            txt = "```ansi\n" + txt + "\n```"
        pyperclip.copy(txt)

    def open_url(self, url):
        webbrowser.open(url)

    def query(self, query):
        if query != '':
            highlighted = str(Highlighter.highlight(query))
            return [
                {
                    "Title": "Copy Highlighted text: {}".format(highlighted),
                    "SubTitle": "Copy the output to the clipboard",
                    "IcoPath": "Images/logo.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [highlighted]
                    },
                    "score": 1
                },
                {
                    "Title": "Copy the output with markdown",
                    "SubTitle": "With these ```ansi ``` things",
                    "IcoPath": "Images/logo.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [highlighted, True]
                    },
                    "score": 0
                }
        ]
        else:
            highlighted_from_clip = str(Highlighter.highlight(pyperclip.paste()))
            return [
                {
                    "Title": "Highlighted text from clipboard: {}".format(highlighted_from_clip.split("\n")[0][:-1] + " ..."),
                    "SubTitle": "Copy ",
                    "IcoPath": "Images/logo.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [highlighted_from_clip]
                    },
                    "score": 1
                },
                {
                    "Title": "Copy the output from your clipboard with markdown",
                    "SubTitle": "With these ```ansi ``` things",
                    "IcoPath": "Images/logo.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [highlighted_from_clip, True]
                    },
                    "score": 0
                }
            ]

    def context_menu(self, data):
        return [
            {
                "Title": "Open highlighter web app",
                "SubTitle": "Made by bth123",
                "IcoPath": "Images/logo.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://bth123.github.io/mcf-ansi-highlighter/"]
                }
            },
            {
                "Title": "Open highlighter github",
                "SubTitle": "From bth123",
                "IcoPath": "Images/logo.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/bth123/mcf-ansi-highlighter"]
                }
            }
        ]