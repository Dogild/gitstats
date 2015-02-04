bodies = {}

bodies["https://api.github.com/users/little-dude?per_page=100"] = '{"login":"little-dude",\
                                                                    "id":6646324,\
                                                                    "avatar_url":"https://avatars.githubusercontent.com/u/6646324?v=3",\
                                                                    "gravatar_id":"",\
                                                                    "url":"https://api.github.com/users/little-dude",\
                                                                    "html_url":"https://github.com/little-dude",\
                                                                    "followers_url":"https://api.github.com/users/little-dude/followers",\
                                                                    "following_url":"https://api.github.com/users/little-dude/following{/other_user}",\
                                                                    "gists_url":"https://api.github.com/users/little-dude/gists{/gist_id}",\
                                                                    "starred_url":"https://api.github.com/users/little-dude/starred{/owner}{/repo}",\
                                                                    "subscriptions_url":"https://api.github.com/users/little-dude/subscriptions",\
                                                                    "organizations_url":"https://api.github.com/users/little-dude/orgs",\
                                                                    "repos_url":"https://api.github.com/users/little-dude/repos",\
                                                                    "events_url":"https://api.github.com/users/little-dude/events{/privacy}",\
                                                                    "received_events_url":"https://api.github.com/users/little-dude/received_events",\
                                                                    "type":"User",\
                                                                    "site_admin":false,\
                                                                    "name":"",\
                                                                    "company":"",\
                                                                    "blog":"",\
                                                                    "location":"",\
                                                                    "email":"",\
                                                                    "hireable":false,\
                                                                    "bio":null,\
                                                                    "public_repos":16,\
                                                                    "public_gists":1,\
                                                                    "followers":1,\
                                                                    "following":3,\
                                                                    "created_at":"2014-02-11T04:07:08Z",\
                                                                    "updated_at":"2015-01-29T18:03:47Z"}'

bodies["https://api.github.com/users/Dogil?per_page=100"] = '{"message": "Not Found",\
                                                 "documentation_url": "https://developer.github.com/v3"}'

bodies["https://api.github.com/users/little-dude/orgs?per_page=100"] = '[{"login":"cappuccino",\
                                                                          "id":16595,\
                                                                          "url":"https://api.github.com/orgs/cappuccino",\
                                                                          "repos_url":"https://api.github.com/orgs/cappuccino/repos",\
                                                                          "events_url":"https://api.github.com/orgs/cappuccino/events",\
                                                                          "members_url":"https://api.github.com/orgs/cappuccino/members{/member}",\
                                                                          "public_members_url":"https://api.github.com/orgs/cappuccino/public_members{/member}",\
                                                                          "avatar_url":"https://avatars.githubusercontent.com/u/16595?v=3",\
                                                                          "description":null},\
                                                                          {"login":"ArchipelProject",\
                                                                          "id":1847921,"url":"https://api.github.com/orgs/ArchipelProject",\
                                                                          "repos_url":"https://api.github.com/orgs/ArchipelProject/repos",\
                                                                          "events_url":"https://api.github.com/orgs/ArchipelProject/events",\
                                                                          "members_url":"https://api.github.com/orgs/ArchipelProject/members{/member}",\
                                                                          "public_members_url":"https://api.github.com/orgs/ArchipelProject/public_members{/member}",\
                                                                          "avatar_url":"https://avatars.githubusercontent.com/u/1847921?v=3",\
                                                                          "description":""}]'

bodies["https://api.github.com/users/Dogild/orgs?per_page=100"] = '[]'

