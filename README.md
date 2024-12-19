# Resume Generator

This tool simplifies the process of tailoring your resume for specific job applications. By maintaining a JSON file containing your past job and project experiences, the tool can generate a `.tex` file in the format of [Jake's Resume](https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs). This allows for quick and easy resume customization.

[![asciicast](https://asciinema.org/a/Cfp7G8oBJNkeIlyg1FBQKyvMK.svg)](https://asciinema.org/a/Cfp7G8oBJNkeIlyg1FBQKyvMK)

## Features
- Generate `.tex` resumes from a standard JSON file of all your skills and experiences.
- Easily customizable via the CLI for different job applications.

## Requirements
- Python3
- [latexindent](https://github.com/cmhughes/latexindent.pl) (Optional)

## How to Use
1. Prepare a JSON file containing your job and project experiences following the structure in `doc/example.json`. Ensure the structure aligns with the format expected by the tool.
3. Run the tool to generate a `.tex` file.

 ```shell
 command
 ```
   
3. Compile the `.tex` file using your LaTeX compiler to create a PDF resume.

## Support for different resume formats 
Currently, the codebase supports only Jake's Resume format, but it functions as a mini template engine. In the directories, `App/templates/renderer/templates` is reserved for different renderers to handle different resume templates. To create a new format:
1. Add your custom template to `App/templates/renderer/templates`, using `jake_resume.py` as an example.
2. Update the template reference in `App/app.py` to use your new format.

## Licence 
This project is under GNU General Public License v3.0. 
