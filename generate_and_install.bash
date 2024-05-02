#!/usr/bin/env bash

rm frankenfish-1.19.2.zip
rm frankenfish-1.20.1.zip

pdm run main 1.19.2 || exit 1
if [[ -d $FRANKENFISH_INSTALL_DIR_1_19_2 ]]; then
    cp frankenfish-1.19.2.zip "$FRANKENFISH_INSTALL_DIR_1_19_2"
fi

pdm run main 1.20.1 || exit 1
if [[ -d $FRANKENFISH_INSTALL_DIR_1_20_1 ]]; then
    cp frankenfish-1.20.1.zip "$FRANKENFISH_INSTALL_DIR_1_20_1"
fi