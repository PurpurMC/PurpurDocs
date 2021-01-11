# PurpurDocs

This is the documentation for Purpur that uses [Mkdocs](https://github.com/mkdocs/mkdocs) to generate a static site hosted on https://purpur.pl3x.net/docs

## Setup

#### Requirements

1. You must have `mkdocs` version 1.1.2 or greater installed on your system. Follow the installation guide here: https://www.mkdocs.org/#installation. I personally recommend installing it through python's package manager `pip`. 
```sh
$ pip install mkdocs
```

2. You must have `mkdocs-material` version 6.2.3 or greater installed on your system. Follow the installation guide here: https://squidfunk.github.io/mkdocs-material/getting-started/#installation. `pip` is required to install the mkdocs theme.
```sh
$ pip install mkdocs-material
```

3. You must have `mkdocs-material-extensions` version 1.0.1 or greater installed on your system. Follow the installation guide here: https://squidfunk.github.io/mkdocs-material/getting-started/#installation. `pip` is required to install the mkdocs theme extension.
```sh
$ pip install mkdocs-material-extensions
```

#### Preview changes

To preview your changes to the documentation, run `mkdocs serve`. This will start a dev-server that will preview the documentation and auto reload as you make changes. More info is shown here: https://www.mkdocs.org/#getting-started
```sh
$ git clone https://github.com/pl3xgaming/PurpurDocs.git
$ cd PurpurDocs
$ mkdocs serve
```