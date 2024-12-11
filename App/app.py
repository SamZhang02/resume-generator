import argparse
from pathlib import Path
from re import fullmatch

from App.rendering import renderer

from .cli.cli import CLI
from .parsing.parser import Parser
from .rendering.templates.jake_resume import JakeResumeRenderer


def parse_args():
    parser = argparse.ArgumentParser(
        description="CLI Tool for Resume Customization. Parses input JSON and allows customization of resume sections."
    )

    # Required Arguments
    parser.add_argument(
        "--data_path",
        type=Path,
        required=True,
        help="Path to the input JSON file containing resume data.",
    )
    parser.add_argument(
        "--out_path", type=Path, required=True, help="Path to save the output file."
    )

    # Optional Arguments
    parser.add_argument(
        "--to_pdf", action="store_true", help="Compile the resume into PDF as well."
    )
    parser.add_argument(
        "--format_tex",
        action="store_true",
        help="Format the generated tex file (requires latexindent).",
    )

    # parser.add_argument(
    #     "--template",
    #     type=str,
    #     default="jake_resume",
    #     help="Specify the template style to use for rendering (e.g., 'modern', 'classic')."
    # )

    return parser.parse_args()


def main():
    args = parse_args()

    parser = Parser(args.data_path)
    full_resume = parser.parse()

    if not full_resume:
        raise ValueError("Could ot parse full resume")

    cli = CLI(full_resume)
    cli.start()
    custom_resume = cli.custom_resume

    if not custom_resume:
        raise ValueError("Did not receive a resume to render")

    renderer = JakeResumeRenderer(args.out_path)
    renderer.render_document(custom_resume)

    print(args)


if __name__ == "__main__":
    main()
