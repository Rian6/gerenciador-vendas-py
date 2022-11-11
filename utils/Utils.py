class Utils():
    def processId(id):
        ns = ""
        for i in id:
            if(i == "-"):
                break
            ns = ns+i
        return int(ns)