import os
import sys
import requests


project = 'scikit-image'
team = 'core'
emeritus_team = 'emeritus'
team_url = f'https://api.github.com/orgs/{project}/teams/{team}/members'
emeritus_team_url = f'https://api.github.com/orgs/{project}/teams/{emeritus_team}/members'


token = os.environ.get('GH_TOKEN', None)
if token is None:
    print("No token found.  Please export a GH_TOKEN with permissions "
          "to read team members.")
    sys.exit(-1)


def api(url):
    json = requests.get(url=url,
                        headers={'Authorization': f'token {token}'}).json()
    if 'message' in json and json['message'] == 'Bad credentials':
        raise RuntimeError('Invalid token provided')
    else:
        return json


resp = api(team_url)
team = sorted(resp, key=lambda user: user['login'].lower())

resp = api(emeritus_team_url)
emeritus_team = sorted(resp, key=lambda user: user['login'].lower())


def render_team(team):
    for member in team:
        profile = api(member['url'])

        print(f"""
.. raw:: html

   <div class="team-member">
     <a href="https://github.com/{member['login']}" class="team-member-name">
        <div class="team-member-photo">
           <img
             src="{member['avatar_url']}&s=40"
             loading="lazy"
             alt="Avatar picture of @{profile['login']}"
           />
        </div>
        {profile['name'] if profile['name'] else '@' + profile['login']}
     </a>
     <div class="team-member-handle">@{member['login']}</div>
   </div>
""")


print("""
Our Team
--------

Along with a large community of contributors, scikit-image development
is guided by the following core team:

""")

render_team(team)

print("""

Emeritus Developers
-------------------

We thank these previously-active core developers for their contributions to scikit-image.

""")

render_team(emeritus_team)
