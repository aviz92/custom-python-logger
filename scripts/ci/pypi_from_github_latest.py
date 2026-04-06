import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/user/aviz/"
PYPI_JSON = "https://pypi.org/pypi/{}/json"


def get_latest_version(package: str) -> str:
    session = requests.Session()
    session.headers.update({"User-Agent": "uv-upgrade-script"})
    resp = session.get(PYPI_JSON.format(package))
    resp.raise_for_status()
    return resp.json()["info"]["version"]


def get_all_pypi_projects_latest_versions() -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    projects_res = soup.find_all("h3", class_="package-snippet__title")

    projects = {}
    for _, project in enumerate(projects_res, 1):
        if "Archived" not in project.text and "python-test-aviz" not in project.text:
            _project_name = project.text.strip()
            projects[_project_name] = get_latest_version(_project_name)
    return projects


def build_uv_command(projects: dict) -> str:
    command = "uv add "
    for project, latest_version in projects.items():
        command += f"{project}=={latest_version} "
    return command.strip()


def main() -> None:
    projects = get_all_pypi_projects_latest_versions()
    for project, latest_version in projects.items():
        print(f"{project}=={latest_version}")
        # print(f'"{project}=={latest_version}",')

    uv_cmd = build_uv_command(projects)
    print(uv_cmd)
    print()


if __name__ == "__main__":
    main()
