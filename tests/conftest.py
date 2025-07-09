import json

from pytest import fixture


@fixture()
def target_all_contributors_rc():
    return """
{
  "files": ["README.md"],
  "imageSize": 100,
  "contributorsPerLine": 7,
  "badgeTemplate": "[![All Contributors](https://img.shields.io/badge/all_contributors-<%= contributors.length %>-orange.svg)](#contributors)",
  "skipCi": false,
  "contributorsSortAlphabetically": true,
  "contributors": [
    {
      "login": "harrylime",
      "name": "Harry Lime",
      "avatar_url": "example.com/example.png",
      "profile": "example.com",
      "contributions": [
        "doc",
        "ideas",
        "question",
        "talk"
      ]
    },
    {
      "login": "samspade",
      "name": "Sam Spade",
      "avatar_url": "example.com/example.png",
      "profile": "example.com",
      "contributions": [
        "infra",
        "doc"
      ]
    }
  ],
  "projectName": "my-project",
  "projectOwner": "my-org",
  "repoType": "github",
  "repoHost": "https://github.com",
  "commitConvention": "none",
  "commitType": "docs"
}
"""


@fixture()
def target_all_contributors_rc_object(target_all_contributors_rc):
    return json.loads(target_all_contributors_rc)


@fixture()
def target_all_contributors_rc_file(tmp_path, target_all_contributors_rc):
    file = tmp_path / ".all_contributors.rc"
    with open(file, "w") as outfile:
        outfile.write(target_all_contributors_rc)
    return file


@fixture()
def contributor_1():
    return {
        "login": "user1",
        "name": "User One",
        "avatar_url": "https://github.com/user1.png",
        "profile": "https://github.com/user1",
        "contributions": ["doc", "infra"],
    }


@fixture()
def contributor_1_duplicate():
    return {
        "login": "user1",
        "name": "User One",
        "avatar_url": "https://github.com/user1.png",
        "profile": "https://github.com/user1",
        "contributions": ["design", "doc", "code"],
    }


@fixture()
def contributor_1_merged():
    return {
        "login": "user1",
        "name": "User One",
        "avatar_url": "https://github.com/user1.png",
        "profile": "https://github.com/user1",
        "contributions": ["design", "code", "doc", "infra"],
    }


@fixture()
def contributor_2():
    return {
        "login": "user2",
        "name": "User Two",
        "avatar_url": "https://github.com/user2.png",
        "profile": "https://github.com/user2",
        "contributions": ["code", "doc"],
    }
