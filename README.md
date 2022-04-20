# greyboard

Take control over someone's keyboard.

## Current Features
- Can send single key, multiple key and hotkeys
- Get clipboard data
- Set clipboard data
- Persistence
- Can send two set of key presses with time interval
- currently runs on single machine

## Features to be added
- handle multiple connections

## Usage
```
*a -> presses 'a' key
*abcd -> presses 'abcd' keys
*alt+tab -> presses following shortcut
*abc/shortcut{{*2}}*cba/shortcut -> presses abc and waits for 2 seconds and presses cba
clipboard_data -> returns text copied to clipboard
copy~~~text to copy -> copys text to copy to victim's clipboard
pexit -> kills the connection

* -- means changable with same kind of key
```