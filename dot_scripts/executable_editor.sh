#! /bin/sh

#DOC#@CLI@ "Edit any file in current folder or subfolders (recursively)"

vim "$( find 2>/dev/null | fzf )"
