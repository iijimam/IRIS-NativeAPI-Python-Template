#!/bin/bash

pip3 install matplotlib
pip3 install networkx

rm -rf wheel

wget -P wheel https://github.com/intersystems/quickstarts-python/raw/master/Solutions/nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl
pip3 install wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl

# 日本語フォントのインストール（Takaoフォントを利用しています）
#sudo apt-get update
#sudo sudo apt install fontconfig
#sudo apt-get install -y fonts-ipaexfont

# fontList.cache を削除
rm ${PWD}/.cache/matplotlib/fontList.cache