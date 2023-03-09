# -*- coding: utf-8 -*-
#
# Handler exposing application files
import os

from globaleaks.handlers.base import BaseHandler
from globaleaks.rest import errors
from globaleaks.utils.fs import directory_traversal_check


class StaticFileHandler(BaseHandler):
    check_roles = 'any'
    allowed_mimetypes = [
        'text/css',
        'text/html',
        'text/javascript'
    ]

    def __init__(self, state, request):
        BaseHandler.__init__(self, state, request)

        self.root = "%s%s" % (os.path.abspath(state.settings.client_path), "/")

        if not state.settings.disable_csp:
            request.setHeader(b'Content-Security-Policy',
                              b"base-uri 'none';"
                              b"connect-src 'self';"
                              b"default-src 'none';"
                              b"font-src 'self' data:;"
                              b"form-action 'none';"
                              b"frame-ancestors 'none';"
                              b"frame-src 'self';"
                              b"img-src 'self' data:;"
                              b"media-src 'self';"
                              b"script-src 'self' 'sha256-l4srTx31TC+tE2K4jVVCnC9XfHivkiSs/v+DPWccDDM=';"
                              b"style-src 'self' 'sha256-fwyo2zCGlh85NfN4rQUlpLM7MB5cry/1AEDA/G9mQJ8=';")

    def get(self, filename):
        if not filename:
            filename = 'index.html'

        abspath = os.path.abspath(os.path.join(self.root, filename))
        directory_traversal_check(self.root, abspath)

        return self.write_file(filename, abspath)
