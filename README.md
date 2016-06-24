# LSL/OSSL Tooltip Reference for Sublime Text

## Currently supported languages

* LSL [`*.lsl`]: Second Life 16.05.24.315768
* OSSL [`*.ossl`]: OpenSimulator v0.7.5-rc1
  * Including mod\*, os\*, wl\*(LightShare) functions

[kwdb](https://bitbucket.org/Sei_Lisa/kwdb) version 0.0.20160606000

**I try to update the keyword list as soon as it is updated by kwdb, however, I sometimes may not be able to do that. Please refrain from requesting maintenance for at least one month after the kwdb have higher version than the version above. If you want to make an urgent request, please poke me via [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).**

## Installation

This bundle is designed to work with the latest version of [Sublime Text 3](http://www.sublimetext.com/).

### Using [Package Control](https://packagecontrol.io)

The easiest way to install this is via Package Control.

 * If you just went and [installed Package Control](https://packagecontrol.io/installation), you probably need to restart [Sublime Text 3](http://www.sublimetext.com/) before doing this next bit.
 * Bring up the Command Palette (<kbd>Command ⌘</kbd><kbd>Shift ⇧</kbd><kbd>P</kbd> on OS X, <kbd>Ctrl</kbd><kbd>Shift ⇧</kbd><kbd>P</kbd> on Linux/Windows).
 * Select `Package Control: Install Package` (it'll take a few seconds)
 * Type and select `TooltipLSL` when the list appears.

Package Control will automatically keep this bundle up to date with the latest version.

### Using Git

Alternatively, if you are a git user, you can install the plugin and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text application settings area.

You can locate your Sublime Text `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the plugin repository using the command below:

```git
  git clone https://github.com/Makopo/sublime-text-tooltip-lsl TooltipLSL
```

### Download Manually

* Download the files using the GitHub [*.zip](https://github.com/makopo/sublime-text-tooltip-lsl/archive/master.zip) and [*.tar.gz](https://github.com/makopo/sublime-text-tooltip-lsl/archive/master.tar.gz) download options.
* Unzip the files and rename the folder to `TooltipLSL`.
* Copy the folder to your Sublime Text `Packages` directory.

# Usage

Hovering over a word with your mouse will show a tooltip, moving away from the tooltip with your mouse will hide the tooltip again.

![tooltip2](https://raw.githubusercontent.com/Makopo/sublime-text-tooltip-lsl/forimages/tooltip2.png)

* You can use this feature on any type of file, even on simple text file.
* You are not required to use [my LSL/OSSL plugin](https://github.com/Makopo/sublime-text-lsl) to use this plugin.
