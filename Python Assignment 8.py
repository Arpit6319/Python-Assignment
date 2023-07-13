class A:
    def _init_(self, a, b, c):
        self.__a = a  # private member
        self._b = b   # protected member
        self.c = c    # public member

    def display_A(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display_B(self):
        print("Values in class B:")
        try:
            print("a:", self.__a)  # accessing private member raises an exception
        except NameError:
            print("Cannot access private member 'a' in class B")
        except Exception:
            ("Private variable invalid accessing Error Raised")
        print("b:", self._b)
        print("c:", self.c)


# Creating an instance of class A and calling display()
obj_a = A(1, 2, 3)
obj_a.display()

# Creating an instance of class B and calling display()
obj_b = B(4, 5, 6)
obj_b.display()