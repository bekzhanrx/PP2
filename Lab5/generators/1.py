class gen:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a*self.a <= 100:
            x = self.a
            self.a += 1
            x = x**2
            return x
        else:
            raise StopIteration


z = gen()
i = iter(z)
for c in i:
    print(c)
