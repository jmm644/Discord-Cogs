
class Links:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def href(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('href', dict())

    @property
    def rel(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('rel', dict())

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())


class Title_Detail:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())

    @property
    def language(self):
        '''Will return <class 'NoneType'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('language', dict())

    @property
    def base(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('base', dict())

    @property
    def value(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('value', dict())


class Subtitle_Detail:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())

    @property
    def language(self):
        '''Will return <class 'NoneType'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('language', dict())

    @property
    def base(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('base', dict())

    @property
    def value(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('value', dict())


class Image:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def href(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('href', dict())


class Feed:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def links(self):
        '''Will return a generator with instances of class Links(). If no data is available, an empty dict or None is returned'''
        return (Links(item) for item in self.items.get('links', dict()) if item)

    @property
    def title(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('title', dict())

    @property
    def title_detail(self):
        '''Will return class Title_Detail(). If no data is available, an empty dict or None is returned'''
        return Title_Detail(self.items.get('title_detail', dict()))

    @property
    def link(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('link', dict())

    @property
    def subtitle(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('subtitle', dict())

    @property
    def subtitle_detail(self):
        '''Will return class Subtitle_Detail(). If no data is available, an empty dict or None is returned'''
        return Subtitle_Detail(self.items.get('subtitle_detail', dict()))

    @property
    def language(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('language', dict())

    @property
    def ttl(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('ttl', dict())

    @property
    def image(self):
        '''Will return class Image(). If no data is available, an empty dict or None is returned'''
        return Image(self.items.get('image', dict()))


class _Title_Detail:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())

    @property
    def language(self):
        '''Will return <class 'NoneType'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('language', dict())

    @property
    def base(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('base', dict())

    @property
    def value(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('value', dict())


class Authors:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def name(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('name', dict())


class Author_Detail:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def name(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('name', dict())


class Summary_Detail:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())

    @property
    def language(self):
        '''Will return <class 'NoneType'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('language', dict())

    @property
    def base(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('base', dict())

    @property
    def value(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('value', dict())


class _Links:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def rel(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('rel', dict())

    @property
    def type(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('type', dict())

    @property
    def href(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('href', dict())


class Entries:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def title(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('title', dict())

    @property
    def title_detail(self):
        '''Will return class _Title_Detail(). If no data is available, an empty dict or None is returned'''
        return _Title_Detail(self.items.get('title_detail', dict()))

    @property
    def authors(self):
        '''Will return a generator with instances of class Authors(). If no data is available, an empty dict or None is returned'''
        return (Authors(item) for item in self.items.get('authors', dict()) if item)

    @property
    def author(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('author', dict())

    @property
    def author_detail(self):
        '''Will return class Author_Detail(). If no data is available, an empty dict or None is returned'''
        return Author_Detail(self.items.get('author_detail', dict()))

    @property
    def summary(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('summary', dict())

    @property
    def summary_detail(self):
        '''Will return class Summary_Detail(). If no data is available, an empty dict or None is returned'''
        return Summary_Detail(self.items.get('summary_detail', dict()))

    @property
    def published(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('published', dict())

    @property
    def published_parsed(self):
        '''Will return <class 'time.struct_time'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('published_parsed', dict())

    @property
    def id(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('id', dict())

    @property
    def guidislink(self):
        '''Will return <class 'bool'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('guidislink', dict())

    @property
    def link(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('link', dict())

    @property
    def links(self):
        '''Will return a generator with instances of class _Links(). If no data is available, an empty dict or None is returned'''
        return (_Links(item) for item in self.items.get('links', dict()) if item)

    @property
    def twitter_source(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('twitter_source', dict())

    @property
    def twitter_place(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('twitter_place', dict())


class Namespaces:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def _(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('', dict())

    @property
    def georss(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('georss', dict())

    @property
    def twitter(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('twitter', dict())

    @property
    def dc(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('dc', dict())


class Rss_Feed:
    def __init__(self, items):
        if items:
            self.items = items
        else:
            self.items = dict()

    @property
    def feed(self):
        '''Will return class Feed(). If no data is available, an empty dict or None is returned'''
        return Feed(self.items.get('feed', dict()))

    @property
    def entries(self):
        '''Will return a generator with instances of class Entries(). If no data is available, an empty dict or None is returned'''
        return (Entries(item) for item in self.items.get('entries', dict()) if item)

    @property
    def bozo(self):
        '''Will return <class 'int'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('bozo', dict())

    @property
    def encoding(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('encoding', dict())

    @property
    def version(self):
        '''Will return <class 'str'>. If no data is available, an empty dict or None is returned'''
        return self.items.get('version', dict())

    @property
    def namespaces(self):
        '''Will return class Namespaces(). If no data is available, an empty dict or None is returned'''
        return Namespaces(self.items.get('namespaces', dict()))
