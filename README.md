
ulauncher-asbru_cm
=================

Asbru Connection Manager connect plugin for ULauncher.

This plugin allows you to connect to a connection from Asbru connection manager. 
Requires `Ásbrú Connection Manager` https://www.asbru-cm.net.

- [❓ What is ULauncher](https://ulauncher.io/)

Installation
--------------

Open Ulauncher settings, go to extensions tab and add this
extension from URL:
```
https://github.com/robinsongina/ulauncher_asbru_cm
```

Run in debug mode:
--------------------

```bash
export VERBOSE=1
export ULAUNCHER_WS_API=ws://127.0.0.1:5054/com.github.robinsongina.ulauncher_asbru_cm
export PYTHONPATH=$HOME/projects/ulauncher-asbru 
/usr/bin/python3 main.py
```
