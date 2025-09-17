# ~/.config/fish/config.fish

function fish_prompt
    set_color red
    echo -n "@"
    set_color yellow
    echo -n (hostname)
    set_color cyan
    echo -n " "(prompt_pwd)" "
    set_color green
    echo -n "→"
    set_color normal
    echo -n " "
end

string match -q "$TERM_PROGRAM" "kiro" and . (kiro --locate-shell-integration-path fish)
