#!/bin/bash

# サンプルで使うライブラリのインポート
pip3 install matplotlib
pip3 install networkx

rm -rf wheel
# NativeAPI用whlファイルのGET（Linux用）
wget -P wheel https://github.com/intersystems/quickstarts-python/raw/master/Solutions/nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl
pip3 install wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl

# networkxの日本語表示に使いたいフォントインストール
sudo apt-get update
sudo sudo apt install fontconfig
sudo apt-get install -y fonts-ipaexfont