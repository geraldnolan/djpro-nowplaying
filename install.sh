#!/bin/bash
if python -m pip --version &> /dev/null; then
    echo 'Pip Installed'
else
     #--------------------------------------------------
        # Install Dependencies
        #--------------------------------------------------
        echo -e "\n--- Installing Pip --"
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

        sudo python get-pip.py
fi

pip install watchdog --user --no-warn-script-location











