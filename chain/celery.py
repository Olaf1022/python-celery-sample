from celery import Celery
import os
app = Celery(
    'chain',
    broker='redis://localhost',
    backend='redis://localhost',
    include=['chain.tasks'])

if __name__ == '__main__':
    app.start()
