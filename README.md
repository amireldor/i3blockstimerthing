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

The script saves a file with the unix timestamp of the time to calculate since when it started as well as the timer's state, which in that case just saves the "second count" at pause time. By default, it's writing a file in `/tmp` somewhere to not pollute your home folder (how cnsiderate!). The filepath is configurable via the `I3BLOCKSTIMERTHING_FILE` env var which can be magically passed like this:

	[i3blockstimerthing]
	command=/home/amir/dev/i3blockstimerthing/i3blockstimerthing.py
	interval=1
	I3BLOCKSTIMERTHING_FILE=/home/amir/.i3blockstimerthing

Saving the file in your home folder makes it persist between reboots which is super-awesome.


## TODO

 - [x] Configurable filename for keeping timer start, allowing to keep the timer running even after restatrts
 - [ ] Be red and sad when >25m, should also be configurable for on/off and the time passed for when to shout at you
 - [ ] Better python-foo
 - [ ] Customizable formatting of the text
 - [ ] Does anyone want this to run for days? hours? if so, support h:mm:ss formats :) and not only m:ss
 - [ ] I think that's it, I'm very proud of myself.
