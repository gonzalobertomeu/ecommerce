# coding=utf_8

import utils.mongo as db
import utils.errors as error
import re


def searchArticles(text):
    """
    Busca articulos por nombre o descripcion.\n
    test string Texto a buscar
    """
    """
    @api {get} /articles/search/:criteria Buscar articulos
    @apiName SearchArticle
    @apiGroup Articulos
    @apiDescription Busca articulos por nombre o descripci&oacute;n

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        [
            {
                "_id": "{id de articulo}"
                "name": "{nombre del articulo}",
                "description": "{descripcion del articulo}",
                "image": "{id de imagen}",
                "price": {precio actual},
                "stock": {stock actual}
                "updated": {fecha ultima actualizacion}
                "created": {fecha creacion}
                "enabled": {activo}
            },
            ...
        ]

    @apiUse Errors
    """
    try:
        regx = re.compile(text, re.IGNORECASE)
        results = []

        cursor = db.articles.find({
            "$and": [{
                "enabled": True
            }, {
                "$or": [{
                    "name": regx
                }, {
                    "description": regx
                }]
            }]
        })
        for doc in cursor:
            results.append(doc)
        return results
    except Exception:
        raise error.InvalidRequest("Invalid search criteria")
