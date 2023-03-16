# y2p  
Convert yaml file to dotted notation, object style.  
Used to convert java profile configuration from yaml to the more readable properties format.  

ex:
my:
  yaml:
    file: hello

my.yaml.file=hello

## install

```
pip install git+https://github.com/pylanglois/yaml2prop
```

## usage
```
y2p --help-all

convert yaml to dot notation

Utilisation:
    y2p [OPTIONS] [SOUS_COMMANDE [OPTIONS]] 

Meta-options:
    -h, --help         Imprime ce message d'aide et sort
    --help-all         Prints help messages of all sub-commands and quits
    -v, --version      Imprime la version du programme et sort

Options:
    --show-params      Show parameters given to y2p and exit.

Sub-commands:
    file               voir 'y2p file --help' pour plus d'information
    string             voir 'y2p string --help' pour plus d'information

Utilisation:
    y2p file [OPTIONS] files...

Hidden-switches:
    -h, --help         Imprime ce message d'aide et sort
    --help-all         Prints help messages of all sub-commands and quits
    -v, --version      Imprime la version du programme et sort


Utilisation:
    y2p string [OPTIONS] yaml_strs...

Hidden-switches:
    -h, --help         Imprime ce message d'aide et sort
    --help-all         Prints help messages of all sub-commands and quits
    -v, --version      Imprime la version du programme et sort

Options:
    -s, --stdin        Use stdin as source

```

## file
```
y2p file ~/blabla/application.yml
```

## string
```
y2p string "my:
  yaml:
    file: hello"
```
## stdin
```
cat  ~/blabla/application.yml | y2p string --stdin
```