#!/usr/bin/env bash

rm frankenfish.zip
pdm run main || exit 1
if [ "$INSTALL_DIR" ]; then
    cp frankenfish.zip "$INSTALL_DIR"
fi