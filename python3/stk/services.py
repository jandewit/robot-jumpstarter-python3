class ServiceCache(object):

    def __init__(self, bridge):
        self.bridge = bridge

    def __getattr__(self, servicename):
        # print(servicename)
        return ServiceWrapper(self.bridge, servicename)



class ServiceWrapper(object):
    def __init__(self, bridge, servicename):
        self.bridge = bridge
        self.servicename = servicename

    def __getattr__(self, functionname):
        # print(functionname)

        def wrapper(*args, **kw):
            # print('called with %r and %r' % (args, kw))
            argstr = list()

            for a in args:
                if isinstance(a, str):
                    argstr.append('"' + a + '"')
                else:
                    argstr.append(str(a))

            self.bridge.sendMessage("python27:self.s." + self.servicename + "." + functionname + "(" + ','.join(argstr) + ")")
            # return getattr(self.child, attr)(*args, **kw)
        return wrapper        