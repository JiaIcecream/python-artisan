from jinja2 import Template


_MOVIES_TMPL = '''\
Welcome, {{username}}.
{%for name, rating in movies %}
* {{ name }}, Rating: {{ rating|default("[NOT RATED]), True }}
{%- endfor %}
'''

def render_movies(username, movies):
  tmpl = Template(_MOVIES_TMPL)
  return tmpl.render(username = username, movies=movies)

movies = [
    ('The Shawshank Redemption', '9.3'),
    ('The Prestige', '8.5'),
    ('Mulan', None),
]

print(render_movies('piglei', movies))