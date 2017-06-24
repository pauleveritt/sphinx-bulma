from livereload import Server, shell

cmd = "env/bin/python3 env/bin/sphinx-build -E -b html docs docs/_build"

server = Server()
delay = 1
server.watch('docs/*.rst', shell(cmd), delay=delay)
server.watch('src/sphinx_bulma/*.html', shell(cmd), delay=delay)
server.watch('src/sphinx_bulma/*.scss', shell(cmd), delay=delay)
server.serve(root='docs/_build')

