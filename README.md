
ulauncher-asbru_cm
=================

Asbru Connection Manager connect plugin for ULauncher.

This plugin can enable or disable NetworkManager connections from
ULauncher panel. Requires `ásbrú connection manager` .

- [❓ What is ULauncher](https://ulauncher.io/)
- [💓 Donate](https://melianmiko.ru/donate)

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
export ULAUNCHER_WS_API=ws://127.0.0.1:5054/com.github.melianmiko.ulauncher-nmcli
export PYTHONPATH=$HOME/Projects/Ulauncher 
/usr/bin/python3 main.py
```
