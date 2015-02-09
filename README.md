serpaste
========

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

<p><b>Setup</b></p>

<ol>
  <li>Download serpaste.py and <a href="https://pip.pypa.io/en/latest/installing.html">get-pip.py</a> to desktop.</li>
  <li>Create a folder titled “images” on the desktop.</li>
  <li>Open serpaste.py and modify line 7 to reflect your user name.</li>
  <li>Open Terminal and type the following command: <i>cd ~/Desktop</i> and press enter.</li>
  <li>Then type the following command: <i>sudo python get-pip.py</i> You will be prompted to enter your account password.</li>
  <li>Lastly, enter the following command: <i>sudo pip install Pillow</i>.</li>
</ol>


<p><b>Application</b></p>

<ol>
  <li>Import iOS screenshots directly to the “images” folder you created. Do not resize or rename the files.</li>
  <li>Open Terminal, type: <i>Python</i> and then drag the serpaste.py folder into terminal. Then press enter to run the code.</li>
  <li>Open your "images" folder and voila! There is a new image called "composite.PNG" with all your screenshots magically stitched together.
</ol>


Demo video! http://youtu.be/LgxfdE7qAeM
