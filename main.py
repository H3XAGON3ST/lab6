def AddString(str_list, pos, str):
        try:
                str_list.insert(pos, str)
                if (str_list.index(str)!=pos):
                        raise Exception()
                return str_list
        except:
                return "paste operation is not possible"
