from flask import Flask
from flask import make_response
from flask_restful import Resource
from flask_restful import Api
import os
import os.path


def stat(path):
    st = os.stat(path)
    s = {}
    s['atime'] = st.st_atime
    s['blksize'] = st.st_blksize
    s['blocks'] = st.st_blocks
    s['ctime'] = st.st_ctime
    s['dev'] = st.st_dev
    s['gid'] = st.st_gid
    s['ino'] = st.st_ino
    s['mode'] = st.st_mode
    s['mtime'] = st.st_mtime
    s['nlink'] = st.st_nlink
    s['rdev'] = st.st_rdev
    s['size'] = st.st_size
    s['uid'] = st.st_uid
    return s


class FS(Resource):
    def get(self, path='/'):
        if path[0] != '/':
            path = os.path.join('/', path)
        ret = {}
        if os.path.isdir(path):
            for entry in os.listdir(path):
                ret[entry] = \
                    stat(os.path.join(path, entry))
        else:
            ret = make_response(open(path).read())
            ret.headers['Content-Type'] = 'application/octet-stream'
        return ret


app = Flask(__name__)
api = Api(app)
api.add_resource(FS,'/', '/<path:path>')
