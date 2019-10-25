#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import sys
import getopt

app = Flask(__name__)
api = Api(app)


class Version(Resource):
    def get(self):
        return "0.0.2", 200


class Echo(Resource):
    def get(self, request):
        return request+" is ok!", 200

    def delete(self, request):
        return request+" delete", 200


api.add_resource(Echo, '/echo/<request>')
api.add_resource(Version, '/version')


def StartServer(port):
    app.run(debug=False, port=port)
    return


def main(argv):
    port = 5000
    try:
        opts, args = getopt.getopt(argv, "p", ["port="])
    except getopt.GetoptError:
        print('server.py -p <绑定端口>')
        sys.exit(2)

    print(opts)
    print(args)
    for opt, arg in opts:
        if opt in ("-p", "--port"):
            port = int(arg)

    StartServer(port)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
