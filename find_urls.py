import os

def find_url_references(directory, search_term):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_term in content:
                        line_number = 1
                        for line in content.split('\n'):
                            if search_term in line:
                                results.append(f"{file_path}:{line_number} - {line.strip()}")
                            line_number += 1
    return results

if __name__ == "__main__":
    templates_dir = "c:\\Users\\Team\\Desktop\\animal-\\home\\templates"
    search_term = "scholars_aerial"
    
    results = find_url_references(templates_dir, search_term)
    if results:
        print(f"Found {len(results)} references to '{search_term}':")
        for result in results:
            print(result)
    else:
        print(f"No references to '{search_term}' found.")