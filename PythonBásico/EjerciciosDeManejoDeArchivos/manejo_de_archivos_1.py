# =============================================================================
#  1. READ, CLEAN AND SORT THE CONTENT
# =============================================================================
def read_and_sort_content(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        list_content = file.readlines()

    clear_content = []
    for line in list_content:
        clear_content.append(line.strip())

    return sorted(clear_content)

# =============================================================================
#  2. SAVE THE SORTED RESULTS
# =============================================================================
def save_sorted_result(file_name, content_list):
    with open(file_name, "w", encoding="utf-8") as file:
        for item in content_list:
            file.write(item + "\n")
    print(f"File '{file_name}' created successfully.")

# =============================================================================
#  3. MAIN EXECUTION FLOW
# =============================================================================
def main():
    output_file = "sorted_songs.txt"

    sorted_songs = read_and_sort_content("random.txt")
    save_sorted_result(output_file, sorted_songs)
    
if __name__ == "__main__":
    main()
