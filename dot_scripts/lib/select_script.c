#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define CACHE_FILE_REL "/.cache/script_info.csv"
#define SCRIPT_FOLDER_REL "/.scripts/"

typedef struct {
    char file[256];
    char descr[256];
} ScriptInfo;

void load_cache(ScriptInfo **infos, int *count, const char *cache_file) {
    FILE *file = fopen(cache_file, "r");
    if (!file) {
        perror("Error opening cache file");
        return;
    }

    char line[512];
    *count = 0;
    ScriptInfo *temp_infos = NULL;

    // Skip the header line
    fgets(line, sizeof(line), file);

    while (fgets(line, sizeof(line), file)) {
        temp_infos = realloc(temp_infos, sizeof(ScriptInfo) * (*count + 1));
        sscanf(line, "%[^,],%*[^,],%*[^,],%*[^,],%*[^,],%*[^,],\"%255[^\"]\"", 
               temp_infos[*count].file, temp_infos[*count].descr);
        (*count)++;
    }

    fclose(file);
    *infos = temp_infos;
}

void free_cache(ScriptInfo *infos) {
    free(infos);
}

void display_rofi(ScriptInfo *infos, int count) {
    FILE *rofi = popen("rofi -dmenu -markup-rows -i -lines 30 -width 80", "w");
    if (!rofi) {
        perror("Error opening rofi");
        return;
    }

    for (int i = 0; i < count; i++) {
        fprintf(rofi, "<span color='green'>%s</span> \u27F6 %s\n", infos[i].file, infos[i].descr);
    }

    pclose(rofi);
}

void extract_choice(ScriptInfo *infos, int count, char *choice) {
    FILE *rofi = popen("rofi -dmenu -markup-rows -i -lines 30 -width 80", "r");
    if (!rofi) {
        perror("Error opening rofi");
        return;
    }

    char line[512];
    if (fgets(line, sizeof(line), rofi)) {
        sscanf(line, "<span color='green'>%255[^<]</span>", choice);
    }

    pclose(rofi);
}

void execute_choice(const char *choice, const char *script_folder) {
    if (strlen(choice) > 0) {
        char filepath[512];
        snprintf(filepath, sizeof(filepath), "%s/%s", script_folder, choice);
        execl(filepath, filepath, NULL);
    }
}

int main() {
    const char *home = getenv("HOME");
    if (!home) {
        fprintf(stderr, "HOME environment variable not set\n");
        return 1;
    }

    char cache_file[512];
    snprintf(cache_file, sizeof(cache_file), "%s%s", home, CACHE_FILE_REL);

    char script_folder[512];
    snprintf(script_folder, sizeof(script_folder), "%s%s", home, SCRIPT_FOLDER_REL);

    ScriptInfo *infos;
    int count;
    char choice[256] = "";

    load_cache(&infos, &count, cache_file);
    display_rofi(infos, count);
    extract_choice(infos, count, choice);
    free_cache(infos);

    execute_choice(choice, script_folder);

    return 0;
}
