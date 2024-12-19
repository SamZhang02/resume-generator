from ...models.contact import ContactItem
from ...models.education import EducationItem
from ...models.experience import ExperienceItem
from ...models.project import ProjectItem
from ...models.skill import SkillsItem
from ...models.resume import Resume

from ..renderer import Renderer


class JakeResumeRenderer(Renderer):
    header = r"""
\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------

\begin{document}"""
    footer = r"\end{document}"

    def __init__(self, out_path):
        super().__init__(out_path)

    def _render_contact(self, contact: ContactItem):
        if not contact.link:
            return contact.text

        return rf"\href{{{contact.link}}}{{\underline{{{contact.text}}}}}"

    def _render_title(self, name: str, contacts: list[ContactItem]):

        return rf"""\begin{{center}}
            \textbf{{\Huge \scshape {name}}} \\ \vspace{{1pt}}
            \small {" $|$ \n".join([self._render_contact(contact) for contact in contacts])}
        \end{{center}}"""

    def _render_experience(self, experience: ExperienceItem):
        company_link = (
            f"{{{experience.company}}}"
            if not experience.link
            else rf"\href{{{experience.link}}}{{{experience.company}}}"
        )

        return fr"""\resumeSubheading
          {{{experience.title}}}{{{experience.date}}}
          {{{company_link}}}{{{experience.location}}}
          \resumeItemListStart
            {"\n".join(f"\\resumeItem{{{bulletpoint}}}" for bulletpoint in experience.bulletpoints)}
          \resumeItemListEnd"""

    def _render_experiences(self, experiences: list[ExperienceItem]):
        if not experiences:
            return ""

        rendered = [self._render_experience(exp) for exp in experiences]

        return fr"""\section{{Experience}}
          \resumeSubHeadingListStart
          {"\n".join(rendered)}
          \resumeSubHeadingListEnd"""

    def _render_education(self, education: EducationItem):
        education_link = (
            f"{{{education.institution}}}"
            if not education.link
            else rf"\href{{{education.link}}}{{{education.institution}}}"
        )

        return rf"""\resumeSubheading
              {{{education_link}}}{{{education.location}}}
              {{{education.degree}}}{{{education.date}}}"""

    def _render_educations(self, educations: list[EducationItem]):
        if not educations:
            return ""

        rendered = [self._render_education(education) for education in educations]

        return fr"""\section{{Education}}
          \resumeSubHeadingListStart
          {"\n".join(rendered)}
          \resumeSubHeadingListEnd"""

    def _render_project(self, project: ProjectItem):
        project_link = (
            f"{{{project.name}}}"
            if not project.link
            else rf"\href{{{project.link}}}{{{project.name}}}"
        )

        return fr"""\resumeProjectHeading
          {{\textbf{{{project_link}}} $|$ \emph{{{", ".join(project.technologies)}}}}}{{{project.date}}}
          \resumeItemListStart
            {"\n".join(f"\\resumeItem{{{bulletpoint}}}" for bulletpoint in project.bulletpoints)}
          \resumeItemListEnd"""

    def _render_projects(self, projects: list[ProjectItem]):
        if not projects:
            return ""

        rendered = [self._render_project(project) for project in projects]

        return fr"""\section{{Projects}}
            \resumeSubHeadingListStart
              {"\n".join(rendered)}
            \resumeSubHeadingListEnd"""

    def _render_skill(self, skill: SkillsItem):
        return rf"\textbf{{{skill.category}}}{{: {", ".join(skill.items)}}} \\"

    def _render_skills(self, skills: list[SkillsItem]):
        if not skills:
            return ""

        rendered = [self._render_skill(skill) for skill in skills]

        return fr"""\section{{Technical Skills}}
         \begin{{itemize}}[leftmargin=0.15in, label={{}}]
            \small{{\item{{
              {"\n".join(rendered)}
            }}}}
         \end{{itemize}}"""

    def render_document(self, resume: Resume):
        document = rf"""
                {self.header}

                {self._render_title(resume.name, resume.contacts)}

                {self._render_educations(resume.educations)}

                {self._render_experiences(resume.experiences)}

                {self._render_projects(resume.projects)}

                {self._render_skills(resume.skills)}

                {self.footer}
        """

        with open(self.out_path, "w") as fobj:
            fobj.write(document)
