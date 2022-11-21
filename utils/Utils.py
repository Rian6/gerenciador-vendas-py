class Utils():
    def processId(id):
        ns = ""
        if(type(id) is str):
            for i in id:
                if(i == "-"):
                    break
                ns = ns+i
        if(ns == ""):
            return None
        return int(ns)