#!/bin/bash

# サンプルで使うライブラリのインポート
pip3 matplotlib
pip3 networkx

rm -rf wheel
# NativeAPI用whlファイルのGET（Linux用）
wget -P wheel https://github.com/intersystems/quickstarts-python/raw/master/Solutions/nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl
pip3 install wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl
