# Mcfunction ANSI Highlighter - Flow
[Mcf-ansi-highlighter](https://github.com/bth123/mcf-ansi-highlighter), adapted as a [flow launcher](https://github.com/Flow-Launcher/Flow.Launcher) plugin.

## Usage
Open the search window and type `hl` - the plugin will automatically try to highlight the text you have in your clipboard. This method supports multiple commands. If you type any text after the action keyword `hl`, the plugin will instead highlight it. This method supports only one command. Afterwards you will be able to choose between copying just the highlighted text or with markdown formatting  (\`\`\`ansi \`\`\`) for discord messages.

### Example
Flow launcher query:

`hl execute store result storage namespace:storage temp.lvl int 1 run scoreboard players get @s level`

Result:

![example](Images/example.png)
---
### Example №2
User's clipboard content:
```
say hi
scoreboard players remove @s timer 1
execute at @e[type=villager] run setblock ~ ~3 ~ anvil
```

Flow launcher query:

`hl`

Result:

![example2](Images/example2.png)