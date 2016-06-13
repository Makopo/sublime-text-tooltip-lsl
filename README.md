LSL/OSSL Tooltip Reference for Sublime Text
==========

# Current supported language

* LSL [\*.lsl]: Second Life 16.05.24.315768
* OSSL [\*.ossl]: OpenSimulator v0.7.5-rc1
  - Including mod\*, os\*, wl\*(LightShare) functions

[kwdb](https://bitbucket.org/Sei_Lisa/kwdb) version 0.0.20160606000

**I try to update the keyword list as soon as it is updated by kwdb, however, I sometimes may not be able to do that. Please refrain from requesting maintenance for at least one month after the kwdb have higher version than the version above. If you want to make an urgent request, please poke me via [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).**

# Installation

This bundle is designed to work with the latest version of [Sublime Text 3](http://www.sublimetext.com/).

### Using Sublime Package Control

The easiest way to install this is via [Package Control](https://sublime.wbond.net).

 * If you just went and installed Package Control, you probably need to restart Sublime Text before doing this next bit.
 * Bring up the Command Palette (<kbd>Command</kbd><kbd>Shift</kbd><kbd>P</kbd> on OS X, <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Type and select "TooltipLSL" when the list appears.

Package Control will automatically keep this bundle up to date with the latest version.

### Using Git

Alternatively, if you are a git user, you can install the plugin and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text application settings area.

You can locate your Sublime Text `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the plugin repository using the command below:

    git clone https://github.com/Makopo/sublime-text-tooltip-lsl TooltipLSL

### Download Manually

* Download the files using the GitHub [*.zip](https://github.com/makopo/sublime-text-tooltip-lsl/archive/master.zip) and [*.tar.gz](https://github.com/makopo/sublime-text-tooltip-lsl/archive/master.tar.gz) download options.
* Unzip the files and rename the folder to `TooltipLSL`.
* Copy the folder to your Sublime Text `Packages` directory.

# Usage

1. Place the CARET on the name of function/constant/event.
2. Right click to show the context menu.
3. Select `Show in LSL Reference`, even for OSSL features.

![tooltip1](https://raw.githubusercontent.com/Makopo/sublime-text-tooltip-lsl/forimages/tooltip1.png)
![tooltip2](https://raw.githubusercontent.com/Makopo/sublime-text-tooltip-lsl/forimages/tooltip2.png)

* You can use this feature on any type of file, even on simple text file.
* You are not required to use [my LSL/OSSL plugin](https://github.com/Makopo/sublime-text-lsl) to use this plugin.

## Shortcut Key Assignment

To "Key Bindings - User", add (e.g. <kbd>Command</kbd><kbd>Shift</kbd><kbd>W</kbd> key for OSX):
```json
[
    { "keys": ["super+shift+w"], "command": "lsl_tooltip" }
]
```
