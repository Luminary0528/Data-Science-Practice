# update_readme.py
import nbformat
import os

notebooks_dir = "."
readme_path = "README.md"

all_markdown = []

# Loop through all notebooks in the folder
for nb_file in sorted(os.listdir(notebooks_dir)):
    if nb_file.endswith(".ipynb"):
        nb_path = os.path.join(notebooks_dir, nb_file)
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        markdown_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'markdown']
        if markdown_cells:
            all_markdown.append(f"# Notebook: {nb_file}\n\n")
            all_markdown.append("\n\n".join(markdown_cells))
            all_markdown.append("\n\n---\n\n")

# Write combined markdown to README
with open(readme_path, "w", encoding="utf-8") as f:
    f.write("\n".join(all_markdown))

print("README.md updated from all notebooks!")

