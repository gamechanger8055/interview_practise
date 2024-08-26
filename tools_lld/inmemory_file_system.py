class TrieNode:
    def __init__(self):
        self.children={}
        self.is_file=False
        self.content=""

class FileSystem:
    def __init__(self):
        self.root=TrieNode()

    def find(self,path):
        current=self.root
        if path=="/":
            return current
        parts=path.split("/")[1:]
        for part in parts:
            if part not in current.children:
                return
            current=current.children[part]
        return current

    def mkdir(self,path):
        current=self.root
        parts = path.split("/")[1:]
        for part in parts:
            if part not in current.children:
                current.children[part]=TrieNode()
            current = current.children[part]

    def add_content_to_file(self,file_path,content):
        current = self.root
        parts = file_path.split("/")[1:]
        for part in parts[:-1]:
            if part not in current.children:
                current.children[part]=TrieNode()
            current = current.children[part]
        if parts[-1] not in current.children:
            current.children[parts[-1]] = TrieNode()
        current = current.children[parts[-1]]
        current.is_file=True
        current.content+=content


    def read_content_from_file(self,file_path):
        node=self.find(file_path)
        if node and node.is_file:
            return node.content
        return ""

    def ls(self,path):
        node = self.find(path)
        if not node:
            return []
        if node.is_file:
            return [path.split('/')[-1]]
        return node.children.keys()


# Example usage:
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.add_content_to_file("/a/b/c/d", "hello")
print(fs.read_content_from_file("/a/b/c/d"))  # Output: hello
print(fs.ls("/a/b"))  # Output: ['c']


