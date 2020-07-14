class Category:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.value_list = []
        self.op_list = []

    def __str__(self):
        name_width = len(self.name)
        line_width = 30
        lines = []

        lines.append("")
        lines[0] += "*" * int((line_width - name_width)/2)

        lines[0] += self.name
        i = len(lines[0])

        while i < line_width:
            lines[0] += "*"
            i += 1
        lines[0] += "\n"

        for i in range(len(self.value_list)):
            line = self.op_list[i][:23]

            line += " " * \
                (line_width - len(line) - len(self.value_list[i]))
            line += (self.value_list[i])
            line += "\n"
            lines.append(line)

        lines.append("Total: %.2f" % (self.value))

        return "".join(lines)

    def deposit(self, value, operation=""):
        self.value += value
        self.value_list.append("+%.2f" % value)
        self.op_list.append(operation)

    def withdraw(self, value, operation=""):
        self.value -= value
        self.value_list.append("-%.2f" % value)
        self.op_list.append(operation)

    def transfer(self, value, target):
        self.withdraw(value, ("Transfer to " + target.name.capitalize()))
        target.deposit(value, ("Transfer from " + self.name.capitalize()))

    def get_balance(self):
        return self.value


def create_spend_chart(categories):
    chart = ""

    return chart
