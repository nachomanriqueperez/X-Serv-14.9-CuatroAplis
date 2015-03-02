#!/usr/bin/python


class hola():

        def parse(self, request, rest):
            return "Listo"

        def process(self, parsedRequest):
            return ("200 OK", "<html><body><b>Hola Mundo!</h1></body></html>")
