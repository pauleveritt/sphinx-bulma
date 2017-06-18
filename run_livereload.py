from livereload import Server, shell

cmd = "env/bin/python3 env/bin/sphinx-build -b html docs docs/_build"

server = Server()
server.watch('docs/*.rst', shell(cmd))
server.watch('src/sphinx_bulma/*.html', shell(cmd))
server.watch('src/sphinx_bulma/*.scss', shell(cmd))
server.serve(root='docs/_build')

