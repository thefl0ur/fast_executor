# FAst eXecutor

Fast Executor is a Sublime Text 3/4 plugin that allow you to fast prove your script, 
without distracting for selecting directory, filename, etc.

After executing, result from `stdout` is shown in output panel. If `stderr` is available, it 
will be concatenated to output.

## Supported languages
Currently supported next executors:
 * Python3 (`python3`)
 * TypeScript (`tsc`)
 * JavaScript (`node`)

Binaries expected to be presented in `PATH`. But you always can provide your full path.
 
## Installation
1. Clone this repository into your Sublime Text `Packages` directory.
2. Restart Sublime Text.

## Usage
Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and search for "Fast Execute".

By default, there is keybinding `ctr`+`shift`+`x` for fast executing python script.

## Settings

You can provide next arguments for command:
   * suffix - used for saving file with provided extension (default `.py`)
   * executor - program for call (default `python3`)
   * options - additional options for passing to executor (default `null`)

Example settings:

```json
{
    "keys": ["ctrl+shift+x"],
    "command": "faxecutor",
    "args" : {
         "executor": "python",
         "options": ["-v", "-b"]
    }
}
