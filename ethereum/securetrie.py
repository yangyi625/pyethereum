from ethereum import utils


class SecureTrie(object):

    def __init__(self, t):
        self.trie = t
        self.db = t.db

    def update(self, k, v):
        h = utils.sha3(k)
        self.db.put(h, utils.str_to_bytes(k))
        self.trie.update(h, v)

    def get(self, k):
        return self.trie.get(utils.sha3(k))
    # Trie don't support delete for the moment
    # def delete(self, k):
    #     self.trie.delete(utils.sha3(k))

    def to_dict(self, hexify=False):
        o = {}
        for h, v in list(self.trie.to_dict(hexify).items()):
            k = self.db.get(h)
            o[k] = v
        return o
    
    # Trie don't support branch for the moment
    # def iter_branch(self):
    #     for h, v in self.trie.iter_branch():
    #         k = self.db.get(h)
    #         yield (k, v)

    # def root_hash_valid(self):
    #     return self.trie.root_hash_valid()

    @property
    def root_hash(self):
        return self.trie.root_hash

    @root_hash.setter
    def root_hash(self, value):
        self.trie.root_hash = value

    # Trie don't support delete for the moment
    # @property
    # def deletes(self):
    #     return self.trie.deletes

    # Trie don't support delete for the moment
    # @deletes.setter
    # def deletes(self, value):
    #     self.trie.deletes = value
