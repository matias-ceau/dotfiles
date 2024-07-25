# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /opt/miniforge3/bin/conda
    eval /opt/miniforge3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/opt/miniforge3/etc/fish/conf.d/conda.fish"
        . "/opt/miniforge3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/opt/miniforge3/bin" $PATH
    end
end
# <<< conda initialize <<<
