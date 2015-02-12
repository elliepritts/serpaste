# serpaste

```

                  /((((((\\\\
          =======((((((((((\\\\\
               ((           \\\\\\\
               ( (*    _/      \\\\\\\
                 \    /  \      \\\\\\________________
                  |  |   |       </                  ((\\\\
                  o_|   /        /                      \ \\\\    \\\\\\\
                       |  ._    (                        \ \\\\\\\\\\\\\\\\
                       | /                       /       /    \\\\\\\     \\
               .______/\/     /                 /       /         \\\
              / __.____/    _/         ________(       /\
             / / / ________/`---------'         \     /  \_
            / /  \ \                             \   \ \_  \
           ( <    \ \                             >  /    \ \
            \/      \\_                          / /       > )
                     \_|                        / /       / /
                                              _//       _//
                                             /_|       /_|
                                             
                                             
```

Serpaste is a tool I created to speed up workflow at my production artist gig. I use this tool to gather screenshots of lengthy menus, like the settings menu on the iPhone, and create one simple image of the entire thing. This process normally would take around 15 minutes to do with photoshop from scratch. Now it only takes a few seconds :) 

### Setup

1. Download serpaste.py and [get-pip.py](https://pip.pypa.io/en/latest/installing.html) to desktop.
1. Create a folder titled “images” on the desktop.
1. Open serpaste.py and modify line 7 to reflect your user name.
1. Open Terminal and type the following command: `cd ~/Desktop` and press enter.
1. Then type the following command: `sudo python get-pip.py` You will be prompted to enter your account password.
1. Lastly, enter the following command: `sudo pip install Pillow`.


### Application

1. Import iOS screenshots directly to the `images` folder you created. Do not resize or rename the files.
1. Open Terminal, type: `Python` and then drag the serpaste.py folder into terminal. Then press enter to run the code.
1. Open your "images" folder and voila! There is a new image called `composite.PNG` with all your screenshots magically stitched together.

### Demo video!
You can see me walk through these steps in my demo video: http://youtu.be/LgxfdE7qAeM