bodies["https://api.github.com/orgs/cappuccino/repos?per_page=100"] = '[{"id": 49107,\
                                                                         "name": "cappuccino",\
                                                                         "full_name": "cappuccino/cappuccino",\
                                                                         "owner": {\
                                                                         "login": "cappuccino",\
                                                                         "id": 16595,\
                                                                         "avatar_url": "https://avatars.githubusercontent.com/u/16595?v=3",\
                                                                         "gravatar_id": "",\
                                                                         "url": "https://api.github.com/users/cappuccino",\
                                                                         "html_url": "https://github.com/cappuccino",\
                                                                         "followers_url": "https://api.github.com/users/cappuccino/followers",\
                                                                         "following_url": "https://api.github.com/users/cappuccino/following{/other_user}",\
                                                                         "gists_url": "https://api.github.com/users/cappuccino/gists{/gist_id}",\
                                                                         "starred_url": "https://api.github.com/users/cappuccino/starred{/owner}{/repo}",\
                                                                         "subscriptions_url": "https://api.github.com/users/cappuccino/subscriptions",\
                                                                         "organizations_url": "https://api.github.com/users/cappuccino/orgs",\
                                                                         "repos_url": "https://api.github.com/users/cappuccino/repos",\
                                                                         "events_url": "https://api.github.com/users/cappuccino/events{/privacy}",\
                                                                         "received_events_url": "https://api.github.com/users/cappuccino/received_events",\
                                                                         "type": "Organization",\
                                                                         "site_admin": false\
                                                                         },\
                                                                         "private": false,\
                                                                         "html_url": "https://github.com/cappuccino/cappuccino",\
                                                                         "description": "Web Application Framework in JavaScript and Objective-J",\
                                                                         "fork": false,\
                                                                         "url": "https://api.github.com/repos/cappuccino/cappuccino",\
                                                                         "forks_url": "https://api.github.com/repos/cappuccino/cappuccino/forks",\
                                                                         "keys_url": "https://api.github.com/repos/cappuccino/cappuccino/keys{/key_id}",\
                                                                         "collaborators_url": "https://api.github.com/repos/cappuccino/cappuccino/collaborators{/collaborator}",\
                                                                         "teams_url": "https://api.github.com/repos/cappuccino/cappuccino/teams",\
                                                                         "hooks_url": "https://api.github.com/repos/cappuccino/cappuccino/hooks",\
                                                                         "issue_events_url": "https://api.github.com/repos/cappuccino/cappuccino/issues/events{/number}",\
                                                                         "events_url": "https://api.github.com/repos/cappuccino/cappuccino/events",\
                                                                         "assignees_url": "https://api.github.com/repos/cappuccino/cappuccino/assignees{/user}",\
                                                                         "branches_url": "https://api.github.com/repos/cappuccino/cappuccino/branches{/branch}",\
                                                                         "tags_url": "https://api.github.com/repos/cappuccino/cappuccino/tags",\
                                                                         "blobs_url": "https://api.github.com/repos/cappuccino/cappuccino/git/blobs{/sha}",\
                                                                         "git_tags_url": "https://api.github.com/repos/cappuccino/cappuccino/git/tags{/sha}",\
                                                                         "git_refs_url": "https://api.github.com/repos/cappuccino/cappuccino/git/refs{/sha}",\
                                                                         "trees_url": "https://api.github.com/repos/cappuccino/cappuccino/git/trees{/sha}",\
                                                                         "statuses_url": "https://api.github.com/repos/cappuccino/cappuccino/statuses/{sha}",\
                                                                         "languages_url": "https://api.github.com/repos/cappuccino/cappuccino/languages",\
                                                                         "stargazers_url": "https://api.github.com/repos/cappuccino/cappuccino/stargazers",\
                                                                         "contributors_url": "https://api.github.com/repos/cappuccino/cappuccino/contributors",\
                                                                         "subscribers_url": "https://api.github.com/repos/cappuccino/cappuccino/subscribers",\
                                                                         "subscription_url": "https://api.github.com/repos/cappuccino/cappuccino/subscription",\
                                                                         "commits_url": "https://api.github.com/repos/cappuccino/cappuccino/commits{/sha}",\
                                                                         "git_commits_url": "https://api.github.com/repos/cappuccino/cappuccino/git/commits{/sha}",\
                                                                         "comments_url": "https://api.github.com/repos/cappuccino/cappuccino/comments{/number}",\
                                                                         "issue_comment_url": "https://api.github.com/repos/cappuccino/cappuccino/issues/comments/{number}",\
                                                                         "contents_url": "https://api.github.com/repos/cappuccino/cappuccino/contents/{+path}",\
                                                                         "compare_url": "https://api.github.com/repos/cappuccino/cappuccino/compare/{base}...{head}",\
                                                                         "merges_url": "https://api.github.com/repos/cappuccino/cappuccino/merges",\
                                                                         "archive_url": "https://api.github.com/repos/cappuccino/cappuccino/{archive_format}{/ref}",\
                                                                         "downloads_url": "https://api.github.com/repos/cappuccino/cappuccino/downloads",\
                                                                         "issues_url": "https://api.github.com/repos/cappuccino/cappuccino/issues{/number}",\
                                                                         "pulls_url": "https://api.github.com/repos/cappuccino/cappuccino/pulls{/number}",\
                                                                         "milestones_url": "https://api.github.com/repos/cappuccino/cappuccino/milestones{/number}",\
                                                                         "notifications_url": "https://api.github.com/repos/cappuccino/cappuccino/notifications{?since,all,participating}",\
                                                                         "labels_url": "https://api.github.com/repos/cappuccino/cappuccino/labels{/name}",\
                                                                         "releases_url": "https://api.github.com/repos/cappuccino/cappuccino/releases{/id}",\
                                                                         "created_at": "2008-09-04T10:43:35Z",\
                                                                         "updated_at": "2015-02-02T19:40:36Z",\
                                                                         "pushed_at": "2015-01-15T21:44:25Z",\
                                                                         "git_url": "git://github.com/cappuccino/cappuccino.git",\
                                                                         "ssh_url": "git@github.com:cappuccino/cappuccino.git",\
                                                                         "clone_url": "https://github.com/cappuccino/cappuccino.git",\
                                                                         "svn_url": "https://github.com/cappuccino/cappuccino",\
                                                                         "homepage": "http://cappuccino-project.org",\
                                                                         "size": 59573,\
                                                                         "stargazers_count": 2051,\
                                                                         "watchers_count": 2051,\
                                                                         "language": "Objective-J",\
                                                                         "has_issues": true,\
                                                                         "has_downloads": true,\
                                                                         "has_wiki": true,\
                                                                         "has_pages": false,\
                                                                         "forks_count": 333,\
                                                                         "mirror_url": null,\
                                                                         "open_issues_count": 117,\
                                                                         "forks": 333,\
                                                                         "open_issues": 117,\
                                                                         "watchers": 2051,\
                                                                         "default_branch": "master",\
                                                                         "permissions": {\
                                                                           "admin": false,\
                                                                           "push": false,\
                                                                           "pull": true\
                                                                         }\
                                                                        },\
                                                                        {\
                                                                          "id": 52225,\
                                                                          "name": "ojunit",\
                                                                          "full_name": "cappuccino/ojunit",\
                                                                          "owner": {\
                                                                            "login": "cappuccino",\
                                                                            "id": 16595,\
                                                                            "avatar_url": "https://avatars.githubusercontent.com/u/16595?v=3",\
                                                                            "gravatar_id": "",\
                                                                            "url": "https://api.github.com/users/cappuccino",\
                                                                            "html_url": "https://github.com/cappuccino",\
                                                                            "followers_url": "https://api.github.com/users/cappuccino/followers",\
                                                                            "following_url": "https://api.github.com/users/cappuccino/following{/other_user}",\
                                                                            "gists_url": "https://api.github.com/users/cappuccino/gists{/gist_id}",\
                                                                            "starred_url": "https://api.github.com/users/cappuccino/starred{/owner}{/repo}",\
                                                                            "subscriptions_url": "https://api.github.com/users/cappuccino/subscriptions",\
                                                                            "organizations_url": "https://api.github.com/users/cappuccino/orgs",\
                                                                            "repos_url": "https://api.github.com/users/cappuccino/repos",\
                                                                            "events_url": "https://api.github.com/users/cappuccino/events{/privacy}",\
                                                                            "received_events_url": "https://api.github.com/users/cappuccino/received_events",\
                                                                            "type": "Organization",\
                                                                            "site_admin": false\
                                                                          },\
                                                                          "private": false,\
                                                                          "html_url": "https://github.com/cappuccino/ojunit",\
                                                                          "description": "OJUnit - Original unit testing framework for Objective-J. Soon to be deprecated in favor of http://github.com/280north/ojtest",\
                                                                          "fork": false,\
                                                                          "url": "https://api.github.com/repos/cappuccino/ojunit",\
                                                                          "forks_url": "https://api.github.com/repos/cappuccino/ojunit/forks",\
                                                                          "keys_url": "https://api.github.com/repos/cappuccino/ojunit/keys{/key_id}",\
                                                                          "collaborators_url": "https://api.github.com/repos/cappuccino/ojunit/collaborators{/collaborator}",\
                                                                          "teams_url": "https://api.github.com/repos/cappuccino/ojunit/teams",\
                                                                          "hooks_url": "https://api.github.com/repos/cappuccino/ojunit/hooks",\
                                                                          "issue_events_url": "https://api.github.com/repos/cappuccino/ojunit/issues/events{/number}",\
                                                                          "events_url": "https://api.github.com/repos/cappuccino/ojunit/events",\
                                                                          "assignees_url": "https://api.github.com/repos/cappuccino/ojunit/assignees{/user}",\
                                                                          "branches_url": "https://api.github.com/repos/cappuccino/ojunit/branches{/branch}",\
                                                                          "tags_url": "https://api.github.com/repos/cappuccino/ojunit/tags",\
                                                                          "blobs_url": "https://api.github.com/repos/cappuccino/ojunit/git/blobs{/sha}",\
                                                                          "git_tags_url": "https://api.github.com/repos/cappuccino/ojunit/git/tags{/sha}",\
                                                                          "git_refs_url": "https://api.github.com/repos/cappuccino/ojunit/git/refs{/sha}",\
                                                                          "trees_url": "https://api.github.com/repos/cappuccino/ojunit/git/trees{/sha}",\
                                                                          "statuses_url": "https://api.github.com/repos/cappuccino/ojunit/statuses/{sha}",\
                                                                          "languages_url": "https://api.github.com/repos/cappuccino/ojunit/languages",\
                                                                          "stargazers_url": "https://api.github.com/repos/cappuccino/ojunit/stargazers",\
                                                                          "contributors_url": "https://api.github.com/repos/cappuccino/ojunit/contributors",\
                                                                          "subscribers_url": "https://api.github.com/repos/cappuccino/ojunit/subscribers",\
                                                                          "subscription_url": "https://api.github.com/repos/cappuccino/ojunit/subscription",\
                                                                          "commits_url": "https://api.github.com/repos/cappuccino/ojunit/commits{/sha}",\
                                                                          "git_commits_url": "https://api.github.com/repos/cappuccino/ojunit/git/commits{/sha}",\
                                                                          "comments_url": "https://api.github.com/repos/cappuccino/ojunit/comments{/number}",\
                                                                          "issue_comment_url": "https://api.github.com/repos/cappuccino/ojunit/issues/comments/{number}",\
                                                                          "contents_url": "https://api.github.com/repos/cappuccino/ojunit/contents/{+path}",\
                                                                          "compare_url": "https://api.github.com/repos/cappuccino/ojunit/compare/{base}...{head}",\
                                                                          "merges_url": "https://api.github.com/repos/cappuccino/ojunit/merges",\
                                                                          "archive_url": "https://api.github.com/repos/cappuccino/ojunit/{archive_format}{/ref}",\
                                                                          "downloads_url": "https://api.github.com/repos/cappuccino/ojunit/downloads",\
                                                                          "issues_url": "https://api.github.com/repos/cappuccino/ojunit/issues{/number}",\
                                                                          "pulls_url": "https://api.github.com/repos/cappuccino/ojunit/pulls{/number}",\
                                                                          "milestones_url": "https://api.github.com/repos/cappuccino/ojunit/milestones{/number}",\
                                                                          "notifications_url": "https://api.github.com/repos/cappuccino/ojunit/notifications{?since,all,participating}",\
                                                                          "labels_url": "https://api.github.com/repos/cappuccino/ojunit/labels{/name}",\
                                                                          "releases_url": "https://api.github.com/repos/cappuccino/ojunit/releases{/id}",\
                                                                          "created_at": "2008-09-13T05:33:05Z",\
                                                                          "updated_at": "2014-07-31T12:49:05Z",\
                                                                          "pushed_at": "2010-03-31T23:37:57Z",\
                                                                          "git_url": "git://github.com/cappuccino/ojunit.git",\
                                                                          "ssh_url": "git@github.com:cappuccino/ojunit.git",\
                                                                          "clone_url": "https://github.com/cappuccino/ojunit.git",\
                                                                          "svn_url": "https://github.com/cappuccino/ojunit",\
                                                                          "homepage": "http://cappuccino.org",\
                                                                          "size": 106,\
                                                                          "stargazers_count": 25,\
                                                                          "watchers_count": 25,\
                                                                          "language": "Objective-J",\
                                                                          "has_issues": true,\
                                                                          "has_downloads": true,\
                                                                          "has_wiki": true,\
                                                                          "has_pages": false,\
                                                                          "forks_count": 3,\
                                                                          "mirror_url": null,\
                                                                          "open_issues_count": 0,\
                                                                          "forks": 3,\
                                                                          "open_issues": 0,\
                                                                          "watchers": 25,\
                                                                          "default_branch": "master",\
                                                                          "permissions": {\
                                                                            "admin": false,\
                                                                            "push": false,\
                                                                            "pull": true\
                                                                          }\
                                                                        }]'

