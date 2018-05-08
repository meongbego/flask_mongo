class Paginate():
    """
    Pembuatan Paging
    """
    def __init__(self):
        pass

    @classmethod
    def create(self,data, url, start, limit):
        count = len(data)
        obj = {}
        obj['start'] = start
        obj['limit'] = limit
        obj['total'] = count
        obj['code'] = 200
        obj['status'] = 'success'
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start - limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        obj['data'] = data[(start - 1):(start - 1 + limit)]
        return obj
