Twitch Plays
============

Clone of [Twitch Plays Pokemon](http://twitch.tv/twitch_plays_pokemon).

Modifications by [JackNet](https://github.com/Jacknet).

Original code by [aidanrwt](https://github.com/aidanrwt).

macOS/Linux/*NIX port by [ynohtna92](https://github.com/ynohtna92)

Under the MIT license.

Requirements
============

It is recommended to use [2.7.x releases](http://www.python.org/download/releases/2.7/) of Python.

For Microsoft Windows, keystrokes are performed by utilising Windows API calls through the [PyWin32 extension](http://sourceforge.net/projects/pywin32/), which must be installed alongside a normal Python for Windows installation.

For macOS/Linux/*NIX installs, keystrokes are performed through xdotool/xautomation. Check your distro's repositories if it's available for install through your package manager.

How To Run
============

Rename `config/config_dist.py` to `config/config.py` and replace the default username/password values with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Feel free to modify button throttles there aswell.

In your Emulator, set the controls to the following keys:

```
Up: 0
Down: 1
Left: 2
Right: 3
Button A: 4
Button B: 5
Button X: 6
Button Y: 7
Start: 8
Select: 9
Button L: A
Button R: B
```

If necessary, comment out any buttons you don't want to use in the `lib/game.py` script.

After setup, open up your terminal and type `python serve.py`. If your username/password is wrong, you will be notified.

Whilst the script is running, make sure you have the emulator in focus as your primary window since the commands are only sent to the active window. If you click onto another window, the keypresses might disrupt operation of the program in focus. If you're unable to maintain a window focused should you need to do other things with your computer, run the emulator and script within a virtual machine.
