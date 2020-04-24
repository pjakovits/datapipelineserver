import connexion
import six

import os
from flask import Flask, Response

from openapi_server.models.data_pipeline import DataPipeline  # noqa: E501
from openapi_server import util


def submit_datapipeline(data_pipeline=None):  # noqa: E501
    """Submit a data pipeline

     # noqa: E501

    :param data_pipeline: 
    :type data_pipeline: dict | bytes

    :rtype: file
    """
    if connexion.request.is_json:
        data_pipeline = DataPipeline.from_dict(connexion.request.get_json())  # noqa: E501
    #   return 'do some magic!'



    file =  connexion.request.files['file']
    filepath = '/tmp/' + file.filename
    file.save(filepath)

    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
        ".jpeg": "image/jpeg",
        ".csar": "application/octet-stream",
    }

    ext = os.path.splitext(filepath)[1]
    mimetype = mimetypes.get(ext, "image/jpeg")
    with open(filepath, 'rb') as f:
      content =  f.read()
    
    
    return send_file(io.BytesIO(content), as_attachment=True, attachment_filename=file.filename, mimetype=mimetype)

