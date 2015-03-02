#!/usr/bin/python

import random


class aleat():

    def parse(self, request, rest):
        return "Listo"

    def process(self, parsedRequest):
        num_al = random.randrange(100000)
        return ("200 OK", "<html><body><h1>Hello World!</h1>" +
                "<a href='" + str(num_al) + "'>Dame otra url</a>" +
                "</body></html>")
