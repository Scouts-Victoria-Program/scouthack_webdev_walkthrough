#!/usr/bin/env bash
for commit in $(git log --format=%H --reverse main);
do
    git checkout "$commit";
    read _;
done
