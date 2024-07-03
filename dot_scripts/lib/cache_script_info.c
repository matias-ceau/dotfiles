//#DOC#=2024-06=@OTH@ "SC of C script that extracts the metadata of non-binary scripts and outputs a CSV"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>

#define SCRIPT_FOLDER_REL "/.scripts/"
#define CACHE_FILE_REL "/.scripts/data/script_info.csv"

typedef struct {
    char file[256];
    char type[10];
    char status[20];
    char host[50];
    char date[10];
    char tag[50];
    char descr[256];
} ScriptInfo;

void extract_info(const char *path, ScriptInfo *info) {
    FILE *file = fopen(path, "r");
    if (!file) {
        perror("Error opening file");
        return;
    }

    strcpy(info->file, path);
    strcpy(info->type, "OTH");
    strcpy(info->status, "active");
    strcpy(info->host, "all");
    strcpy(info->tag, "");
    strcpy(info->descr, "");

    char line[512];
    for (int i = 0; i < 3; i++) {
        if (fgets(line, sizeof(line), file) == NULL) {
            break;
        }
    }
    fclose(file);

    if (strncmp(line, "#DOC#", 5) != 0) {
        return;
    }

    char *metadata = strtok(line, "\"");
    char *description = strtok(NULL, "\"");

    if (description) {
        strcpy(info->descr, description);
    }

    if (strstr(metadata, "@CLI@")) strcpy(info->type, "CLI");
    if (strstr(metadata, "@RUN@")) strcpy(info->type, "RUN");
    if (strstr(metadata, "$deprecated$")) strcpy(info->status, "deprecated");
    if (strstr(metadata, "$in_progress$")) strcpy(info->status, "in_progress");
    
    char *host_start = strstr(metadata, "~");
    if (host_start) {
        sscanf(host_start, "~%[^~]~", info->host);
    }
    
    char *date_start = strstr(metadata, "=");
    if (date_start) {
        sscanf(date_start, "=%[^=]=", info->date);
    } else {
        struct stat attr;
        if (stat(path, &attr) == 0) {
            struct tm *tm = localtime(&attr.st_ctime);
            strftime(info->date, sizeof(info->date), "%Y-%m", tm);
        } else {
            strcpy(info->date, "2000-01");
        }
    }

    char *tag_start = strstr(metadata, "+");
    if (tag_start) {
        sscanf(tag_start, "+%[^+]+", info->tag);
    }
}

void update_cache(const char *script_folder, const char *cache_file) {
    DIR *dir = opendir(script_folder);
    if (!dir) {
        perror("Error opening script directory");
        return;
    }

    FILE *cache = fopen(cache_file, "w");
    if (!cache) {
        perror("Error opening cache file");
        closedir(dir);
        return;
    }

    fprintf(cache, "file,type,status,host,date,tag,description\n");

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_REG) {
            char filepath[512];
            snprintf(filepath, sizeof(filepath), "%s/%s", script_folder, entry->d_name);

            ScriptInfo info;
            extract_info(filepath, &info);
            if (strlen(info.descr) > 0) {
                // Use only the filename, not the full path
                fprintf(cache, "%s,%s,%s,%s,%s,%s,\"%s\"\n",
                        entry->d_name, info.type, info.status, info.host, info.date, info.tag, info.descr);
            }
        }
    }

    closedir(dir);
    fclose(cache);
}

int main() {
    const char *home = getenv("HOME");
    if (!home) {
        fprintf(stderr, "HOME environment variable not set\n");
        return 1;
    }

    char script_folder[512];
    snprintf(script_folder, sizeof(script_folder), "%s%s", home, SCRIPT_FOLDER_REL);

    char cache_file[512];
    snprintf(cache_file, sizeof(cache_file), "%s%s", home, CACHE_FILE_REL);

    // Ensure the data directory exists
    char data_dir[512];
    snprintf(data_dir, sizeof(data_dir), "%s/.scripts/data", home);
    mkdir(data_dir, 0777);

    update_cache(script_folder, cache_file);

    return 0;
}
