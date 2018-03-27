#!/bin/bash
#: Title : PIP over Proxy
#: Date : 2018-02-13
#: Author : Dominik Strässle
#: Version : 1.0
#: Description : Use PIP behind a Proxy
#: Parameters : 1. http_proxy
#: Parameters : 2. https_proxy
#: Parameters : 3. module name
#: Example : sh pip_over_proxy.sh http://user:pwd@server:port https://user:pwd@server:port flask
#: Example : sh pip_over_proxy.sh "" https://user:pwd@server:port flask

if [[ -n $3 ]]; then
  echo "pip will start now"
  export http_proxy=$1
  export https_proxy=$2
  pip install --index-url=https://pypi.python.org/simple/ --trusted-host pypi.python.org $3
  export http_proxy=
  export https_proxy=
  echo "pip finished"
else
  echo "argument error: modulname missing"
fi

#: Alternative in %appdata%/pip/pip.ini:
#: https://stackoverflow.com/questions/9698557/how-to-use-pip-on-windows-behind-an-authenticating-proxy/37219624#37219624
