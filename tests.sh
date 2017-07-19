#!/bin/sh
coverage erase
tox
coverage combine
coverage report -m
coverage xml -i
coverage html -i