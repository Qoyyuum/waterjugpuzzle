from dataclasses import dataclass

@dataclass
class Jug:
    name:str
    current:int
    maximum_capacity:int

    def fill(self):
        "Filling Jug to full capacity"
        self.current = self.maximum_capacity
        print(f"Filled {self.name} to {self.current}")
        return f"Filled {self.name} to {self.current}"

    def empty(self):
        "Emptying Jug to 0"
        self.current = 0
        print(f"Emptied {self.name} to 0")
        return f"Emptied {self.name} to 0"

    def status(self) -> str:
        print(f"Jug: {self.name} = {self.current} / {self.maximum_capacity}")
        return f"Jug: {self.name} = {self.current} / {self.maximum_capacity}"

    def __repr__(self):
        return f"Jug: {self.name} = {self.current} / {self.maximum_capacity}"

    def __str__(self):
        return f"Jug: {self.name} = {self.current} / {self.maximum_capacity}"

@dataclass
class JugsProblem:
    jugs:list
    goal:int


    def status(self):
        for jug in self.jugs:
            jug.status()
            return self.jugs
        return None


    def fill(self, which_jug) -> bool:
        """Fill which jug"""
        for jug in self.jugs:
            if jug.name == which_jug:
                jug.fill()
                self.status()
                return True
        else:
            print(f"Jug {which_jug} NOT FOUND")
        self.status()
        return False


    def empty(self, which_jug) -> bool:
        """Empty which jug"""
        for jug in self.jugs:
            if jug.name == which_jug:
                jug.empty()
                self.status()
                return True
        else:
            print(f"Jug {which_jug} NOT FOUND")
        self.status()
        return False

    def findjug(self, jug_name):
        for jug in self.jugs:
            if jug.name in jug_name:
                print(f"Found jug: {jug_name}")
                return jug
        print(f"Jug: {jug_name} NOT FOUND")
        return None


    def transfer(self, from_jug, to_jug) -> bool:
        """Transfer water from_jug to to_jug, up to the limit of to_jug"""
        if from_jug == to_jug:
            print("Can't transfer to the same jug")
            return False

        A = self.findjug(from_jug)
        B = self.findjug(to_jug)
        if A and B:
            while A.current >= 1 and B.current <= B.maximum_capacity-1:
                print(f"Transfering from:\n{A.name} ({A.current}/{A.maximum_capacity})\nto\n{B.name} ({B.current}/{B.maximum_capacity})")
                A.current -= 1
                B.current += 1
            self.status()
            return True
        print(f"Unable to transfer:\nfrom: {from_jug}\nto: {to_jug}")
        return False

    def goalcheck(self) -> bool:
        for jug in self.jugs:
            if jug.current == self.goal:
                print("PROBLEM SOLVED!")
                return True
        else:
            print("Still a problem")
            self.status()
            return False


def main():
    jug_a = Jug(name="A", current=0, maximum_capacity=3)
    jug_b = Jug(name="B", current=0, maximum_capacity=5)
    jugs = [jug_a, jug_b]
    problem = JugsProblem(jugs=jugs, goal=4)
    problem.fill(which_jug="B")
    problem.transfer(from_jug="B",to_jug="A")
    problem.empty(which_jug="A")
    problem.transfer(from_jug="B",to_jug="A")
    problem.fill(which_jug="B")
    problem.transfer(from_jug="B",to_jug="A")
    problem.goalcheck()


if __name__ == '__main__':
    main()
