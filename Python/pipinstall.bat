@echo off
rm -rf wheel

bitsadmin /transfer myDownloadJob /download /priority normal https://github.com/intersystems/quickstarts-python/raw/master/Solutions/nativeAPI_wheel/irisnative-1.0.0-cp34.cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl %CD%/wheel/irisnative-1.0.0-cp34.cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl
pip install wheel/irisnative-1.0.0-cp34.cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl

pip install matplotlib
pip install networkx