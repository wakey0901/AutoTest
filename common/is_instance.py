class IsInstance:

    def get_instance(self, value, check):
        flag = None
        if isinstance(value, str):
            if check == value:
                flag = True
            else:
                flag = False
        elif isinstance(value, float):
            if value - float(check) == 0:
                flag = True
            else:
                flag = False
        elif isinstance(value, int):
            if value - int(check) == 0:
                flag = True
            else:
                flag = False
        return flag
