from livereload import Server, shell

# Создаём сервер
server = Server()

# Слежение за HTML-файлами в папке dist
server.watch('dist/*.html')

# Слежение за CSS
server.watch('dist/*.css')

# Слежение за JS (если есть)
server.watch('dist/*.js')

# Также можно следить за любой другой задачей, например сборкой
# server.watch('src/', shell('make html', cwd='docs'))

# Запускаем сервер — он по умолчанию слушает порт 5500
server.serve(root='dist')