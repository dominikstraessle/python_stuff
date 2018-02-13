#!/bin/bash
#: Title : PIP over Proxy
#: Date : 2018-02-13
#: Author : Dominik Strässle
#: Version : 1.0
#: Description : Use PIP behind a Proxy
#: Options : None
#: Prerequisites : Replace "module", https- and http proxy server (remove the ")
#: Warning : 

export http_proxy="http://user:pwd@server:port"
export https_proxy="https://user:pwd@server:port"
pip install --index-url=https://pypi.python.org/simple/ --trusted-host pypi.python.org "module"
