class TagCloud:
    def __init__(self):
        self.__tags = {}  # prefic with double undercore to make attribute or methods private!

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
# priint(cloud.tags) cannot be accessed because its private

# however you can access private once you find it with the __dict__ attribute.
print(cloud.__dict__)
print(cloud._TagCloud__tags)
