from pyhtmldsl import h


html = h('html', {'lang': 'en'}, [
    h('head', [
        h('meta', {'charset': 'UTF-8'}),
        h('meta', {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}),
        h('meta', {'http-equiv': 'X-UA-Compatible', 'content': 'ie=edge'}),
        h('title', ['Document']),
    ]),
    h('body')
])

print(html.html())
