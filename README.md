# nurgapy

```bash  _   _                       ____
 | \ | |_   _ _ __ __ _  __ _|  _ \ _   _
 |  \| | | | | '__/ _` |/ _` | |_) | | | |
 | |\  | |_| | | | (_| | (_| |  __/| |_| |
 |_| \_|\__,_|_|  \__, |\__,_|_|    \__, |
                  |___/             |___/
```

Small convenience Python library.

Rationally to build this library, that I don't want copy over this code to multiple projects.

Currently, `nurgapy` library consists two functions:
- `tyme` - it is a small wrapper function, which is used for measuring execution time of functions. Also works for the class functions.
- `trackbar` - it is a simple progress bar, which just works without many imports. Inspired by [stackoverflow post](https://stackoverflow.com/a/34482761/15059130). There is well-known `tqdm` library, but it prevents user from using `print` statements. For simple use-cases this progress bar should be enough. There is another nice library `alive-progress`, which does not have this issue and many others. But I just wanted to have some simple progress bar, which lives in the single library with other convenience functions.

## Roadmap
- ~~Add basic code~~
~~- Add pre-commit hook~~
    - Add more rules to pre-commit
~~- Add public API to the `init.py`~~
- Add tests
- Add badges
- Add packaging
- Publish to pip

Progress bar
- Add percentages
- Flexible size
- Progress bar runs in the independent thread
