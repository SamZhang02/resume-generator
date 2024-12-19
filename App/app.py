import argparse
from pathlib import Path
from typing import NamedTuple

from .rendering.renderer import Renderer
from .cli.cli import CLI
from .parsing.parser import Parser
from .rendering.templates.jake_resume import JakeResumeRenderer
from .tools.latex_indent import format_tex


class Args(NamedTuple):
    data_path: Path
    out_path: Path
    format_tex: bool


def parse_args():
    parser = argparse.ArgumentParser(
        description="CLI Tool for Resume Customization. Parses input JSON and allows customization of resume sections."
    )

    _ = parser.add_argument(
        "--data_path",
        type=Path,
        required=True,
        help="Path to the input JSON file containing resume data.",
    )
    _ = parser.add_argument(
        "--out_path", type=Path, required=True, help="Path to save the output file."
    )

    _ = parser.add_argument(
        "--format_tex",
        action="store_true",
        help="Format the generated tex file (requires latexindent).",
    )

    args = parser.parse_args()
    args_dict = vars(args)

    return Args(args_dict["data_path"], args_dict["out_path"], args_dict["format_tex"])


def main():
    args: Args = parse_args()

    resume_parser = Parser(args.data_path)
    full_resume = resume_parser.parse()

    if not full_resume:
        raise ValueError("Could ot parse full resume")

    cli = CLI(full_resume)
    cli.start()
    custom_resume = cli.custom_resume

    if not custom_resume:
        raise ValueError("Did not receive a resume to render")

    renderer: Renderer = JakeResumeRenderer(args.out_path)
    renderer.render_document(custom_resume)

    print(f"Resume tex file written to {renderer.out_path}.")

    if args.format_tex:
        format_tex(renderer.out_path)


if __name__ == "__main__":
    main()
