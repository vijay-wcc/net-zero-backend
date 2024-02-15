# Project Structure


```markdown

/app
        /api
            __init__.py
            /v1
                __init__.py
                /endpoints
                    __init__.py
                    item_router.py
        /core
            __init__.py
            config.py
        /crud
            __init__.py
            crud_item.py
        /db
            __init__.py
            base_class.py
            session.py
            models.py
        /schemas
            __init__.py
            item.py
        main.py
    alembic.ini
    /alembic
        /versions
    .env
    requirements.txt
```