bodies["https://api.github.com/orgs/little-dude/repos?per_page=100"] = '[]'

bodies["https://api.github.com/repos/cappuccino/ojtest/commits?per_page=100&since=2014-02-04T00:00:00.000001&until=2015-02-03T00:00:00.000001&author=little-dude"] = '[{"sha":"7ac6fd56dd614b1c124a594251dc694cb3930d9b",\
                                                                                                                                                                      "commit":{"author":{"name":"Alexandre Wilhelm",\
                                                                                                                                                                                          "email":"contact.dogild@gmail.com",\
                                                                                                                                                                                          "date":"2014-08-04T23:47:35Z"},\
                                                                                                                                                                                          "committer":{"name":"Alexandre Wilhelm",\
                                                                                                                                                                                          "email":"contact.dogild@gmail.com",\
                                                                                                                                                                                          "date":"2014-08-04T23:47:35Z"},\
                                                                                                                                                                                          "message":"Fixed: removed double methods...",\
                                                                                                                                                                                          "tree":{"sha":"e9e54d974b0411fa2c55199aba2fdd1dcd176781",\
                                                                                                                                                                                                  "url":"https://api.github.com/repos/cappuccino/OJTest/git/trees/e9e54d974b0411fa2c55199aba2fdd1dcd176781"},\
                                                                                                                                                                                          "url":"https://api.github.com/repos/cappuccino/OJTest/git/commits/7ac6fd56dd614b1c124a594251dc694cb3930d9b",\
                                                                                                                                                                                          "comment_count":0},\
                                                                                                                                                                        "url":"https://api.github.com/repos/cappuccino/OJTest/commits/7ac6fd56dd614b1c124a594251dc694cb3930d9b",\
                                                                                                                                                                        "html_url":"https://github.com/cappuccino/OJTest/commit/7ac6fd56dd614b1c124a594251dc694cb3930d9b",\
                                                                                                                                                                        "comments_url":"https://api.github.com/repos/cappuccino/OJTest/commits/7ac6fd56dd614b1c124a594251dc694cb3930d9b/comments",\
                                                                                                                                                                        "author":{"login":"Dogild","id":2860781,"avatar_url":"https://avatars.githubusercontent.com/u/2860781?v=3",\
                                                                                                                                                                        "gravatar_id":"","url":"https://api.github.com/users/Dogild",\
                                                                                                                                                                        "html_url":"https://github.com/Dogild",\
                                                                                                                                                                        "followers_url":"https://api.github.com/users/Dogild/followers",\
                                                                                                                                                                        "following_url":"https://api.github.com/users/Dogild/following{/other_user}",\
                                                                                                                                                                        "gists_url":"https://api.github.com/users/Dogild/gists{/gist_id}",\
                                                                                                                                                                        "starred_url":"https://api.github.com/users/Dogild/starred{/owner}{/repo}",\
                                                                                                                                                                        "subscriptions_url":"https://api.github.com/users/Dogild/subscriptions",\
                                                                                                                                                                        "organizations_url":"https://api.github.com/users/Dogild/orgs",\
                                                                                                                                                                        "repos_url":"https://api.github.com/users/Dogild/repos",\
                                                                                                                                                                        "events_url":"https://api.github.com/users/Dogild/events{/privacy}",\
                                                                                                                                                                        "received_events_url":"https://api.github.com/users/Dogild/received_events",\
                                                                                                                                                                        "type":"User","site_admin":false},\
                                                                                                                                                                        "committer":{"login":"Dogild",\
                                                                                                                                                                                     "id":2860781,\
                                                                                                                                                                                     "avatar_url":"https://avatars.githubusercontent.com/u/2860781?v=3",\
                                                                                                                                                                                     "gravatar_id":"","url":"https://api.github.com/users/Dogild",\
                                                                                                                                                                                     "html_url":"https://github.com/Dogild",\
                                                                                                                                                                                     "followers_url":"https://api.github.com/users/Dogild/followers",\
                                                                                                                                                                                     "following_url":"https://api.github.com/users/Dogild/following{/other_user}",\
                                                                                                                                                                                     "gists_url":"https://api.github.com/users/Dogild/gists{/gist_id}",\
                                                                                                                                                                                     "starred_url":"https://api.github.com/users/Dogild/starred{/owner}{/repo}",\
                                                                                                                                                                                     "subscriptions_url":"https://api.github.com/users/Dogild/subscriptions",\
                                                                                                                                                                                     "organizations_url":"https://api.github.com/users/Dogild/orgs",\
                                                                                                                                                                                     "repos_url":"https://api.github.com/users/Dogild/repos",\
                                                                                                                                                                                     "events_url":"https://api.github.com/users/Dogild/events{/privacy}",\
                                                                                                                                                                                     "received_events_url":"https://api.github.com/users/Dogild/received_events",\
                                                                                                                                                                                     "type":"User","site_admin":false},"parents":[{"sha":"410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                                                                                   "url":"https://api.github.com/repos/cappuccino/OJTest/commits/410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                                                                                   "html_url":"https://github.com/cappuccino/OJTest/commit/410d9ceaefe4fefac6b7b5726f6c260c4e90121b"}]},\
                                                                                                                                                                    {"sha":"410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                    "commit":{"author":{"name":"Alexandre Wilhelm",\
                                                                                                                                                                                        "email":"contact.dogild@gmail.com",\
                                                                                                                                                                                        "date":"2014-08-04T23:44:20Z"},\
                                                                                                                                                                                        "committer":{"name":"Alexandre Wilhelm",\
                                                                                                                                                                                                     "email":"contact.dogild@gmail.com",\
                                                                                                                                                                                                     "date":"2014-08-04T23:44:20Z"},\
                                                                                                                                                                                                     "message":"New: Added the number of tests launched\\n\\nPreviously, when a suite of tests ended, we didn\'t know how many tests were launched.\\nNow we know. The formats of the message can be :\\n\\n-   All tests passed in the test suite.\\n    Total tests: 176\\n\\n-   Test suite failed with 0 errors and 1 failures and 175 successes\\n    Total tests : 176",\
                                                                                                                                                                                                     "tree":{"sha":"d58a281a3ee9b990fcdb6258f20aba5ddf138aaf",\
                                                                                                                                                                                                             "url":"https://api.github.com/repos/cappuccino/OJTest/git/trees/d58a281a3ee9b990fcdb6258f20aba5ddf138aaf"},\
                                                                                                                                                                                                     "url":"https://api.github.com/repos/cappuccino/OJTest/git/commits/410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                                                     "comment_count":0},\
                                                                                                                                                                                        "url":"https://api.github.com/repos/cappuccino/OJTest/commits/410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                                        "html_url":"https://github.com/cappuccino/OJTest/commit/410d9ceaefe4fefac6b7b5726f6c260c4e90121b",\
                                                                                                                                                                                        "comments_url":"https://api.github.com/repos/cappuccino/OJTest/commits/410d9ceaefe4fefac6b7b5726f6c260c4e90121b/comments",\
                                                                                                                                                                                        "author":{"login":"Dogild",\
                                                                                                                                                                                                  "id":2860781,\
                                                                                                                                                                                                  "avatar_url":"https://avatars.githubusercontent.com/u/2860781?v=3",\
                                                                                                                                                                                                  "gravatar_id":"","url":"https://api.github.com/users/Dogild",\
                                                                                                                                                                                                  "html_url":"https://github.com/Dogild",\
                                                                                                                                                                                                  "followers_url":"https://api.github.com/users/Dogild/followers",\
                                                                                                                                                                                                  "following_url":"https://api.github.com/users/Dogild/following{/other_user}",\
                                                                                                                                                                                                  "gists_url":"https://api.github.com/users/Dogild/gists{/gist_id}",\
                                                                                                                                                                                                  "starred_url":"https://api.github.com/users/Dogild/starred{/owner}{/repo}",\
                                                                                                                                                                                                  "subscriptions_url":"https://api.github.com/users/Dogild/subscriptions",\
                                                                                                                                                                                                  "organizations_url":"https://api.github.com/users/Dogild/orgs",\
                                                                                                                                                                                                  "repos_url":"https://api.github.com/users/Dogild/repos",\
                                                                                                                                                                                                  "events_url":"https://api.github.com/users/Dogild/events{/privacy}",\
                                                                                                                                                                                                  "received_events_url":"https://api.github.com/users/Dogild/received_events",\
                                                                                                                                                                                                  "type":"User","site_admin":false},\
                                                                                                                                                                                        "committer":{"login":"Dogild",\
                                                                                                                                                                                                     "id":2860781,\
                                                                                                                                                                                                     "avatar_url":"https://avatars.githubusercontent.com/u/2860781?v=3",\
                                                                                                                                                                                                     "gravatar_id":"","url":"https://api.github.com/users/Dogild",\
                                                                                                                                                                                                     "html_url":"https://github.com/Dogild",\
                                                                                                                                                                                                     "followers_url":"https://api.github.com/users/Dogild/followers",\
                                                                                                                                                                                                     "following_url":"https://api.github.com/users/Dogild/following{/other_user}",\
                                                                                                                                                                                                     "gists_url":"https://api.github.com/users/Dogild/gists{/gist_id}",\
                                                                                                                                                                                                     "starred_url":"https://api.github.com/users/Dogild/starred{/owner}{/repo}",\
                                                                                                                                                                                                     "subscriptions_url":"https://api.github.com/users/Dogild/subscriptions",\
                                                                                                                                                                                                     "organizations_url":"https://api.github.com/users/Dogild/orgs",\
                                                                                                                                                                                                     "repos_url":"https://api.github.com/users/Dogild/repos",\
                                                                                                                                                                                                     "events_url":"https://api.github.com/users/Dogild/events{/privacy}",\
                                                                                                                                                                                                     "received_events_url":"https://api.github.com/users/Dogild/received_events",\
                                                                                                                                                                                                     "type":"User","site_admin":false},\
                                                                                                                                                                                        "parents":[{"sha":"c289fa7bee69a8cef7adeafbeede25d90cf2e51e",\
                                                                                                                                                                                                    "url":"https://api.github.com/repos/cappuccino/OJTest/commits/c289fa7bee69a8cef7adeafbeede25d90cf2e51e",\
                                                                                                                                                                                                    "html_url":"https://github.com/cappuccino/OJTest/commit/c289fa7bee69a8cef7adeafbeede25d90cf2e51e"}]}]'






























