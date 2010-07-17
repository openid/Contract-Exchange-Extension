import simplejson

class CX:
    CXNS=r'http://specs.openid.net/extensions/cx/1.0/#(.+)'
    def __init__(self,jtype):
        self.jtype = jtype
        self.json = simplejson.loads('{}') 

    @classmethod
    def parse_jtype(cls,jobj):
        if jobj.has_key('type'):
            
    @classmethod
    def parse(cls,json_string ):
        j = simplejson.loads(json_string)

class Request:
    def __init__(self):
        pass 
