import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]


@app.get('/pares')
def get_list():
    return {'name': 'Juan', 'age': 30}


@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Hay texto HTML aca</title>
        </head>
        <body>
            <h1>Soy un parrafo! HTML!</h1>
        </body>
    </html>
    """


def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()