# i3blockstimerthing

Hello. I hacked up this script for i3blocks (or i3xrocks if you use [Regolith](https://regolith-linux.org) like me). What it does is count time up so I know when I was sitting too much and should go stretch and have a glass of water. You can even pause the timer! Wow!

![awesome demonstration](timer2.gif)

Left clicking on it resets the timer. Right or middle click will toggle pause.

The Pomodoro Technique is also nice. Use it.

## How? Why?

I believe you have some kind of Python 3.
Clone/download this script, make sure it's executable, and then in your i3blocks or i3xrocks config do something like this:

	[timerthing]
	command=/home/amir/dev/i3blockstimerthing/i3blockstimerthing.py
	interval=1

I put it just before my `[time]` block so I can be happier with my life.

Now restart something and you should see it.

The script saves a file with the timestamp along with the timer's state. This is used to calculate how much time passed since the save and that's what you see on the bar. When paused, it saves the seconds count of the moment along an indication of the paused state. When toggled back, it calculates a new "start" timestamp relative to the seconds count.

This file is by default saved into `/tmp` so I don't pollute your home folder (how considerate of me!). You can change that with an `I3BLOCKSTIMERTHING_FILE` environment variable which is easily passed-through from your i3blocks config:

	[i3blockstimerthing]
	command=/home/amir/dev/i3blockstimerthing/i3blockstimerthing.py
	interval=1
	I3BLOCKSTIMERTHING_FILE=/home/amir/.i3blockstimerthing

Saving the file in your home folder makes it persist between reboots which is super-awesome(!).

## TODO

 - [x] Configurable filename for keeping timer start, allowing to keep the timer running even after restatrts
 - [ ] Be red and sad when >25m, should also be configurable for on/off and the time passed for when to shout at you
 - [ ] Better python-foo
 - [ ] Customizable formatting of the text
 - [x] Does anyone want this to run for days? hours? if so, support h:mm:ss formats :) and not only m:ss (thanks AdrianoFerrari)
 - [ ] I think that's it, I'm very proud of myself.
