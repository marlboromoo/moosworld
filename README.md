# Moo's World
Source for Moo's world offical website, a tiny minecraft server in Taiwan.

## Requirments
 - Python
 - [Pelican] []

## Build
You need [pelican] [] to build the website from source.

### Install Dependency
```sh
sudo apt-get install python python-dev python-pip build-essential
sudo pip install pelican markdown
```
### Build the site
```sh
cd ~
git clone https://github.com/marlboromoo/moosworld.git
cd moosworld
git submodule init
git submodule update
make clean
make html
```
## Author
Timothy.Lee a.k.a MarlboroMoo.

## License
The following directories and their contents are [CC-BY-NC-SA] [] license.

 * content/articles/
 * content/pages/

  [CC-BY-NC-SA]: http://creativecommons.org/licenses/by-nc-sa/4.0/
  [pelican]: http://docs.getpelican.com/ "Pelican"

